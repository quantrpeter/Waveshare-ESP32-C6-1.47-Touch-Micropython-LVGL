import machine
import time

servo = machine.PWM(machine.Pin(1), freq=50)

# back and forth
while True:
    for i in range(90, 110, 1):
        print(i)
        servo.duty(i)
        time.sleep(1)
