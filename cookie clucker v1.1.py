import tkinter as tk
import random


# variobles--------------------------

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

#stats var------------

overall_cookies = 0
overall_spent = 0
time_spent = 0

stats_open_b = False

shop_open_b = False

ads_open_b = False

# bg="#8b4513", fg="white"
#


#------------------------------------------------------------------------


color = [
    "#8b4513", "#a0522d", "#cd853f", "#d2691e", "#c68642",
    "#e8a87c", "#deb887", "#d4a574", "#c4955a", "#b8860b",
    "#daa520", "#f4a460", "#e5c49e", "#c8a882", "#bf9060",
    "#a67c52", "#8b6914", "#c19a6b", "#e8c99a", "#d4863a",
    "#f5deb3", "#ffe4b5", "#ffdead", "#f0bc74", "#e8a020",
]


def format_num(n):
    def fmt(val, suffix):
        rounded = round(val, 2)
        if rounded == int(rounded):
            return f"{int(rounded)}{suffix}"
        return f"{rounded}{suffix}"

    if n >= 1_000_000_000:
        return fmt(n / 1_000_000_000, "B")
    elif n >= 1_000_000:
        return fmt(n / 1_000_000, "M")
    elif n >= 1_000:
        return fmt(n / 1_000, "K")
    else:
        return str(round(n))


#------------------------------------------------------------------------


def debug_cookie():
    global clicks, overall_cookies
    clicks += 1000000
    overall_cookies += 1000000


def cookie_clicks():
    global clicks, overall_cookies
    clicks += 1
    cookie.config(text=f"🍪 {format_num(clicks)}", bg=random.choice(color))
    overall_cookies += 1

#side btn------------------------------------------------------------------------------------------

def open_advert():
    global advert1, advert_btn, ads_open_b, stats_open_b, shop_open_b, advert2


    advert_btn.config(text="Close", command=close_advert)

    advert1 = tk.Label(root, text="tung tung tung sahurr", bg="#8b4513", fg="white")
    advert1.grid(row=1, column=0)

    advert2 = tk.Label(root, text="tung tung tung sahurr", bg="#8b4513", fg="white")
    advert2.grid(row=2, column=0)

    ads_open_b = True

    if shop_open_b:
        close_shops()
    if stats_open_b:
        close_stats()
    

def close_advert():
    global advert_btn, advert1, ads_open_b, advert2

    advert_btn.config(text="Ads", command=open_advert)

    advert1.grid_remove()
    advert2.grid_remove()


    

def open_stats():
    global ov_cookies, ov_spent, time_spent_lb, stats_open_b, shop_open_b, ads_open_b

    if shop_open_b:
        close_shops()
    if ads_open_b:
        close_advert()

    ov_cookies = tk.Label(root, text=f"Overall cookies made: {format_num(overall_cookies)}", bg="#8b4513", fg="white")
    ov_cookies.grid(row=1, column=0)

    ov_spent = tk.Label(root, text=f"Overall cookies spent: {format_num(overall_spent)}", bg="#8b4513", fg="white")
    ov_spent.grid(row=2, column=0)

    time_spent_lb = tk.Label(root, text=f"Time spent: {time_spent}", bg="#8b4513", fg="white")
    time_spent_lb.grid(row=3, column=0)

    stats_btn.config(text="Close", command=close_stats)
    stats_open_b = True
    

def close_stats():
    global ov_cookies, ov_spent, time_spent_lb, stats_open_b

    ov_cookies.grid_remove()
    ov_spent.grid_remove()
    time_spent_lb.grid_remove()

    stats_btn.config(text="Stats", command=open_stats)
    stats_open_b = False



def open_shops():
    global clicker_btn, grandma_btn, farm_btn, mine_btn
    global betclickers1_btn, betgrandma1_btn, betfarm1_btn, betmine1_btn, shop_open_b, stats_open_b, ads_open_b

    shops_btn.config(text="Close", command=close_shops)

    # --------------
    clicker_btn = tk.Button(root, text=f"Clicker {format_num(clicker_price)} 🍪 ({clickers})", width=22, command=buy_clicker, bg="#8b4513", fg="white", relief="flat")
    clicker_btn.grid(row=1, column=0, pady=4)

    grandma_btn = tk.Button(root, text=f"Grandma {format_num(grandma_price)} 🍪 ({grandmas})", width=22, command=buy_grandmas, bg="#8b4513", fg="white", relief="flat")
    grandma_btn.grid(row=2, column=0, pady=4)

    farm_btn = tk.Button(root, text=f"Farm {format_num(farm_price)} 🍪 ({farms})", width=22, command=buy_farm, bg="#8b4513", fg="white", relief="flat")
    farm_btn.grid(row=3, column=0, pady=4)

    mine_btn = tk.Button(root, text=f"Mine {format_num(mine_price)} 🍪 ({mines})", width=22, command=buy_mine, bg="#8b4513", fg="white", relief="flat")
    mine_btn.grid(row=4, column=0, pady=4)

    # -----------------
    betclickers1_btn = tk.Button(root, text="✅ 2x👆" if clicker_upgraded else f"2x👆 {format_num(clicker_upgrade_price)} 🍪", bg="#8b4513", fg="white", width=13, command=upgrade_clicker)
    betclickers1_btn.grid(row=1, column=1)

    betgrandma1_btn = tk.Button(root, text="✅ 2x👵" if grandma_upgraded else f"2x👵 {format_num(grandma_upgrade_price)} 🍪", bg="#8b4513", fg="white", width=13, command=upgrade_grandma)
    betgrandma1_btn.grid(row=2, column=1)

    betfarm1_btn = tk.Button(root, text="✅ 2x🌾" if farm_upgraded else f"2x🌾 {format_num(farm_upgrade_price)} 🍪", bg="#8b4513", fg="white", width=13, command=upgrade_farm)
    betfarm1_btn.grid(row=3, column=1)

    betmine1_btn = tk.Button(root, text="✅ 2x⛏️" if mine_upgraded else f"2x⛏️ {format_num(mine_upgrade_price)} 🍪", bg="#8b4513", fg="white", width=13, command=upgrade_mine)
    betmine1_btn.grid(row=4, column=1)

    shop_open_b = True
    if stats_open_b:
        close_stats()
    if ads_open_b:
        close_advert()

    shops_btn.config(text="Close", command=close_shops)


def close_shops():
    global clicker_btn, grandma_btn, farm_btn, mine_btn
    global betclickers1_btn, betgrandma1_btn, betfarm1_btn, betmine1_btn, shop_open_b
    shops_btn.config(text="Shops", command=open_shops)

    # Buyable buttons------------------------------------------------------------------------

    clicker_btn.grid_remove()
    grandma_btn.grid_remove()
    farm_btn.grid_remove()
    mine_btn.grid_remove()

    # Upgrade buttons------------------------------------------------------------------------

    betclickers1_btn.grid_remove()
    betgrandma1_btn.grid_remove()
    betfarm1_btn.grid_remove()
    betmine1_btn.grid_remove()

    shops_open_b = False

# Buyables------------------------------------------------------------------------

def buy_clicker():
    global clicks, clickers, clicker_price, overall_spent, overall_spent
    if clicks >= clicker_price:
        clicks -= clicker_price
        clickers += 1
        clicker_price *= 1.15
        cookie.config(text=f"🍪 {format_num(clicks)}")
        clicker_btn.config(text=f"Clicker - {format_num(clicker_price)} 🍪 ({clickers})")
    else:
        clicker_btn.config(text=f"Need {format_num(clicker_price)} cookies! 🍪")
        root.after(1500, lambda: clicker_btn.config(text=f"Clicker - {format_num(clicker_price)} 🍪 ({clickers})"))
    overall_spent += clicker_price


def buy_grandmas():
    global clicks, grandma_price, grandmas, overall_spent
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
    overall_spent += grandma_price


def buy_farm():
    global clicks, farm_price, farms, overall_spent
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
    overall_spent += farm_price

def buy_mine():
    global clicks, mine_price, mines, overall_spent
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
    overall_spent += mine_price

# Upgrades------------------------------------------------------------------------


def upgrade_clicker():
    global clicks, clicker_mult, clicker_upgraded, overall_spent
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
    overall_spent += clicker_upgrade_price

def upgrade_grandma():
    global clicks, grandma_mult, grandma_upgraded, overall_spent
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
    overall_spent += grandma_upgrade_price

def upgrade_farm():
    global clicks, farm_mult, farm_upgraded, overall_spent
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
    overall_spent += farm_upgrade_price

def upgrade_mine():
    global clicks, mine_mult, mine_upgraded, overall_spent
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
    overall_spent += mine_upgrade_price

# Loop------------------------------------------------------------------------


def auto_click():
    global clicks, clicker_mult, grandma_mult, clickers, grandmas, farms, farm_mult, mines, mine_mult, overall_cookies, time_spent

    clicks += clickers * 0.1 / 100 * clicker_mult
    clicks += grandmas * 1 / 100 * grandma_mult
    clicks += farms * 8 / 100 * farm_mult
    clicks += mines * 47 / 100 * mine_mult

    cps = (clickers * 0.1 * clicker_mult + grandmas * 1 * grandma_mult
           + farms * 8 * farm_mult + mines * 47 * mine_mult)

    overall_cookies += cps / 100
    time_spent += 10

    if stats_open_b:
        ov_cookies.config(text=f"Overall cookies made: {format_num(overall_cookies)}")
        ov_spent.config(text=f"Overall spent: {format_num(overall_spent)}")
        time_spent_lb.config(text=f"Time spent: {time_spent // 1000}s")

    cookie.config(text=f"🍪 {format_num(clicks)}")
    cps_count.config(text=f"CPS: {cps}")
    root.after(10, auto_click)



# Window------------------------------------------------------------------------

root = tk.Tk()
root.title("Cookie Clicker")
root.configure(bg="#cd853f")
root.after(10, auto_click)
root.columnconfigure(1, minsize=100)

cookie = tk.Button(root, text=f"🍪 {format_num(clicks)}", width=15, height=3, command=cookie_clicks, font=("Arial", 16))
cookie.grid(row=0, column=0, pady=20, padx=20)

cps_count = tk.Label(root, text=f"CPS: {cps}", bg="#cd853f", font=("Arial", 10))
cps_count.grid(row=0, column=1)


# side buttons --------------------------------------------------------------------

shops_btn = tk.Button(root, text="Shops", bg="black", fg="white", width=5, command=open_shops)
shops_btn.grid(row=1, column=2, pady=4)

stats_btn = tk.Button(root, text="Stats", bg="black", fg="white", width=5, command=open_stats)
stats_btn.grid(row=2, column=2, pady=4)

advert_btn = tk.Button(root, text="Ads", bg="black", fg="white", width=5, command=open_advert)
advert_btn.grid(row=3, column=2, pady=4)

# Debug------------------------------------------------------------------------

debugc = tk.Button(root, text="1M", width=5, command=debug_cookie)
debugc.grid(row=0, column=2)

root.mainloop()