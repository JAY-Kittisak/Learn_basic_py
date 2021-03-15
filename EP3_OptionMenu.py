import tkinter as tk
import pandas as pd

PATH_FILE = "data.xlsx"
df_house = pd.read_excel(PATH_FILE)
print(df_house.columns)

def on_click(e):
    # f คือ format starig ทำให้อ่านตัวแปรใน {} ได้
    tv_string.set(f'you selected {selectedOpt.get()}')

root = tk.Tk()
root.option_add('*Font', 'consolas 10')
root.title('testTitle')
root.minsize(width=400, height=400)

countries = ['Thailand', 'Japan', 'korea']

selectedOpt = tk.StringVar()
selectedOpt.set('โปรเลือกตัวเลือก')

tv_string = tk.StringVar()

om = tk.OptionMenu(root, selectedOpt, *df_house.columns)
om.config(width=15)
om.grid(row=0, column=0)

btn = tk.Button(root, text='select', bg='orange')
btn.grid(row=0, column=1)
btn.bind('<Button-1>', on_click)

tk.Label(root, textvariable=tv_string).grid(row=1, column=2)

root.mainloop()