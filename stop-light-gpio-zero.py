from gpiozero import LED
from time import sleep

red = LED(22)
amber = LED(27)
green = LED(17)

## Worksheet: Controlling a Traffic LIght Sequence with GPIO Zero

## Control the LEDs

## Step 2: Test red blink...
red.blink()

## Step 4: 3 lights, blinking at different speeds...
#red.blink(1, 1)
#amber.blink(2, 2)
#green.blink(3, 3)

## Step 6: Blink more quickly...
#red.blink(1, .25)
#amber.blink(2, .25)
#green.blink(3, .25)

## Traffic light sequence

## Step 1: Single run of turning on the leds...
#red.on()
#sleep(1)
#amber.on()
#sleep(1)
#green.on()
#sleep(1)

## Step 2: Try turning the lights on and off in sequence...
#red.on()
#sleep(1)
#amber.on()
#sleep(1)
#green.on()
#sleep(1)
#red.off()
#sleep(1)
#amber.off()
#sleep(1)
#green.off()

## Step 3: Try repeating this by putting the code inside a while loop...
#while True:
#    red.on()
#    sleep(1)
#    amber.on()
#    sleep(1)
#    green.on()
#    sleep(1)
#    red.off()
#    sleep(1)
#    amber.off()
#    sleep(1)
#    green.off()

## Step 4: Control the lights in a proper sequence
#while True:
#    green.on()
#    sleep(1)
#    green.off()
#    amber.on()
#    sleep(1)
#    amber.off()
#    red.on()
#    sleep(1)
#    amber.on()
#    sleep(1)
#    red.off()
#    amber.off()
