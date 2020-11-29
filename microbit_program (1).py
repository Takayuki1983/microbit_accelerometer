from microbit import *
import music

tune = ["C4:4", "G4:8"]


while True:
    X_reading = accelerometer.get_x()
    Y_reading = accelerometer.get_y()
    Z_reading = accelerometer.get_z()

    if accelerometer.was_gesture('up') and not accelerometer.was_gesture("left") and not accelerometer.was_gesture("right"):
        display.clear()
        display.show("R")
        music.play(tune)
        sleep(3000)

    else:
        display.show("-")