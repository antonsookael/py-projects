import tkinter as tk
import numpy as np
import os
from PIL import Image, ImageTk
import random

keys = set()
mouse_down = False

mouse_x = 0
mouse_y = 0

target_x = random.randint(50, 550)
target_y = random.randint(50, 550)
target_alive = True

rect_x = 300
rect_y = 300

target_1_hp = 5
can_fire = True
hits = 0

def mouse_press(e):
    global mouse_down
    mouse_down = True

def mouse_release(e):
    global mouse_down
    mouse_down = False

def keypress(e):
    keys.add(e.keysym)

def keyrelease(e):
    keys.discard(e.keysym)

def game_loop():
    global rect_x, rect_y

    if "a" in keys and rect_x > 0:
        rect_x -= 5
    if "d" in keys and rect_x < 530:
        rect_x += 5
    if "w" in keys and rect_y > 0:
        rect_y -= 5
    if "s" in keys and rect_y < 530:
        rect_y += 5

    canvas.coords(rect, rect_x, rect_y)
    canvas.coords(crosshair_rect, mouse_x - 5, mouse_y - 5, mouse_x + 5, mouse_y + 5)
    root.after(16, game_loop)


def track_mouse(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y


def fire_line():
    global hits, target_1_hp, can_fire, target_alive
    if not can_fire:
        return
    can_fire = False
    root.after(150, lambda: globals().update(can_fire=True))

    rect_midx = rect_x + 35
    rect_midy = rect_y + 35

    line = canvas.create_line(rect_midx, rect_midy, mouse_x, mouse_y, fill="red", width=2)

    overlapping = canvas.find_overlapping(target_x, target_y, target_x + 50, target_y + 50)
    if line in overlapping and target_alive:
        target_1_hp -= 1
        hits += 1
        print("hit!", hits)
        if target_1_hp == 0:
            target_alive = False
            canvas.delete(target)
            canvas.delete(line)
            root.after(3000, respawn_target)

    root.after(15, lambda: canvas.delete(line))


def respawn_target():
    global target, target_1_hp, target_x, target_y, target_alive
    target_alive = True

    target_x = random.randint(50, 550)
    target_y = random.randint(50, 550)
    target = canvas.create_rectangle(target_x, target_y, target_x + 50, target_y + 50, fill="green")
    target_1_hp = 5


def fire_line_loop():
    if mouse_down:
        fire_line()

    root.after(200, fire_line_loop)

#region root

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600, bg="yellow")
canvas.pack()

root.bind("<KeyPress>", keypress)
root.bind("<KeyRelease>", keyrelease)
canvas.bind("<Motion>", track_mouse)
root.bind("<ButtonRelease-1>", mouse_release)
root.bind("<Button-1>", lambda e: (mouse_press(e), fire_line()))

#region img1luigi
script_dir = os.path.dirname(os.path.abspath(__file__))
img1 = Image.open(os.path.join(script_dir, "smt1stuff1.png")).convert("RGBA")
img1 = img1.resize((70, 70))

data = np.array(img1)
white = (data[:, :, 0] > 200) & (data[:, :, 1] > 200) & (data[:, :, 2] > 200)
data[white] = [255, 255, 255, 0]
img1 = Image.fromarray(data)
img1 = ImageTk.PhotoImage(img1)
#endregion

rect = canvas.create_image(rect_x, rect_y, image=img1, anchor="nw")

target = canvas.create_rectangle(target_x, target_y, target_x + 50, target_y + 50, fill="green")
crosshair_rect = canvas.create_rectangle(mouse_x - 5, mouse_y - 5, mouse_x + 5, mouse_y + 5, fill="black")


fire_line_loop()
game_loop()
root.mainloop()
#endregion
