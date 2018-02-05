# Raspberry Pi System Load LED
A script for your Raspberry Pi that will show the system load through an external RGB LED.

--------------------------------------------------------------------------------

### How it works

The color range goes from green to red depending on the system load as it follows:
 - under 25%: quarter brightness starting with pure green
 - under 50%: half brightness yellow nuances
 - over 50%: full brightness
 - over 60%: slowly pulsating orange light
 - over 80%: fast pulsating red light

--------------------------------------------------------------------------------

### Running the script

Download *RPI-SystemLoad-LED.py*, put it wherever you want and then run it with:

    # python3 RPI-SystemLoad-LED.py

You might want to set it to run at startup :)

--------------------------------------------------------------------------------

### Pictures

![raspberry pi 3 model b - closed](https://github.com/blchinezu/rpi-system-load-led/blob/master/IMG_20180131_214042.jpg?raw=true)

![raspberry pi 3 model b - opened](https://github.com/blchinezu/rpi-system-load-led/blob/master/IMG_20180131_214209.jpg?raw=true)

--------------------------------------------------------------------------------

### Video

[![Youtube Video](https://i.ytimg.com/vi/9k0FLhkswZg/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAo_DoDWDPisInGwgvv96DGJtch2g)](https://www.youtube.com/watch?v=9k0FLhkswZg)

--------------------------------------------------------------------------------

### Requirements

 - Raspberry Pi
 - Raspbian OS (easiest as it already has every software thing you may need)
 - SMD 5050 LED board (you can obviously build it yourself too but you'll probably get a bulky thing)
 - Edit the script so it'll point to the right LED GPIO pins

--------------------------------------------------------------------------------

### My config

 - Raspberry Pi 3 Model B
 - Raspbian OS
 - [THIS](https://www.aliexpress.com/item/3-Colour-RGB-SMD-LED-Module-5050-full-color-Pwm-tri-color-LED-For-Arduino-MCU/32818529969.html) SMD 5050 LED board
 - RGB pins: 15, 13, 11
 - Ground pin: 9

--------------------------------------------------------------------------------

### Raspberry Pi 3 Model B pinout

![Raspberry Pi 3 Model B pinout image](https://raw.githubusercontent.com/blchinezu/RPI-SystemLoad-LED/master/rpi-pinout.png)
