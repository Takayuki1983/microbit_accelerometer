from microbit import *
import music

tune = ["C4:4", "G4:8"]


while True:
    X_reading = accelerometer.get_x()
    Y_reading = accelerometer.get_y()
    Z_reading = accelerometer.get_z()

    if accelerometer.was_gesture('up') :
        display.clear()
        
        if accelerometer.was_gesture("left"):
            display.show("#")
        elif accelerometer.was_gesture("right"):
            display.show("O")
        else:
            display.show("R")
            music.play(tune)
            sleep(1500)

    else:
        display.show("-")