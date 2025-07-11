import lcd_bus
from micropython import const
import machine
from time import sleep
import jd9853
import lvgl as lv

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

scrn = lv.screen_active()
scrn.set_style_bg_color(lv.color_hex(0xff0000), 0)

label = lv.label(scrn)
label.set_text('HELLO')
label.set_style_text_color(lv.color_hex(0xffffff), 0)
label.align(lv.ALIGN.CENTER, 0, 30)

# Draw a rectangle
rect1 = lv.obj(scrn)
rect1.set_size(10, 10)
rect1.set_style_bg_color(lv.color_hex(0x00aa00), 0)
rect1.set_style_border_color(lv.color_hex(0xffffff), 0)
rect1.set_style_border_width(1, 0)
rect1.set_style_radius(0, 0)
rect1.align(lv.ALIGN.TOP_LEFT, 0, 0)

rect2 = lv.obj(scrn)
rect2.set_size(10, 10)
rect2.set_style_bg_color(lv.color_hex(0xaa0000), 0)
rect2.set_style_border_color(lv.color_hex(0xffffff), 0)
rect2.set_style_border_width(1, 0)
rect2.set_style_radius(0, 0)
rect2.align(lv.ALIGN.TOP_RIGHT, 0, 0)

rect3 = lv.obj(scrn)
rect3.set_size(10, 10)
rect3.set_style_bg_color(lv.color_hex(0xaa00aa), 0)
rect3.set_style_border_color(lv.color_hex(0xffffff), 0)
rect3.set_style_border_width(1, 0)
rect3.set_style_radius(0, 0)
rect3.align(lv.ALIGN.BOTTOM_RIGHT, 0, 0)

rect4 = lv.obj(scrn)
rect4.set_size(10, 10)
rect4.set_style_bg_color(lv.color_hex(0x0000aa), 0)
rect4.set_style_border_color(lv.color_hex(0xffffff), 0)
rect4.set_style_border_width(1, 0)
rect4.set_style_radius(0, 0)
rect4.align(lv.ALIGN.BOTTOM_LEFT, 0, 0)

# Draw a circle
circle = lv.obj(scrn)
circle.set_size(50, 50)
circle.set_style_bg_color(lv.color_hex(0x0000ff), 0)
circle.set_style_border_color(lv.color_hex(0xff00ff), 0)
circle.set_style_border_width(3, lv.STATE.DEFAULT)
circle.set_style_radius(25, 0)  # Make it circular (radius = half of width/height)
circle.align(lv.ALIGN.CENTER, 0, -10)

print('end')

import utime as time
time_passed = 1000

while True:
    start_time = time.ticks_ms()
    time.sleep_ms(1)  # sleep for 1 ms
    lv.tick_inc(time_passed)
    lv.task_handler()
    end_time = time.ticks_ms()
    time_passed = time.ticks_diff(end_time, start_time)

