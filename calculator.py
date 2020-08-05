# Basic Calculator in Python
# using tkinter
# By: Dimitris Gkountelos

from tkinter import *

# main window of the application
root = Tk()
root.title("Calculator")

input_box = Entry(root, width=23, borderwidth=3)
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# function for each operation
def division(input_str):
    comb_numbers = input_str.split("/")

    num1 = float(comb_numbers[0])
    num2 = float(comb_numbers[1])
    clear()
    num = num1 / num2
    num = round(num, 6)
    input_box.insert(0, str(num))
    return

def multiplication(input_str):
    comb_numbers = input_str.split("x")
    num1 = float(comb_numbers[0])
    num2 = float(comb_numbers[1])
    clear()
    num = num1 * num2
    num = round(num, 6)
    input_box.insert(0, str(num))
    return 

def add(input_str):
    comb_numbers = input_str.split("+")
    num1 = float(comb_numbers[0])
    num2 = float(comb_numbers[1])
    clear()
    num = num1 + num2
    num = round(num, 6)
    input_box.insert(0, str(num))
    return

def subtraction(input_str):
    comb_numbers = input_str.split("-")
    num1 = float(comb_numbers[0])
    num2 = float(comb_numbers[1])
    clear()
    num = num1 - num2
    num = round(num, 6)
    input_box.insert(0, str(num))
    return

# function that clears
# the input box
def clear():
    input_box.delete(0, END)

# function that gets each
# button click and calls 
# the needed operation
def click(number):
    if number == "C":
        clear()
        return

    current = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, current + str(number))
    
    if number == "=":
        if "+" in current:
            add(current)
        elif "-" in current:
            subtraction(current)
        elif "x" in current:
            multiplication(current)
        elif "/" in current:
            division(current)

# function to converts %
def percent():
    current = input_box.get()
    number = float(current)
    number = number/100
    input_box.delete(0, END)
    input_box.insert(0, str(float(number)))
    return

# shape, placement and text for
# each number button
button_7 = Button(root, text="7", padx=15, pady=15, command=lambda: click(7), bg="#aaddaa", fg="black")
button_7.grid(row=2,column=0)

button_8 = Button(root, text="8", padx=15, pady=15, command=lambda: click(8), bg="#aaddaa", fg="black")
button_8.grid(row=2,column=1)

button_9 = Button(root, text="9", padx=15, pady=15, command=lambda: click(9), bg="#aaddaa", fg="black")
button_9.grid(row=2,column=2)

button_4 = Button(root, text="4", padx=15, pady=15, command=lambda: click(4), bg="#aaddaa", fg="black")
button_4.grid(row=3,column=0)

button_5 = Button(root, text="5", padx=15, pady=15, command=lambda: click(5), bg="#aaddaa", fg="black")
button_5.grid(row=3,column=1)

button_6 = Button(root, text="6", padx=15, pady=15, command=lambda: click(6), bg="#aaddaa", fg="black")
button_6.grid(row=3,column=2)

button_1 = Button(root, text="1", padx=15, pady=15, command=lambda: click(1), bg="#aaddaa", fg="black")
button_1.grid(row=4,column=0)

button_2 = Button(root, text="2", padx=15, pady=15, command=lambda: click(2), bg="#aaddaa", fg="black")
button_2.grid(row=4,column=1)

button_3 = Button(root, text="3", padx=15, pady=15, command=lambda: click(3), bg="#aaddaa", fg="black")
button_3.grid(row=4,column=2)

button_0 = Button(root, text="0", padx=38, pady=15, command=lambda: click(0), bg="#aaddaa", fg="black")
button_0.grid(row=5, column=0, columnspan=2)


# shape, placement and text
# for each operation button
button_dot = Button(root, text=".", padx=15, pady=15, command=lambda: click("."), bg="#3f3f3f", fg="white")
button_dot.grid(row=5, column=2)

button_equal = Button(root, text="=", padx=15, pady=38, command=lambda: click("="), bg="#3f3f3f", fg="white")
button_equal.grid(row=4, column=3, rowspan=2)

button_plus = Button(root, text="+", padx=15, pady=15, command=lambda: click("+"), bg="#3f3f3f", fg="white")
button_plus.grid(row=3, column=3)

button_minus = Button(root, text="-", padx=15, pady=15, command=lambda: click("-"), bg="#3f3f3f", fg="white")
button_minus.grid(row=2, column=3)

button_c = Button(root, text="C", padx=15, pady=15, command=clear, bg="#3f3f3f", fg="white")
button_c.grid(row=1, column=0)

button_percent = Button(root, text="%", padx=15, pady=15, command=percent, bg="#3f3f3f", fg="white")
button_percent.grid(row=1, column=1)

button_division = Button(root, text="/", padx=15, pady=15, command=lambda: click("/"), bg="#3f3f3f", fg="white")
button_division.grid(row=1, column=2)

button_multiplication = Button(root, text="x", padx=15, pady=15, command=lambda: click("x"), bg="#3f3f3f", fg="white")
button_multiplication.grid(row=1, column=3)

root.mainloop()