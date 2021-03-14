import tkinter as tk
import pandas as pd

PATH_FILE = "test_data.csv"
df_house = pd.read_csv(PATH_FILE)


def set_message():
    output_label.configure(text=df_house)


windows = tk.Tk()
windows.title('testTitle')
windows.minsize(width=400, height=400)

title_label = tk.Label(master=windows, text='test')
title_label.pack(pady=20)
# pady = พื้นที่ว่างแนวตั้ง
# padx = พืนที่ระยะหางแนนนอน

number_input = tk.Entry(master=windows)
number_input .pack()

go_button = tk.Button(
    master=windows,
    text='คำนวณ',
    command=set_message,
    width=15,
    height=2
)
go_button.pack(pady=10)

output_label = tk.Label(master=windows)
output_label.pack(pady=20)

windows.mainloop()