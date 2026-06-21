from machine import Pin, PWM
import time

class Servo:
    def __init__(self, pin_num, min_us=500, max_us=2500, freq=50):
        """
        Initialize the Servo.
        min_us and max_us define the pulse width range for 0 to 180 degrees.
        Standard SG90 servos usually work well with 500us to 2500us.
        """
        self.pwm = PWM(Pin(pin_num), freq=freq)
        self.min_ns = min_us * 1000
        self.max_ns = max_us * 1000

    def write_angle(self, angle):
        """Moves the servo to a specific angle (0-180 degrees)."""
        # Constrain the angle between 0 and 180
        angle = max(0, min(180, angle))
        
        # Calculate the corresponding pulse width in nanoseconds
        pulse_width_ns = self.min_ns + int((self.max_ns - self.min_ns) * (angle / 180.0))
        
        # Send the PWM signal
        self.pwm.duty_ns(pulse_width_ns)
        
    def off(self):
        """Turns off the PWM signal, stopping the servo from holding its position."""
        self.pwm.deinit()

# ==========================================
# Example Usage
# ==========================================

my_servo = Servo(pin_num=0)

try:
	for i in range(0, 100, 1):
		my_servo.write_angle(0)
		time.sleep(1)
		my_servo.write_angle(180)
		time.sleep(1)

	for i in range(0, 0, 1):
		print(f"Moving to {i} degrees")
		my_servo.write_angle(i)
		time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping...")
finally:
    print("end")
    # my_servo.off() # Clean up the PWM signal
    
while True:
    time.sleep(1)