"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio

led1 = digitalio.DigitalInOut(board.LED)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP14)
led2.direction = digitalio.Direction.OUTPUT

led1.value = 1
led2.value = 0

print("Starting...")
while True:
    led1.value = not led1.value
    led2.value = not led2.value
    time.sleep(0.25)
