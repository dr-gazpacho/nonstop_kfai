# nonstop_kfai
One station. One volume.

## This is only possible with the great work of literally everyone else
This uses some Circuit Python and some community libraries
- https://circuitpython.org/libraries
Bunch of real ones also made a library to support the radio
- https://learn.adafruit.com/scoutmakes-fm-radio-board-stemma-i2c/circuitpython-code

## Starting up from scrach with a brand new Pico?
I'll be real with you, I'm gonna be super vauge here and just give you the broad strokes of what you need to do. How you do it is entirely up to you.
1. Load the circuit python firmware onto your pico (you can get this from Adafruit directly or use the version I have in the repo)
1. Load up the radio library by dragging this `tinkeringtech_rda5807m` from the repo the Pico's `lib` directory, or get one from the community bundle
1. Flash code.py onto the pico
1. Hook it up.
1. Plug it in.
1. Crank it.
