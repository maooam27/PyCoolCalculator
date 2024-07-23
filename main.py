from tkinter import *

root = Tk()
root.geometry("450x350")
root.title("PyCalc")

calc = StringVar()


def equal():
    try:
        if calc.get() == "":
            calc.set("0")
        calc.set(eval(calc.get()))
    except Exception as e:
        calc.set("Error")
        print(e)


def printV(value):
    calc.set(str(calc.get()) + value)


# Entry
prompt = Entry(root, width=40, borderwidth=6, font=("Arial", 26), textvariable=calc, justify="left",
               state="readonly")
prompt.pack()

# Buttons 1-+
buttons13 = Frame(root)
buttons13.pack()

button1 = Button(buttons13, text="1", pady=20, font=("Arial", 20), width=6, command=lambda: printV("1"))
button1.pack(side=LEFT)
button2 = Button(buttons13, text="2", pady=20, font=("Arial", 20), width=6, command=lambda: printV("2"))
button2.pack(side=LEFT)
button3 = Button(buttons13, text="3", pady=20, font=("Arial", 20), width=6, command=lambda: printV("3"))
button3.pack(side=LEFT)
button_plus = Button(buttons13, text="+", pady=20, font=("Arial", 20), width=6, command=lambda: printV("+"))
button_plus.pack(side=LEFT)

# Buttons 4--
buttons46 = Frame(root)
buttons46.pack()

button4 = Button(buttons46, text="4", pady=20, font=("Arial", 20), width=6, command=lambda: printV("4"))
button4.pack(side=LEFT)
button5 = Button(buttons46, text="5", pady=20, font=("Arial", 20), width=6, command=lambda: printV("5"))
button5.pack(side=LEFT)
button6 = Button(buttons46, text="6", pady=20, font=("Arial", 20), width=6, command=lambda: printV("6"))
button6.pack(side=LEFT)
button_minus = Button(buttons46, text="-", pady=20, font=("Arial", 20), width=6, command=lambda: printV("-"))
button_minus.pack(side=LEFT)

# Buttons 7-x
buttons79 = Frame(root)
buttons79.pack()

button7 = Button(buttons79, text="7", pady=20, font=("Arial", 20), width=6, command=lambda: printV("7"))
button7.pack(side=LEFT)
button8 = Button(buttons79, text="8", pady=20, font=("Arial", 20), width=6, command=lambda: printV("8"))
button8.pack(side=LEFT)
button9 = Button(buttons79, text="9", pady=20, font=("Arial", 20), width=6, command=lambda: printV("9"))
button9.pack(side=LEFT)
button_times = Button(buttons79, text="x", pady=20, font=("Arial", 20), width=6, command=lambda: printV("*"))
button_times.pack(side=LEFT)

# Buttons left
buttons_left = Frame(root)
buttons_left.pack()

button_canc = Button(buttons_left, text="C", pady=20, font=("Arial", 20), width=6, command=lambda: calc.set(""))
button_canc.pack(side=LEFT)
button0 = Button(buttons_left, text="0", pady=20, font=("Arial", 20), width=6, command=lambda: printV("0"))
button0.pack(side=LEFT)
button_equal = Button(buttons_left, text="=", pady=20, font=("Arial", 20), width=6, command=equal)
button_equal.pack(side=LEFT)
button_divide = Button(buttons_left, text=":", pady=20, font=("Arial", 20), width=6, command=lambda: printV("/"))
button_divide.pack(side=LEFT)

root.bind_all("<Return>", lambda e: equal())
root.bind_all("<KP_Enter>", lambda e: equal())

root.mainloop()
