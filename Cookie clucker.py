import tkinter as tk
import random

clicks = 0.0
cps = 0

clickers = 0
clicker_price = 15
clicker_mult = 1 # 2x upgrade
clicker_upgrade_price =500
clicker_upgraded = False

grandmas = 0
grandma_price = 100
grandma_mult = 1 # 2x upgrade
grandma_upgrade_price = 1000
grandma_upgraded = False

farms = 0
farm_price = 1100
farm_mult = 1
farm_upgrade_price = 5000
farm_upgraded = False




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

def debug_cookie():
    global clicks
    clicks += 1000000

def cookie_clicks():
    global clicks
    clicks += 1
    cookie.config(text=f"🍪 {round(clicks)}", bg=random.choice(color))
    

# Buyables

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


def buy_farm():
    global clicks, farm_price, farms
    
    if clicks >= farm_price and grandmas >= 1:
        clicks -= farm_price
        farms += 1
        farm_price *= 1.15

        cookie.config(text=f"🍪 {round(clicks)}")
        farm_btn.config(text=f"Buy Farms - {round(farm_price)} 🍪({farms})")

    elif clicks < farm_price:
        farm_btn.config(text=f"Need {round(farm_price)} cookies! 🍪")
        root.after(1500, lambda: farm_btn.config(text=f"Buy Farm - {round(farm_price)} 🍪 ({farms})"))

    elif grandmas < 1:
        farm_btn.config(text="Need atleast 1 Grandma!")
        root.after(1500, lambda: farm_btn.config(text=f"Buy Farm - {round(farm_price)} 🍪 ({farms})"))


# Upgardes

def upgrade_grandma():
    global clicks, grandma_mult, grandma_upgraded
    if grandma_upgraded:
        betgrandma1_btn.config(text="✅ 2x👵")
        return
    
    if grandmas >= 1 and clicks >= grandma_upgrade_price:
        clicks -= grandma_upgrade_price
        grandma_mult = 2
        grandma_upgraded = True
        cookie.config(text=f"🍪 {round(clicks)}")
        betgrandma1_btn.config(text="✅ 2x👵")

    elif grandmas < 1:
        betgrandma1_btn.config(text="Need 1 grandmas!")
        root.after(1500, lambda: betgrandma1_btn.config(text="2x👵"))

    else:
        betgrandma1_btn.config(text=f"Need {grandma_upgrade_price} 🍪!")
        root.after(1500, lambda: betgrandma1_btn.config(text="2x👵"))


def upgrade_clicker():
    global clicks, clicker_mult, clicker_upgraded
    if clicker_upgraded:
        betclickers1_btn.config(text="✅ 2x👆")
        return
    if clickers >= 1 and clicks >= clicker_upgrade_price:
        clicks -= clicker_upgrade_price
        clicker_mult = 2
        clicker_upgraded = True
        cookie.config(text=f"🍪 {round(clicks)}")
        betclickers1_btn.config(text="✅ 2x👆")
    elif clickers < 1:
        betclickers1_btn.config(text="Need 1 clickers!")
        root.after(1500, lambda: betclickers1_btn.config(text="2x👆"))
    else:
        betclickers1_btn.config(text=f"Need {clicker_upgrade_price} 🍪!")
        root.after(1500, lambda: betclickers1_btn.config(text="2x👆"))


def upgrade_farm():

    global clicks, farm_mult, farm_upgraded
    if farm_upgraded:
        betfarm1_btn.config(text="✅ 2x")
        return
    if farms >= 1 and clicks >= farm_upgrade_price:
        clicks -= farm_upgrade_price
        farm_mult = 2
        farm_upgraded = True
        cookie.config(text=f"🍪 {round(clicks)}")
        betfarm1_btn.config(text="✅ 2x")
    elif farms < 1:
        betfarm1_btn.config(text="Need 1 Farm!")
        root.after(1500, lambda: betfarm1_btn.config(text="2x"))
    else:
        betfarm1_btn.config(text=f"Need {farm_upgrade_price} 🍪!")
        root.after(1500, lambda: betfarm1_btn.config(text="2x"))  


# loop

def auto_click():
    global clicks, clicker_mult, grandma_mult, clickers, grandmas, farms, farm_mult
    clicks += clickers * 0.1 * clicker_mult
    clicks += grandmas * 1 * grandma_mult
    clicks += farms * 8 * farm_mult

    cps = clickers * 0.1 * clicker_mult + grandmas * 1 * grandma_mult + farms * 8 * farm_mult  # calculate current cps

    cookie.config(text=f"🍪 {round(clicks)}")
    cps_count.config(text=f"CPS: {round(cps, 1)}")  # update the label every second
    root.after(1000, auto_click)

    

# Window tkinter stuff

root = tk.Tk()


root.title("Cookie Clicker")
root.configure(bg="#cd853f")

root.after(1000, auto_click)

root.columnconfigure(1, minsize=100)

cookie = tk.Button(root, text=f"🍪 {round(clicks)}", width=15, height=3, command=cookie_clicks, font=("Arial", 16))
cookie.grid(row=0, column=0, pady=20, padx=20)

cps_count = tk.Label(root, text=f"CPS: {cps}", bg="#cd853f", font=("Arial", 12))
cps_count.grid(row=0, column=1)

# buyable

clicker_btn = tk.Button(root, text=f"Buy Clicker {round(clicker_price)} 🍪 ({clickers})", width=20, command=buy_clicker, bg="#8b4513", fg="white", relief="flat")
clicker_btn.grid(row=1, column=0, pady=4)

grandma_btn = tk.Button(root, text=f"Buy Grandma {round(grandma_price)} 🍪 ({grandmas})", width=20, command=buy_grandmas, bg="#8b4513", fg="white", relief="flat")
grandma_btn.grid(row=2, column=0, pady=4)

farm_btn = tk.Button(root, text=f"Buy Farm {round(farm_price)} 🍪 ({farms})", width=20, command=buy_farm, bg="#8b4513", fg="white", relief="flat")
farm_btn.grid(row=3, column=0, pady=4)

# upgrades

betclickers1_btn = tk.Button(root, text=f"2x👆 {clicker_upgrade_price} 🍪", bg="#8b4513", fg="white", width=13, command=upgrade_clicker)
betclickers1_btn.grid(row=1, column=1)

betgrandma1_btn = tk.Button(root, text=f"2x👵 {grandma_upgrade_price} 🍪", bg="#8b4513", fg="white", width=13, command=upgrade_grandma)
betgrandma1_btn.grid(row=2, column=1)

betfarm1_btn = tk.Button(root, text=f"2x {farm_upgrade_price} 🍪", bg="#8b4513", fg="white", width=13, command=upgrade_farm)
betfarm1_btn.grid(row=3, column=1)


# debug

debugc = tk.Button(root, text="1m", width=5, command=debug_cookie)
debugc.grid(row=0, column=2)

root.mainloop()