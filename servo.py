import machine
import time

servo = machine.PWM(machine.Pin(1), freq=50)
print(1)

# back and forth
while True:
    for i in range(115, 40, -1):
        servo.duty(i)
        time.sleep(0.01)
    for i in range(40, 115):
        servo.duty(i)
        time.sleep(0.01)
