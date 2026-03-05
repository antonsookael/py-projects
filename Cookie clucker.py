import tkinter as tk
import random

clicks = 0.0
cps = 0
better_clicks1 = 2 # 2x upgrade

clickers = 0
clicker_price = 15
better_clickers1 = 2 # 2x upgrade

grandmas = 0
grandma_price = 100
better_grandma1 = 2 # 2x upgrade

color = [
    "#8b4513",  # saddle brown
    "#a0522d",  # sienna
    "#cd853f",  # peru
    "#d2691e",  # chocolate
    "#c68642",  # cookie brown
    "#e8a87c",  # light cookie
    "#deb887",  # burlywood
    "#d4a574",  # warm tan
    "#c4955a",  # golden brown
    "#b8860b",  # dark goldenrod
    "#daa520",  # goldenrod
    "#f4a460",  # sandy brown
    "#e5c49e",  # pale cookie
    "#c8a882",  # biscuit
    "#bf9060",  # medium brown
    "#a67c52",  # walnut
    "#8b6914",  # dark cookie
    "#c19a6b",  # caramel
    "#e8c99a",  # vanilla cream
    "#d4863a",  # burnt orange brown
    "#f5deb3",  # wheat
    "#ffe4b5",  # moccasin (white chocolate)
    "#ffdead",  # navajo white
    "#f0bc74",  # honey
    "#e8a020",  # golden
]

def cookie_clicks():
    global clicks
    clicks += 1
    cookie.config(text=f"🍪 {round(clicks)}", bg=random.choice(color))
    

def buy_clicker():
    global clicks, clickers, clicker_price

    if clicks >= clicker_price:

        clicks -= clicker_price
        clickers += 1
        clicker_price *= 1.15

        cookie.config(text=f"🍪 {round(clicks)}")
        clicker_btn.config(text=f"Buy Clicker - {round(clicker_price)} 🍪({clickers})")  

    else:
        clicker_btn.config(text=f"Need {round(clicker_price)} cookies! 🍪")
        root.after(1500, lambda: clicker_btn.config(text=f"Buy Clicker - {round(clicker_price)} 🍪 ({clickers})"))

    
def buy_grandmas():


    global clicks, grandma_price, grandmas

    if clicks >= grandma_price and clickers >= 1:
        clicks -= grandma_price
        grandmas += 1
        grandma_price *= 1.15

        cookie.config(text=f"🍪 {round(clicks)}")
        grandma_btn.config(text=f"Buy Grandma - {round(grandma_price)} 🍪({grandmas})")

    elif clicks < grandma_price:
        grandma_btn.config(text=f"Need {round(grandma_price)} cookies! 🍪")
        root.after(1500, lambda: grandma_btn.config(text=f"Buy Grandma - {round(grandma_price)} 🍪 ({grandmas})"))
    elif clickers < 1:
        grandma_btn.config(text="Need atleast 1 clicker!")
        root.after(1500, lambda: grandma_btn.config(text=f"Buy Grandma - {round(grandma_price)} 🍪 ({grandmas})"))


def better_grandma1():
    global clicks, grandmas
    if grandmas >= 10:

        betgrandma1_btn.config()

def auto_click():
    global clicks
    clicks += clickers * 0.1
    clicks += grandmas * 2

    cps = clickers * 0.1 + grandmas * 2  # calculate current cps

    cookie.config(text=f"🍪 {round(clicks)}")
    cps_count.config(text=f"CPS: {round(cps, 1)}")  # update the label every second
    root.after(1000, auto_click)

    





root = tk.Tk()


root.title("Cookie Clicker")
root.configure(bg="#cd853f")

root.after(1000, auto_click)

root.columnconfigure(1, minsize=100)

cookie = tk.Button(root, text=f"🍪 {round(clicks)}", width=15, height=3, command=cookie_clicks, font=("Arial", 16))
cookie.grid(row=0, column=0, pady=20, padx=25)

cps_count = tk.Label(root, text=f"CPS: {cps}", bg="#cd853f", font=("Arial", 12))
cps_count.grid(row=0, column=1)

clicker_btn = tk.Button(root, text=f"Buy Clicker {round(clicker_price)} 🍪 ({clickers})", width=20, command=buy_clicker, bg="#8b4513", fg="white", relief="flat")
clicker_btn.grid(row=1, column=0, pady=4)

grandma_btn = tk.Button(root, text=f"Buy Grandma {round(grandma_price)} 🍪 ({grandmas})", width=20, command=buy_grandmas, bg="#8b4513", fg="white", relief="flat")
grandma_btn.grid(row=2, column=0, pady=4)

betclickers1_btn = tk.Button(root, text="2x👆", bg="#8b4513", fg="white", width= 5)
betclickers1_btn.grid(row=1, column=1)

betgrandma1_btn = tk.Button(root, text="2x👵", bg="#8b4513", fg="white", width=5)
betgrandma1_btn.grid(row=2, column=1)


root.mainloop()