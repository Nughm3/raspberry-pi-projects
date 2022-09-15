import board
import neopixel

from time import sleep

PIXEL_COUNT = 30
PIN = board.D18

pixels = neopixel.NeoPixel(PIN, PIXEL_COUNT)

for i in range(len(pixels)):
    pixels[i] = (0, 255, 0)
    pixels.show()
    sleep(0.1)

pixels.fill((0, 0, 0))
pixels.show()