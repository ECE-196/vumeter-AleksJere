#print("Hello World!")

import time

import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT
start_time = time.time()
max = 0
prev_volume = 0
# main loop
while True:

    #for i in range(len(leds)):
    #    leds[i].value = False
    volume = microphone.value
    elapsed_time = time.time() - start_time
    #print(volume)
    

    if elapsed_time >= 15:
            print("15 seconds have passed!")
            start_time = time.time()
            max = 0

    if (max< volume or max == 0):
        max = volume

    yes = volume//max
    timing = 0.25
    #print('this is yes' + str(yes))
    
    #leds[0].value = not leds[0].value
    #print(type(leds[0].value))
    
    #leds[1].value = not leds[0].value
    #leds[8].value = True
    
    if int(volume//(max/10)) < prev_volume:
        value = int(volume//(max/10)) - prev_volume
        for i in range(prev_volume,int(volume//(max/10)),-1):
            time.sleep(timing*.1)
            leds[i].value = False
    else:
        print(int(volume//(max/10)))
        for i in range(int(volume//(max/10))):
            leds[i].value = True

    prev_volume = int(volume//(max/10))
    sleep(timing)
 

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter? 