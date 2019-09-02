import os
import time
from gpiozero import Button

button = Button(8)
print("Press Button:")

button.when_pressed = os.system('python3 main.py')

if (button.when_pressed):
    print("Photo being uploaded")
    
b=print("Button released")
