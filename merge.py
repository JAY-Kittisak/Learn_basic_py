import tkinter as tk
import pandas as pd

PATH_FILE = "data.xlsx"
df_house = pd.read_excel(PATH_FILE)
print(df_house.columns)


def set_message():
    cl1_input = column1_input.get()
    cl2_input = column2_input.get()
    cl3_input = column3_input.get()
    output_label.configure(text=df_house[[cl1_input, cl2_input, cl3_input]])


root = tk.Tk()
root.title('testTitle')
root.minsize(width=400, height=400)

title_label = tk.Label(master=root, text='test')
title_label.pack(pady=20)
# pady = พื้นที่ว่างแนวตั้ง
# padx = พืนที่ระยะหางแนนนอน


column1_input = tk.Entry(master=root)
column1_input .pack()
column2_input = tk.Entry(master=root)
column2_input .pack()
column3_input = tk.Entry(master=root)
column3_input .pack()

go_button = tk.Button(
    master=root,
    bg='orange',
    text='คำนวณ',
    command=set_message,
    width=15,
    height=2
)
go_button.pack(pady=10)

output_label = tk.Label(master=root)
output_label.pack(pady=20)

root.mainloop()