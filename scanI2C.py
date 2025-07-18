from machine import I2C, Pin
import time

# Initialize I2C with correct pins
i2c = I2C(0, sda=Pin(18), scl=Pin(9), freq=100000)

# Optional: Set reset pin (if used, adjust GPIO based on schematic)
reset_pin = Pin(8, Pin.OUT)  # Example: replace with actual reset pin if needed
reset_pin.value(0)  # Assert reset
time.sleep(0.01)    # Hold for 10ms
reset_pin.value(1)  # Release reset
time.sleep(0.1)     # Wait for controller to initialize

# Scan I2C bus
print("Scanning I2C bus...")
devices = i2c.scan()
if devices:
    print("Devices found at addresses (decimal):", devices)
else:
    print("No I2C devices detected")

# Try probing CST816S address
try:
    i2c.writeto(0x15, b'')
    print("CST816S responded at address 0x15")
except OSError:
    print("No response from address 0x15")