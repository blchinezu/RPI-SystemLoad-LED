import subprocess
import time
import RPi.GPIO as GPIO


# Pin numbers
red = 15
green = 13
blue = 11

checkInterval = 1.0 # Seconds

Freq = 100 # Hz

# Functions
def setRGB(R, G, B):
    """
    R, G & B range from 0 to 100
    """

    # Safety first
    if  R < 0 or R > 100 or \
        G < 0 or G > 100 or \
        B < 0 or B > 100:
        return

    # Duty after
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)


def setFadedRGB(R, G, B, newR, newG, newB, interval):

    # Avoid useless processing
    if R == newR and G == newG and B == newB:
        time.sleep(interval)
        return

    # Make sure we don't have broken maths
    (R, G, B, newR, newG, newB, interval) = (float(R), float(G), float(B), float(newR), float(newG), float(newB), float(interval))

    # Keep at least 1 iteration
    fadeInterval = 0.05
    if interval < fadeInterval:
        interval = fadeInterval
    nbIterations = round(interval / fadeInterval)

    # Check how much should be changed for each color per iteration
    deltaR = (newR - R) / nbIterations
    deltaG = (newG - G) / nbIterations
    deltaB = (newB - B) / nbIterations

    prevR = int(R)
    prevG = int(G)
    prevB = int(B)

    # Fade to the new color
    for i in range(0, nbIterations):
        time.sleep(fadeInterval)

        currR = int(R + deltaR * i)
        currG = int(G + deltaG * i)
        currB = int(B + deltaB * i)

        if prevR != currR or prevG != currG or prevB != currB:
            setRGB(currR, currG, currB)
            prevR = currR
            prevG = currG
            prevB = currB

def pulseRGB(R, G, B, interval):
    interval = float(interval)
    setFadedRGB(R, G, B, 0, 0, 0, interval/2)
    setFadedRGB(0, 0, 0, R, G, B, interval/2)

def getLoad():
    """
    Returns a float which is the AVG load of the CPU in the last minute
    Return ranges from 0 to 1 as we're already dividing by the number of CPU cores
    """
    load  = float(subprocess.Popen(["uptime"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8').split(', ')[3].split(': ')[1])
    cores = float(subprocess.Popen(["nproc","--all"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'))
    return load / cores

def getLoadRGB(load):
    """
    Returns a certain color combination for the given load
    """

    # Safety fist
    if load < 0.0:
        load = 0.0
    elif load > 1.0:
        load = 1.0

    # Red is bad and green is good... the usual
    R = 100 * load
    G = 100 - R
    B = 0

    return (R, G, B)

# Setup
GPIO.setmode(GPIO.BOARD)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

RED = GPIO.PWM(red, Freq) # Pin, Frequency
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

# Start with the LEDs turned off
R = 0
G = 0
B = 0

RED.start(R)
GREEN.start(G)
BLUE.start(B)

# Do stuff while we're not interrupted by CTRL+C
try:
    while 1:
        (newR, newG, newB) = getLoadRGB(getLoad())
        if R < 60:
            if newR < 25:
                newR = int(newR/4)
                newG = int(newG/4)
                newB = int(newB/4)
            elif newR < 50:
                newR = int(newR/2)
                newG = int(newG/2)
                newB = int(newB/2)
            setFadedRGB(R, G, B, newR, newG, newB, checkInterval)
        elif newR >= 80:
            pulseRGB(newR, newG, newB, checkInterval)
        elif newR >= 60:
            pulseRGB(newR, newG, newB, checkInterval*2)
        R = newR
        G = newG
        B = newB

except KeyboardInterrupt:
    pass

# Turn LEDs off
setRGB(0, 0, 0)

# Stop all the PWM objects
RED.stop()
GREEN.stop()
BLUE.stop()

# Tidy up and remaining connections.
GPIO.cleanup()
