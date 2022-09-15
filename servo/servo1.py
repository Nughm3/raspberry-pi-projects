import RPi.GPIO as GPIO
from time import sleep

SERVO_PIN = 12
FREQ = 50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, FREQ)
servo.start(0)

try:
    while True:
        for dc in range(0, 101, 5):
            servo.ChangeDutyCycle(dc)
            sleep(0.1)
        sleep(3)
        for dc in range(100, -1, -5):
            servo.ChangeDutyCycle(dc)
            sleep(0.1)
        sleep(3)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
