from customtkinter import *
from functools import partial
import re

root = CTk()

root.geometry("400x520")
set_appearance_mode("Dark")

CORNER_RADIUS = 10
WIDTH = 80
LABEL_WIDTH = 380
HEIGHT = 80
FONT_40 = ("arial", 40)
FONT_30 = ("arial", 30)
GREY = "grey"
DARKGREY = "darkgrey"
ORANGE = "orange"
BLACK = "black"
DARKORANGE = "darkorange"
GREEN = "green"


def writeOnLabel(Text):
    global label

    label.configure(text=Text)

outer_operation = ""
inner_operation = ""
previous_result = ""
def addChar(elem):
    global outer_operation
    global inner_operation
    global label

    elem_check = elem in ("+", "-", "x", "÷", ".")
    inner_op_check = [len(inner_operation) == 0, len(inner_operation) != 0]
    inner_check = inner_op_check[1] and inner_operation[-1] in ("+", "-", "*", "/", ".")

    if (inner_check and elem_check) or inner_op_check[0] and elem_check:
        pass
    else:
        outer_operation = outer_operation + str(elem)

        if elem == "÷":
            inner_operation = inner_operation + "/"
        elif elem == "x":
            inner_operation = inner_operation + "*"
        else:
            inner_operation = inner_operation + str(elem)

    writeOnLabel(outer_operation)

def reset():
    global outer_operation
    global inner_operation
    global previous_result

    outer_operation = ""
    inner_operation = ""
    previous_result = ""
    writeOnLabel("")

def removeLastChar():
    global outer_operation
    global inner_operation

    outer_operation = outer_operation[:-1]
    inner_operation = inner_operation[:-1]

    writeOnLabel(outer_operation)

def calculate():
    global outer_operation
    global inner_operation
    global previous_result

    if "/0" in inner_operation:
        writeOnLabel("Error: Cannot divide by zero")
    elif len(inner_operation) == 0:
        writeOnLabel("Error: Cannot calculate an empty operation")
    else:
        outer_operation = str(eval(inner_operation))
        previous_result = outer_operation
        inner_operation = previous_result
        writeOnLabel(outer_operation)

    

def addPrevoiusResult():
    global outer_operation
    global inner_operation
    global previous_result

    outer_operation = outer_operation + previous_result
    inner_operation = inner_operation + previous_result

    writeOnLabel(outer_operation)

def calculatePercentage():
    global outer_operation
    global inner_operation
    global previous_result

    if inner_operation.isnumeric():
        outer_operation = str(int(inner_operation) / 100)
        previous_result = outer_operation
        inner_operation = previous_result
        
        writeOnLabel(outer_operation)
    else:
        writeOnLabel("Error: Cannot calculate the percentage")


label = CTkLabel(root, text="", height=HEIGHT, bg_color=GREEN, width=LABEL_WIDTH)
label.grid(columnspan=6, column=0, row=0, padx=10)

CTkButton(root, text="C", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=GREY, hover_color=DARKGREY, command=reset).grid(row=1, column=1, padx=8, pady=5)
CTkButton(root, text="%", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=GREY, hover_color=DARKGREY, command=calculatePercentage).grid(row=1, column=2)
CTkButton(root, text="←", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=GREY, hover_color=DARKGREY, command=removeLastChar).grid(row=1, column=3, padx=8, pady=5)
CTkButton(root, text="÷", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=GREY, hover_color=DARKGREY, command=partial(addChar, "÷")).grid(row=1, column=4)

CTkButton(root, text="7", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 7)).grid(row=2, column=1)
CTkButton(root, text="8", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 8)).grid(row=2, column=2)
CTkButton(root, text="9", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 9)).grid(row=2, column=3)
CTkButton(root, text="X", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=GREY, hover_color=DARKGREY, command=partial(addChar, "x")).grid(row=2, column=4)

CTkButton(root, text="4", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 4)).grid(row=3, column=1, padx=5, pady=5)
CTkButton(root, text="5", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 5)).grid(row=3, column=2)
CTkButton(root, text="6", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 6)).grid(row=3, column=3)
CTkButton(root, text="-", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=GREY, hover_color=GREY, command=partial(addChar, "-")).grid(row=3, column=4)

CTkButton(root, text="1", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 1)).grid(row=4, column=1)
CTkButton(root, text="2", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 2)).grid(row=4, column=2)
CTkButton(root, text="3", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 3)).grid(row=4, column=3)
CTkButton(root, text="+", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=GREY, hover_color=DARKGREY, command=partial(addChar, "+")).grid(row=4, column=4)

CTkButton(root, text="Ans", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_30, fg_color=BLACK, hover_color=GREY, command=addPrevoiusResult).grid(row=5, column=1, padx=5, pady=5)
CTkButton(root, text="0", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, 0)).grid(row=5, column=2)
CTkButton(root, text=",", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=BLACK, hover_color=GREY, command=partial(addChar, ".")).grid(row=5, column=3)
CTkButton(root, text="=", corner_radius=CORNER_RADIUS, width=WIDTH, height=HEIGHT, font=FONT_40, fg_color=DARKORANGE, hover_color=ORANGE, command=calculate).grid(row=5, column=4)


root.mainloop()