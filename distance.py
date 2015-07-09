#!/usr/bin/python

import time
import RPi.GPIO as GPIO

# Configuration des GPIO
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)
GPIO.setup(ECHO, GPIO.IN)

# ----------------------------------------------------------------------------


def main():
    try:
        while True:
            time.sleep(0.1)
            print("[--- DEBUT DE LA MESURE ---]")

            GPIO.output(TRIG, 1)
            time.sleep(0.00001)
            GPIO.output(TRIG, 0)

            while GPIO.input(ECHO) == 0:
                pass
            start = time.time()

            while GPIO.input(ECHO) == 1:
                pass
            stop = time.time()

            temps = stop - start
            print("Temps : " + str(temps))
            distance = (stop - start) * 17000
            print("Distance : " + str(distance))

    except KeyboardInterrupt:
        print("[--- EXIT (except KeyboardInterrupt) ---]")
        GPIO.cleanup()

    finally:
        print("[--- EXIT WITH CLEANUP ---]")
        GPIO.cleanup()

# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()