import tkinter as tk
import random

clicks = 0.0
cps = 0

clickers = 0
clicker_price = 15

grandmas = 0
grandma_price = 100



color = [
    # Reds
    "#ff0000", "#cc0000", "#990000", "#ff3333", "#ff6666",
    "#ff4500", "#dc143c", "#b22222", "#8b0000", "#ff1493",
    
    # Oranges
    "#ff8c00", "#ffa500", "#ff7f50", "#ff6347", "#e25822",
    
    # Yellows
    "#ffff00", "#ffd700", "#ffc200", "#ffec8b", "#f0e68c",
    
    # Greens
    "#00ff00", "#008000", "#006400", "#32cd32", "#7cfc00",
    "#00ff7f", "#3cb371", "#2e8b57", "#228b22", "#adff2f",
    
    # Blues
    "#0000ff", "#0000cd", "#00008b", "#4169e1", "#1e90ff",
    "#00bfff", "#87ceeb", "#4682b4", "#191970", "#6495ed",
    
    # Purples
    "#800080", "#8b008b", "#9400d3", "#9932cc", "#ba55d3",
    "#da70d6", "#ee82ee", "#dda0dd", "#7b68ee", "#6a0dad",
    
    # Pinks
    "#ff69b4", "#ff1493", "#db7093", "#ffb6c1", "#ffc0cb",
    
    # Cyans
    "#00ffff", "#00ced1", "#20b2aa", "#008b8b", "#40e0d0",
    
    # Browns
    "#8b4513", "#a0522d", "#cd853f", "#d2691e", "#f4a460",
    
    # Whites / Greys / Blacks
    "#ffffff", "#f5f5f5", "#dcdcdc", "#c0c0c0", "#a9a9a9",
    "#808080", "#696969", "#404040", "#1a1a1a", 
    
    # Fun extras
    "#ff00ff", "#7fffd4", "#ffe4c4", "#faebd7", "#e6e6fa",
    "#b0e0e6", "#98fb98", "#f08080", "#e0ffff", "#fafad2",
]

def cookie_clicks():
    global clicks
    clicks += 1
    cookie.config(text=f"🍪 {round(clicks)}", bg=random.choice(color))
    
def buy_clicker():
    global clicks, clickers, clicker_price, grandmas, cps_summ

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
    global clicks, grandma_price, grandmas, clickers, cps_summ

    if clicks >= grandma_price:
        clicks -= grandma_price
        grandmas += 1
        grandma_price *= 1.15

        cookie.config(text=f"🍪 {round(clicks)}")
        grandma_btn.config(text=f"Buy Grandma - {round(grandma_price)} 🍪({grandmas})")

    else:
        grandma_btn.config(text=f"Need {round(grandma_price)} cookies! 🍪")
        root.after(1500, lambda: grandma_btn.config(text=f"Buy Grandma - {round(grandma_price)} 🍪 ({grandmas})"))

    



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

cookie = tk.Button(root, text=f"🍪 {round(clicks)}", width=15, height=3, command=cookie_clicks, font=("Arial", 16))
cookie.grid(row=0, column=0, pady=20, padx=20)

cps_count = tk.Label(root, text=f"CPS: {cps}")
cps_count.grid(row=0, column=1)

clicker_btn = tk.Button(root, text=f"Buy Clicker {round(clicker_price)}🍪 ({clickers})", width=20, command=buy_clicker)
clicker_btn.grid(row=1, column=0, pady=4)

grandma_btn = tk.Button(root, text=f"Buy Grandma {round(grandma_price)}🍪 ({grandmas})", width=20, command=buy_grandmas)
grandma_btn.grid(row=2, column=0, pady=4)

root.mainloop()