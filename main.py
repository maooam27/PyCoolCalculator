from tkinter import *

root = Tk()
root.geometry("400x600")
root.title("PyCalc")

calc = StringVar()

# Entry
prompt = Entry(root, width=40, borderwidth=6, font=("Arial", 26), textvariable=calc, justify="left",
               state="readonly")
prompt.pack()

buttons = Frame(root)
buttons.pack()

root.bind_all("<Return>", lambda e: print("Enter"))

root.mainloop()
