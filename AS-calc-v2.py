import tkinter as tk
import math
import random

current_text = ""
open_brackets = 0
memory = 0

is_trigo = False
is_memory = False

def set_operation(op):
    global current_text
    if current_text == "":
        return
    symbols = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}
    current_text += symbols[op]
    current_text_lb.config(text=current_text)

def equals():
    global current_text
    if current_text == "":
        return
    try:
        result = eval(current_text)
        result = int(result) if result == int(result) else round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

def square():
    global current_text
    if current_text == "":
        return
    try:
        result = float(current_text) ** 2
        result = int(result) if result == int(result) else round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

def square_root():
    global current_text
    if current_text == "":
        return
    try:
        result = math.sqrt(float(current_text))
        result = int(result) if result == int(result) else round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

def add_parenthesis():
    global current_text, open_brackets
    if open_brackets == 0 or current_text[-1] == "(":
        current_text += "("
        open_brackets += 1
    else:
        current_text += ")"
        open_brackets -= 1
    current_text_lb.config(text=current_text)
    open_p_btn.config(text="(" if open_brackets == 0 else ")")

def add_number(n):
    global current_text
    current_text += str(n)
    current_text_lb.config(text=current_text)

def add_dot():
    global current_text
    if "." not in current_text.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]:
        current_text += "."
        current_text_lb.config(text=current_text)

def clear_all():
    global current_text, open_brackets
    current_text = ""
    open_brackets = 0
    current_text_lb.config(text="")
    open_p_btn.config(text="(")

def backspace():
    global current_text, open_brackets
    if current_text:
        if current_text[-1] == "(":
            open_brackets -= 1
        elif current_text[-1] == ")":
            open_brackets += 1
        current_text = current_text[:-1]
        current_text_lb.config(text=current_text)
        open_p_btn.config(text="(" if open_brackets == 0 else ")")

def pi_val():
    global current_text
    if current_text == "":
        current_text = str(math.pi)

    else:
        current_text = str(float(current_text) * math.pi)
    current_text_lb.config(text=current_text)

def flip_sign():
    global current_text
    if current_text == "":
        return
    if current_text.startswith("-"):
        current_text = current_text[1:]
    else:
        current_text = "-" + current_text
    current_text_lb.config(text=current_text)

def random_to1():
    global current_text
    current_text = str(round(random.uniform(0, 1), 3))
    current_text_lb.config(text=current_text)



#------------------------------------------------TRIGONOMETRY--------------------------------------------------------

def open_trigo():
    global sin_val_btn, cos_val_btn, tan_val_btn, open_atrig_btn
    is_memory = True
    opentrig_btn.config(text="Close", command=close_trigo)

    sin_val_btn = tk.Button(calc, text="sin", width=5, height=2, command=sin_val, bg="#cdcdcd")
    sin_val_btn.grid(row=2, column=0, sticky="e")

    cos_val_btn = tk.Button(calc, text="cos", width=5, height=2, command=cos_val, bg="#cdcdcd")
    cos_val_btn.grid(row=3, column=0, sticky="e")

    tan_val_btn = tk.Button(calc, text="tan", width=5, height=2, command=tan_val, bg="#cdcdcd")
    tan_val_btn.grid(row=4, column=0, sticky="e")

    open_atrig_btn = tk.Button(calc, text="aTrig", width=5, height=2, command=open_atrig, bg="#cdcdcd")
    open_atrig_btn.grid(row=5, column=0, sticky="e")

    if is_memory:
        close_memory()

def close_trigo():

    opentrig_btn.config(text="Trig", command=open_trigo)
    is_trigo = False
    sin_val_btn.grid_remove()
    cos_val_btn.grid_remove()
    tan_val_btn.grid_remove()
    open_atrig_btn.grid_remove()


def sin_val():
    global current_text
    if current_text == "":
        return
    try:
        result = math.sin(math.radians(float(current_text)))
        result = round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

def cos_val():
    global current_text
    if current_text == "":
        return
    try:
        result = math.cos(math.radians(float(current_text)))
        result = round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

def tan_val():
    global current_text
    if current_text == "":
        return
    try:
        result = math.tan(math.radians(float(current_text)))
        result = round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

#--------------ATRIGO---------------------------------

def open_atrig():
    global asin_val_btn, atan_val_btn, acos_val_btn

    asin_val_btn = tk.Button(calc, text="sin⁻¹", width=5, height=2, command=asin_val, bg="#cdcdcd")
    asin_val_btn.grid(row=2, column=0, sticky="e")

    acos_val_btn = tk.Button(calc, text="cos⁻¹", width=5, height=2, command=acos_val, bg="#cdcdcd")
    acos_val_btn.grid(row=3, column=0, sticky="e")

    atan_val_btn = tk.Button(calc, text="tan⁻¹", width=5, height=2, command=atan_val, bg="#cdcdcd")
    atan_val_btn.grid(row=4, column=0, sticky="e")

    sin_val_btn.grid_remove()
    cos_val_btn.grid_remove()
    tan_val_btn.grid_remove()
    open_atrig_btn.config(text="Close", command=close_atrig)

def close_atrig():

    asin_val_btn.grid_remove()
    atan_val_btn.grid_remove()
    acos_val_btn.grid_remove()
    open_atrig_btn.config(text="aTrig", command=open_atrig)

    sin_val_btn.grid(row=2, column=0, sticky="e")
    cos_val_btn.grid(row=3, column=0, sticky="e")
    tan_val_btn.grid(row=4, column=0, sticky="e")


def asin_val():
    global current_text
    if current_text == "":
        return
    try:
        result = math.degrees(math.asin(float(current_text)))
        result = round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

def acos_val():
    global current_text
    if current_text == "":
        return
    try:
        result = math.degrees(math.acos(float(current_text)))
        result = round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

def atan_val():
    global current_text
    if current_text == "":
        return
    try:
        result = math.degrees(math.atan(float(current_text)))
        result = round(result, 8)
        current_text = str(result)
        current_text_lb.config(text=current_text)
    except:
        current_text_lb.config(text="Error")
        current_text = ""

#---------------------------------------------MEMORY----------------------------------------------------------------

def open_memory():
    global mm_add_btn, mm_sub_btn, mm_rec_btn, mm_clear_btn
    is_memory = True

    open_mm_btn.config(text="Close", command=close_memory, bg="#cdcdcd")
    open_mm_btn.grid(row=1, column=0, sticky="e")

    mm_add_btn = tk.Button(calc, text="M+", width=5, height=2, command=mm_add, bg="#cdcdcd")
    mm_add_btn.grid(row=2, column=0, sticky="e")
    mm_sub_btn = tk.Button(calc, text="M-", width=5, height=2, command=mm_sub, bg="#cdcdcd")
    mm_sub_btn.grid(row=3, column=0, sticky="e")
    mm_rec_btn = tk.Button(calc, text="MR", width=5, height=2, command=mm_rec, bg="#cdcdcd")
    mm_rec_btn.grid(row=4, column=0, sticky="e")
    mm_clear_btn = tk.Button(calc, text="MC", width=5, height=2, command=mm_clear, bg="#cdcdcd")
    mm_clear_btn.grid(row=5, column=0, sticky="e")

    if is_trigo:
        close_trigo()

def close_memory():
    is_memory = False
    open_mm_btn.config(text="M", command=open_memory, bg="#cdcdcd")
    open_mm_btn.grid(row=2, column=0, sticky="e")

    mm_add_btn.grid_remove()
    mm_sub_btn.grid_remove()
    mm_rec_btn.grid_remove()
    mm_clear_btn.grid_remove()

def mm_add():
    global memory, current_text
    if current_text == "":
        return
    memory += float(current_text)

def mm_sub():
    global memory, current_text
    if current_text == "":
        return
    memory -= float(current_text)

def mm_rec():
    global memory, current_text
    result = int(memory) if memory == int(memory) else round(memory, 8)
    current_text = str(result)
    current_text_lb.config(text=current_text)

def mm_clear():
    global memory
    memory = 0


#----------------------------------------------WINDOWW-----------------------------------------------------------------

calc = tk.Tk()
calc.title("Anton Calc v1.3")

name = tk.Label(calc, text="Anton calc:", height=3)
name.grid(row=0, column=0)

current_text_lb = tk.Label(calc, text="", width=16, font=("Arial", 15), bg="#1f1f1f", fg="white", anchor="w")
current_text_lb.grid(row=0, column=1, columnspan=4)

# Operation buttons------------------------------------------------------------

add_btn = tk.Button(calc, text="+", width=5, height=2, command=lambda: set_operation("add"), bg="#cdcdcd")
add_btn.grid(row=4, column=4)

subtract_btn = tk.Button(calc, text="-", width=5, height=2, command=lambda: set_operation("subtract"), bg="#cdcdcd")
subtract_btn.grid(row=3, column=4)

divide_btn = tk.Button(calc, text="/", width=5, height=2, command=lambda: set_operation("divide"), bg="#cdcdcd")
divide_btn.grid(row=2, column=3)

multiply_btn = tk.Button(calc, text="*", width=5, height=2, command=lambda: set_operation("multiply"), bg="#cdcdcd")
multiply_btn.grid(row=2, column=4)

square_btn = tk.Button(calc, text="x²", width=5, height=2, command=square, bg="#cdcdcd")
square_btn.grid(row=2, column=2)

sqrt_btn = tk.Button(calc, text="√", width=5, height=2, command=square_root, bg="#cdcdcd")
sqrt_btn.grid(row=2, column=1)

equals_btn = tk.Button(calc, text="=", width=5, height=5, command=equals, bg="#4caf50", fg="white")
equals_btn.grid(row=5, column=4, rowspan=2)

# Utility buttons--------------------------------------------------------------

clear_all_btn = tk.Button(calc, text="AC", width=5, height=2, command=clear_all, bg="#ff5555", fg="white")
clear_all_btn.grid(row=1, column=4)

backspace_btn = tk.Button(calc, text="⌫", width=5, height=2, command=backspace, bg="#cdcdcd")
backspace_btn.grid(row=1, column=3)

open_p_btn = tk.Button(calc, text="(", width=5, height=2, command=add_parenthesis, bg="#cdcdcd")
open_p_btn.grid(row=1, column=1, sticky="e")

pi_val_btn = tk.Button(calc, text="π", width=5, height=2, command=pi_val, bg="#cdcdcd")
pi_val_btn.grid(row=1, column=2)

opentrig_btn = tk.Button(calc, text="Trig", width=5, height=2, command=open_trigo, bg="#cdcdcd")
opentrig_btn.grid(row=1, column=0, sticky="e")

open_mm_btn = tk.Button(calc, text="M", width=5, height=2, command=open_memory, bg="#cdcdcd")
open_mm_btn.grid(row=2, column=0, sticky="e")

flip_sign_btn = tk.Button(calc, text="-/+", width=5, height=2, command=flip_sign, bg="#cdcdcd")
flip_sign_btn.grid(row=3, column=0, sticky="e")

random_to1_btn = tk.Button(calc, text="Ran", width=5, height=2, command=random_to1, bg="#cdcdcd")
random_to1_btn.grid(row=4, column=0, sticky="e")


# -----------------------------------------NUMBERS BUTTONS---------------------------------------------------------------

number_1 = tk.Button(calc, text="1", width=5, height=2, command=lambda: add_number(1), bg="#cdcdcd")
number_1.grid(row=3, column=1)
number_2 = tk.Button(calc, text="2", width=5, height=2, command=lambda: add_number(2), bg="#cdcdcd")
number_2.grid(row=3, column=2)
number_3 = tk.Button(calc, text="3", width=5, height=2, command=lambda: add_number(3), bg="#cdcdcd")
number_3.grid(row=3, column=3)
number_4 = tk.Button(calc, text="4", width=5, height=2, command=lambda: add_number(4), bg="#cdcdcd")
number_4.grid(row=4, column=1)
number_5 = tk.Button(calc, text="5", width=5, height=2, command=lambda: add_number(5), bg="#cdcdcd")
number_5.grid(row=4, column=2)
number_6 = tk.Button(calc, text="6", width=5, height=2, command=lambda: add_number(6), bg="#cdcdcd")
number_6.grid(row=4, column=3)
number_7 = tk.Button(calc, text="7", width=5, height=2, command=lambda: add_number(7), bg="#cdcdcd")
number_7.grid(row=5, column=1)
number_8 = tk.Button(calc, text="8", width=5, height=2, command=lambda: add_number(8), bg="#cdcdcd")
number_8.grid(row=5, column=2)
number_9 = tk.Button(calc, text="9", width=5, height=2, command=lambda: add_number(9), bg="#cdcdcd")
number_9.grid(row=5, column=3)

number_0 = tk.Button(calc, text="0", width=5, height=2, command=lambda: add_number(0), bg="#cdcdcd")
number_0.grid(row=6, column=2)

dot_btn = tk.Button(calc, text=".", width=5, height=2, command=add_dot, bg="#cdcdcd")
dot_btn.grid(row=6, column=3)

calc.mainloop()