import lcd_bus
from micropython import const
import machine
from time import sleep
import jd9853
import axs5106
import lvgl as lv
from i2c import I2C

lv.init()

# display settings
_WIDTH = 172
_HEIGHT = 320
_BL = 23
_RST = 22
_DC = 15

_MOSI = 2 #SDA
_MISO = 5
_SCK = 1  # SCL
_HOST = 1  # SPI2

_LCD_CS = 14
_LCD_FREQ = 2000000
_TOUCH_FREQ = 2000000
_TOUCH_CS = 21

_OFFSET_X = 34
_OFFSET_Y = 0


print('s1');
spi_bus = machine.SPI.Bus(
    host=_HOST,
    mosi=_MOSI,
    #miso=_MISO,
    sck=_SCK
)

print('s2');
display_bus = lcd_bus.SPIBus(
    spi_bus=spi_bus,
    freq=_LCD_FREQ,
    dc=_DC,
    cs=_LCD_CS,
)

print('s3');
display = jd9853.JD9853(
    data_bus=display_bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    backlight_pin=_BL,
    reset_pin=_RST,
    reset_state=jd9853.STATE_LOW,
    backlight_on_state=jd9853.STATE_HIGH,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order=jd9853.BYTE_ORDER_BGR,
    rgb565_byte_swap=True,
    offset_x=_OFFSET_X,
    offset_y=_OFFSET_Y
)

print('s4');

display.set_power(True)
display.init()
display.set_color_inversion(True)
# display.set_rotation(lv.DISPLAY_ROTATION._90)
display.set_backlight(100)

i2c_bus = I2C.Bus(host=0, sda=18, scl=19)
touch_i2c = I2C.Device(i2c_bus, axs5106.I2C_ADDR, axs5106.BITS)
indev = axs5106.AXS5106(touch_i2c,
                        debug=True,
                        startup_rotation=lv.DISPLAY_ROTATION._90,
                        reset_pin=20
                        )
# if not indev.is_calibrated:
#indev.calibrate()




# scrn = lv.screen_active()

import utime as time
time_passed = 1000

while True:
    start_time = time.ticks_ms()
    time.sleep_ms(1)  # sleep for 1 ms
    lv.tick_inc(time_passed)
    lv.task_handler()
    end_time = time.ticks_ms()
    time_passed = time.ticks_diff(end_time, start_time)

