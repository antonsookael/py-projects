import tkinter as tk
import random

clicks = 0.0
cps = 0

clickers = 0
clicker_price = 15
clicker_mult = 1
clicker_upgrade_price = 500
clicker_upgraded = False

grandmas = 0
grandma_price = 100
grandma_mult = 1
grandma_upgrade_price = 1000
grandma_upgraded = False

farms = 0
farm_price = 1100
farm_mult = 1
farm_upgrade_price = 5000
farm_upgraded = False

mines = 0
mine_price = 12000
mine_mult = 1
mine_upgrade_price = 20000
mine_upgraded = False

#------------------------------------------------------------------------


color = [
    "#8b4513", "#a0522d", "#cd853f", "#d2691e", "#c68642",
    "#e8a87c", "#deb887", "#d4a574", "#c4955a", "#b8860b",
    "#daa520", "#f4a460", "#e5c49e", "#c8a882", "#bf9060",
    "#a67c52", "#8b6914", "#c19a6b", "#e8c99a", "#d4863a",
    "#f5deb3", "#ffe4b5", "#ffdead", "#f0bc74", "#e8a020",
]


def format_num(n):
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.2f}B"
    elif n >= 1_000_000:
        return f"{n / 1_000_000:.2f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.2f}K"
    else:
        return str(round(n))


#------------------------------------------------------------------------


def debug_cookie():
    global clicks
    clicks += 1000000


def cookie_clicks():
    global clicks
    clicks += 1
    cookie.config(text=f"🍪 {format_num(clicks)}", bg=random.choice(color))


# Buyables------------------------------------------------------------------------


def buy_clicker():
    global clicks, clickers, clicker_price
    if clicks >= clicker_price:
        clicks -= clicker_price
        clickers += 1
        clicker_price *= 1.15
        cookie.config(text=f"🍪 {format_num(clicks)}")
        clicker_btn.config(text=f"Clicker - {format_num(clicker_price)} 🍪 ({clickers})")
    else:
        clicker_btn.config(text=f"Need {format_num(clicker_price)} cookies! 🍪")
        root.after(1500, lambda: clicker_btn.config(text=f"Clicker - {format_num(clicker_price)} 🍪 ({clickers})"))


def buy_grandmas():
    global clicks, grandma_price, grandmas
    if clicks >= grandma_price and clickers >= 1:
        clicks -= grandma_price
        grandmas += 1
        grandma_price *= 1.15
        cookie.config(text=f"🍪 {format_num(clicks)}")
        grandma_btn.config(text=f"Grandma - {format_num(grandma_price)} 🍪 ({grandmas})")
    elif clicks < grandma_price:
        grandma_btn.config(text=f"Need {format_num(grandma_price)} cookies! 🍪")
        root.after(1500, lambda: grandma_btn.config(text=f"Grandma - {format_num(grandma_price)} 🍪 ({grandmas})"))
    elif clickers < 1:
        grandma_btn.config(text="Need atleast 1 clicker!")
        root.after(1500, lambda: grandma_btn.config(text=f"Grandma - {format_num(grandma_price)} 🍪 ({grandmas})"))


def buy_farm():
    global clicks, farm_price, farms
    if clicks >= farm_price and grandmas >= 1:
        clicks -= farm_price
        farms += 1
        farm_price *= 1.15
        cookie.config(text=f"🍪 {format_num(clicks)}")
        farm_btn.config(text=f"Farm - {format_num(farm_price)} 🍪 ({farms})")
    elif clicks < farm_price:
        farm_btn.config(text=f"Need {format_num(farm_price)} cookies! 🍪")
        root.after(1500, lambda: farm_btn.config(text=f"Farm - {format_num(farm_price)} 🍪 ({farms})"))
    elif grandmas < 1:
        farm_btn.config(text="Need atleast 1 Grandma!")
        root.after(1500, lambda: farm_btn.config(text=f"Farm - {format_num(farm_price)} 🍪 ({farms})"))


def buy_mine():
    global clicks, mine_price, mines
    if clicks >= mine_price and farms >= 1:
        clicks -= mine_price
        mines += 1
        mine_price *= 1.15
        cookie.config(text=f"🍪 {format_num(clicks)}")
        mine_btn.config(text=f"Mine - {format_num(mine_price)} 🍪 ({mines})")
    elif clicks < mine_price:
        mine_btn.config(text=f"Need {format_num(mine_price)} cookies! 🍪")
        root.after(1500, lambda: mine_btn.config(text=f"Mine - {format_num(mine_price)} 🍪 ({mines})"))
    elif farms < 1:
        mine_btn.config(text="Need atleast 1 Farm!")
        root.after(1500, lambda: mine_btn.config(text=f"Mine - {format_num(mine_price)} 🍪 ({mines})"))


# Upgrades------------------------------------------------------------------------


def upgrade_clicker():
    global clicks, clicker_mult, clicker_upgraded
    if clicker_upgraded:
        betclickers1_btn.config(text="✅ 2x👆")
        return
    if clickers >= 1 and clicks >= clicker_upgrade_price:
        clicks -= clicker_upgrade_price
        clicker_mult = 2
        clicker_upgraded = True
        cookie.config(text=f"🍪 {format_num(clicks)}")
        betclickers1_btn.config(text="✅ 2x👆")
    elif clickers < 1:
        betclickers1_btn.config(text="Need 1 clicker!")
        root.after(1500, lambda: betclickers1_btn.config(text="2x👆"))
    else:
        betclickers1_btn.config(text=f"Need {clicker_upgrade_price} 🍪!")
        root.after(1500, lambda: betclickers1_btn.config(text="2x👆"))


def upgrade_grandma():
    global clicks, grandma_mult, grandma_upgraded
    if grandma_upgraded:
        betgrandma1_btn.config(text="✅ 2x👵")
        return
    if grandmas >= 1 and clicks >= grandma_upgrade_price:
        clicks -= grandma_upgrade_price
        grandma_mult = 2
        grandma_upgraded = True
        cookie.config(text=f"🍪 {format_num(clicks)}")
        betgrandma1_btn.config(text="✅ 2x👵")
    elif grandmas < 1:
        betgrandma1_btn.config(text="Need 1 grandma!")
        root.after(1500, lambda: betgrandma1_btn.config(text="2x👵"))
    else:
        betgrandma1_btn.config(text=f"Need {grandma_upgrade_price} 🍪!")
        root.after(1500, lambda: betgrandma1_btn.config(text="2x👵"))


def upgrade_farm():
    global clicks, farm_mult, farm_upgraded
    if farm_upgraded:
        betfarm1_btn.config(text="✅ 2x🌾")
        return
    if farms >= 1 and clicks >= farm_upgrade_price:
        clicks -= farm_upgrade_price
        farm_mult = 2
        farm_upgraded = True
        cookie.config(text=f"🍪 {format_num(clicks)}")
        betfarm1_btn.config(text="✅ 2x🌾")
    elif farms < 1:
        betfarm1_btn.config(text="Need 1 Farm!")
        root.after(1500, lambda: betfarm1_btn.config(text="2x🌾"))
    else:
        betfarm1_btn.config(text=f"Need {farm_upgrade_price} 🍪!")
        root.after(1500, lambda: betfarm1_btn.config(text="2x🌾"))


def upgrade_mine():
    global clicks, mine_mult, mine_upgraded
    if mine_upgraded:
        betmine1_btn.config(text="✅ 2x⛏️")
        return
    if mines >= 1 and clicks >= mine_upgrade_price:
        clicks -= mine_upgrade_price
        mine_mult = 2
        mine_upgraded = True
        cookie.config(text=f"🍪 {format_num(clicks)}")
        betmine1_btn.config(text="✅ 2x⛏️")
    elif mines < 1:
        betmine1_btn.config(text="Need 1 Mine!")
        root.after(1500, lambda: betmine1_btn.config(text="2x⛏️"))
    else:
        betmine1_btn.config(text=f"Need {format_num(mine_upgrade_price)} 🍪!")
        root.after(1500, lambda: betmine1_btn.config(text="2x⛏️ 20000 🍪"))


# Loop------------------------------------------------------------------------


def auto_click():
    global clicks, clicker_mult, grandma_mult, clickers, grandmas, farms, farm_mult, mines, mine_mult
    clicks += clickers * 0.1 / 1000 * clicker_mult
    clicks += grandmas * 1 / 1000 * grandma_mult
    clicks += farms * 8 / 1000 * farm_mult
    clicks += mines * 47 / 1000 * mine_mult

    cps = (clickers * 0.1 * clicker_mult + grandmas * 1 * grandma_mult
           + farms * 8 * farm_mult + mines * 47 * mine_mult)

    cookie.config(text=f"🍪 {format_num(clicks)}")
    cps_count.config(text=f"CPS: {format_num(cps)}")
    root.after(1, auto_click)


# Window------------------------------------------------------------------------

root = tk.Tk()
root.title("Cookie Clicker")
root.configure(bg="#cd853f")
root.after(1, auto_click)
root.columnconfigure(1, minsize=100)

cookie = tk.Button(root, text=f"🍪 {format_num(clicks)}", width=15, height=3,
                   command=cookie_clicks, font=("Arial", 16))
cookie.grid(row=0, column=0, pady=20, padx=20)

cps_count = tk.Label(root, text=f"CPS: {cps}", bg="#cd853f", font=("Arial", 12))
cps_count.grid(row=0, column=1)

# Buyable buttons------------------------------------------------------------------------

clicker_btn = tk.Button(root, text=f"Clicker {format_num(clicker_price)} 🍪 ({clickers})",
                         width=22, command=buy_clicker, bg="#8b4513", fg="white", relief="flat")
clicker_btn.grid(row=1, column=0, pady=4)

grandma_btn = tk.Button(root, text=f"Grandma {format_num(grandma_price)} 🍪 ({grandmas})",
                         width=22, command=buy_grandmas, bg="#8b4513", fg="white", relief="flat")
grandma_btn.grid(row=2, column=0, pady=4)

farm_btn = tk.Button(root, text=f"Farm {format_num(farm_price)} 🍪 ({farms})",
                      width=22, command=buy_farm, bg="#8b4513", fg="white", relief="flat")
farm_btn.grid(row=3, column=0, pady=4)

mine_btn = tk.Button(root, text=f"Mine {format_num(mine_price)} 🍪 ({mines})",
                      width=22, command=buy_mine, bg="#8b4513", fg="white", relief="flat")
mine_btn.grid(row=4, column=0, pady=4)

# Upgrade buttons------------------------------------------------------------------------

betclickers1_btn = tk.Button(root, text=f"2x👆 {format_num(clicker_upgrade_price)} 🍪",
                              bg="#8b4513", fg="white", width=13, command=upgrade_clicker)
betclickers1_btn.grid(row=1, column=1)

betgrandma1_btn = tk.Button(root, text=f"2x👵 {format_num(grandma_upgrade_price)} 🍪",
                             bg="#8b4513", fg="white", width=13, command=upgrade_grandma)
betgrandma1_btn.grid(row=2, column=1)

betfarm1_btn = tk.Button(root, text=f"2x🌾 {format_num(farm_upgrade_price)} 🍪",
                          bg="#8b4513", fg="white", width=13, command=upgrade_farm)
betfarm1_btn.grid(row=3, column=1)

betmine1_btn = tk.Button(root, text=f"2x⛏️ {format_num(mine_upgrade_price)} 🍪",
                          bg="#8b4513", fg="white", width=13, command=upgrade_mine)
betmine1_btn.grid(row=4, column=1)

# Debug------------------------------------------------------------------------

debugc = tk.Button(root, text="1M", width=5, command=debug_cookie)
debugc.grid(row=0, column=2)

root.mainloop()