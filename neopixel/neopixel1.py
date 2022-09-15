import board
import neopixel

from time import sleep

PIXEL_COUNT = 30
PIN = board.D18

pixels = neopixel.NeoPixel(PIN, PIXEL_COUNT)

# RGB colors (Red, Green, Blue)
pixels[0] = (255, 0, 0)
pixels.show()

sleep(5)

pixels.fill((0, 0, 255))
pixels.show()
