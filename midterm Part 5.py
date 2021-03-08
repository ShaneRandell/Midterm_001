# Part 5 for the midterm exam

from guizero import App, PushButton, TextBox, Text, Box,Drawing  # importing all the libraries
from threading import Thread
import serial
import time

ser = serial.Serial('COM3', 9600)  # connecting my python to my ardiuno using the Com
ser.flush()  # this flushes the serial monitor
time.sleep(3)  # This gives the arduino time to respond


# Defining all my function i will be calling throughout the program

def Exit_function():  # this funticon controlls my exit button on my app
    app.destroy()


# The next 4 function all do the same thing for the pin buttons in my Gui

def PinButton():
    ser.write(str('Pin8').encode('utf-8'))  # These function write to the serial monitor arduino
    ser.write(str("\n").encode('utf-8'))  # Each one writes a specific message depending on the pin
    ser.flush()


def PinButton1():
    ser.write(str('Pin9').encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    ser.flush()


def PinButton2():
    ser.write(str('Pin10').encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    ser.flush()


def PinButton3():
    ser.write(str('Pin11').encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    ser.flush()


# This function controls all the other functionality of the Gui

def AnalogRead_thread():
    while True:  # Will always run allowing the thread to be constantly running

        ser.flush()
        Monitor_Reading = ser.readline().decode('utf-8')  # Reading the monitor for the values from the arduino
        String_split = Monitor_Reading.split(',')  # Spliting the string and storing it in a variable

        Pot0 = float(String_split[0])  # All of these functions will contain a specific value
        Pot1 = float(String_split[1])  # Each value will be passed to a Gui function
        Pot2 = float(String_split[2])  # Then printed to the Gui in a specific loccation
        Pot3 = float(String_split[3])

        Button1 = float(String_split[4])
        Button2 = float(String_split[5])
        Button3 = float(String_split[6])
        Button4 = float(String_split[7])

        Analog_text1.value = Pot0  # This is where that actual value is printed to the GUI
        Analog_text2.value = Pot1
        Analog_text3.value = Pot2
        Analog_text4.value = Pot3

        # All of these if/else conditions will take the input from the buttons and change the Oval color in the Gui

        if Button1 != 1:
            oval1.oval(5, 25, 25, 45, color="red", outline=True, outline_color="black")
        else:
            oval1.oval(5, 25, 25, 45, color="green", outline=True, outline_color="black")

        if Button2 != 1:
            oval2.oval(5, 25, 25, 45, color="red", outline=True, outline_color="black")
        else:
            oval2.oval(5, 25, 25, 45, color="green", outline=True, outline_color="black")

        if Button3 != 1:
            oval3.oval(5, 25, 25, 45, color="red", outline=True, outline_color="black")
        else:
            oval3.oval(5, 25, 25, 45, color="green", outline=True, outline_color="black")

        if Button4 != 1:
            oval4.oval(5, 25, 25, 45, color="red", outline=True, outline_color="black")
        else:
            oval4.oval(5, 25, 25, 45, color="green", outline=True, outline_color="black")


# The main part of the code

app = App(title="GUI MIDTERM", height=300, width=500, layout="grid")  # Setting up my app size and grid
text = Text(app, text="IO Data acquisition system GUI", grid=[0, 0])  # Setting a textbox up
Exit_Button = PushButton(app, command=Exit_function, text="EXIT", grid=[3, 3])  # creating my exit buton

box1 = Box(app, layout="grid", grid=[0, 1]) # defining my first box and its location
pin_button_title = Text(box1, text="Output", grid=[0, 0]) # adding a title to the box
pin_button1 = PushButton(box1, command=PinButton, text="pin8", grid=[0, 1])  # building all my buttons inside of the box
pin_button2 = PushButton(box1, command=PinButton1, text="pin9", grid=[0, 2])
pin_button3 = PushButton(box1, command=PinButton2, text="pin10", grid=[2, 1])
pin_button4 = PushButton(box1, command=PinButton3, text="pin11", grid=[2, 2])

box2 = Box(app, layout="grid", grid=[1, 1])  # defining my second box and location
Analog_title = Text(box2, text="Analog Input", grid=[0, 0])     # writing all the text required for the box
Analog_title1 = Text(box2, text="A0", grid=[0, 1])              # Making text to label inputs
Analog_title2 = Text(box2, text="A1", grid=[0, 2])
Analog_title3 = Text(box2, text="A2", grid=[0, 3])
Analog_title4 = Text(box2, text="A3", grid=[0, 4])
Analog_text1 = TextBox(box2, grid=[1, 1])                       # making text boxes for every input
Analog_text2 = TextBox(box2, grid=[1, 2])
Analog_text3 = TextBox(box2, grid=[1, 3])
Analog_text4 = TextBox(box2, grid=[1, 4])

Digital_title = Text(app, text="Digital Input", grid=[0, 2], align="left")     # labeling my 3rd box
box3 = Box(app, layout="grid", grid=[0, 3])                                    # creating the box and location
oval1 = Drawing(box3, height=50, width=50, grid=[0, 1])                        # defining my location of my drawing
oval2 = Drawing(box3, height=50, width=50, grid=[1, 1])
oval3 = Drawing(box3, height=50, width=50, grid=[2, 1])
oval4 = Drawing(box3, height=50, width=50, grid=[3, 1])
Digital_title1 = Text(box3, text="2", grid=[0, 2])                             # labeling each of my drawings
Digital_title2 = Text(box3, text="3", grid=[1, 2])
Digital_title3 = Text(box3, text="4", grid=[2, 2])
Digital_title4 = Text(box3, text="5", grid=[3, 2])

thread = Thread(target=AnalogRead_thread)               # declaring my thread and which function will run
thread.start()                                          # starting my thread functions
app.display()                                           # running my app
