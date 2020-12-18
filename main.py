# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk


price_meal = {"HotPot": 20, "Ramen": 10, "Beef stake": 30, "Fried_chicken": 15, "Zicaibaofan": 8}
price_drink = {"Coffee": 10, "Latte": 15, "Icetea": 20, "Lemon": 25, "Chocolate_smoothe": 22}

order_meal = {}
order_drink = {}

total_price = 0


def show_meal():
    btn_meal.configure(bg="yellow")
    btn_drink.configure(bg="white")
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)


def show_drink():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="yellow")
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)


def meal_add(m):
    global price_meal, order_meal, total_price
    if m not in price_meal:
        print("The menu doesn't exist")
    this_price = price_meal.get(m)
    total_price += this_price

    if m in order_meal:
        order_meal[m] = order_meal.get(m) + 1
    else:
        order_meal[m] = 1
    print_order()
    print_price()


def drink_add(m):
    global price_meal, order_meal, total_price
    if m not in price_drink:
        print("The menu doesn't exist")
    this_price = price_drink.get(m)
    total_price += this_price

    if m in order_drink:
        order_drink[m] = order_drink.get(m) + 1
    else:
        order_drink[m] = 1
    print_order()
    print_price()


def print_order():
    global order_meal, order_drink

    tmp = ""
    for i in order_meal:
        tmp = tmp + i + " X " + str(order_meal.get(i)) + "\n"
    for i in order_drink:
        tmp = tmp + i + " X " + str(order_drink.get(i)) + "\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)


def order_end():
    global total_price, order_meal, order_drink
    total_price = 0
    del order_meal
    del order_drink

    order_meal = {}
    order_drink = {}
    print_price()
    print_order()
    show_meal()


def print_price():
    global total_price
    label_price.configure(text=str(total_price)+" $")


window = tk.Tk()
window.title("Order_program")
window.geometry("600x400+500+300")
window.resizable(False, False)

frame1 = tk.Frame(window, width="600", height="10")
frame1.pack(fill="both")

frame2 = tk.Frame(window, width="600")
frame2.pack(fill="both", expand=True)

frame3 = tk.Frame(window, width="600")
# frame3.pack(fill="both", expand=True)

frame4 = tk.Frame(window, width="600", height="10")
frame4.pack(fill="both", expand=True)

btn_meal = tk.Button(frame1, text="Meal", padx="10", pady="10", bg="yellow", command=show_meal)
btn_meal.grid(row=0, column=0, padx=10, pady=10)

btn_drink = tk.Button(frame1, text="Beverage", padx="10", pady="10", bg="white", command=show_drink)
btn_drink.grid(row=0, column=1, padx=10, pady=10)

btn_end = tk.Button(frame1, text="Finish_order", padx="10", pady="10", command=order_end)
btn_end.grid(row=0, column=2, padx=10, pady=10)

label_price = tk.Label(frame1, text="0 $", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="3", padx="10", pady="10")

# Meal
btn_meal_1 = tk.Button(frame2, text="HotPot\n(20$)", padx="10", pady="10", width="10", command=lambda: meal_add('HotPot'))
btn_meal_1.grid(row=0, column=0, padx=10, pady=10)

btn_meal_2 = tk.Button(frame2, text="XinLamian\n(10$)", padx="10", pady="10", width="10", command=lambda: meal_add('Ramen'))
btn_meal_2.grid(row=0, column=1, padx=10, pady=10)

btn_meal_3 = tk.Button(frame2, text="Beef stake\n(30$)", padx="10", pady="10", width="10", command=lambda: meal_add('Beef stake'))
btn_meal_3.grid(row=0, column=2, padx=10, pady=10)

btn_meal_4 = tk.Button(frame2, text="Fried_chicken\n(15$)", padx="10", pady="10", width="10", command=lambda: meal_add('Fried_chicken'))
btn_meal_4.grid(row=0, column=3, padx=10, pady=10)

btn_meal_5 = tk.Button(frame2, text="Zicaibaofan\n(8$)", padx="10", pady="10", width="10", command=lambda: meal_add('Zicaibaofan'))
btn_meal_5.grid(row=0, column=4, padx=10, pady=10)


# Beverage
btn_drink_1 = tk.Button(frame3, text="Coffee\n(10$)", padx="10", pady="10", width="10", command=lambda: drink_add('Coffee'))
btn_drink_1.grid(row=0, column=0, padx=10, pady=10)

btn_drink_2 = tk.Button(frame3, text="Latte\n(15$)", padx="10", pady="10", width="10", command=lambda: drink_add('Latte'))
btn_drink_2.grid(row=0, column=1, padx=10, pady=10)

btn_drink_3 = tk.Button(frame3, text="Icetea\n(20$)", padx="10", pady="10", width="10", command=lambda: drink_add('Icetea'))
btn_drink_3.grid(row=0, column=2, padx=10, pady=10)

btn_drink_4 = tk.Button(frame3, text="Lemon\n(25$)", padx="10", pady="10", width="10", command=lambda: drink_add('Lemon'))
btn_drink_4.grid(row=0, column=3, padx=10, pady=10)

btn_drink_5 = tk.Button(frame3, text="Chocolate_smoothe\n(22$)", padx="10", pady="10", width="10", command=lambda: drink_add('Chocolate_smoothe'))
btn_drink_5.grid(row=0, column=4, padx=10, pady=10)


# Order_List
text_1 = tk.Text(frame4, height="10")
text_1.pack()

window.mainloop()