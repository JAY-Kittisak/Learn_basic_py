from tkinter import *

root = Tk()
root.option_add('*Font',"impact 30")

Label(root, text="weight (kg.)").grid(row=0, column=0, sticky=W, padx=10, pady=10)
Entry(root, width=6).grid(row=0, column=1, padx=10)
Label(root, text="hight (m.)").grid(row=1, column=0, sticky=W, padx=10, pady=10)
Entry(root, width=6).grid(row=1, column=1, padx=10)
Label(root, text="BMI").grid(row=2, column=0)
Button(root, text="calculate").grid(row=3, columnspan=2, pady=10)

root.mainloop()