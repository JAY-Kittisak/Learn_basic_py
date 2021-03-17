import pandas as pd
import tkinter as tk
import tkcalendar as tkC

root = tk.Tk()
root.title('Codemy.com')
# rott.iconditmap()
root.geometry('600x700')

cal_A = tkC.Calendar(root, selectmone='day', year=2021, month=3, day=16)
cal_A.pack(pady=20)

def grab_date_A():


    dataCAL = []
    data_cal_1 = cal_A.selection_get()
    print('data_cal_1>>>>>>>>🌌' , data_cal_1)
    dataCAL.append(data_cal_1)
    dataCAL[0] = dataCAL[0].strftime("%d/%m/%Y")

    print(dataCAL[0])
    # print('data_cal_2>>>>>>>>🌌' , data_cal_2)
    # data_cal_3 = data_cal_2.pd.dt.strftime('%d/%m/%Y')
    # my_label_A.config(text=data_cal_3)
    # print(data_cal_3)
    # my_label_A.config(text=data_cal_1)
    # print(data_cal_1)

def grab_date_B():
    my_label_B.config(text=cal_B.get_date())
    print(cal_B.get_date())

my_button_A = tk.Button(root, text='Get Date A', command=grab_date_A)
my_button_A.pack(pady=20)

my_label_A = tk.Label(root, text='')
my_label_A.pack(pady=20)

cal_B = tkC.Calendar(root, selectmone='day', year=2021, month=3, day=16)
cal_B.pack(pady=20)

my_button_B = tk.Button(root, text='Get Date B', command=grab_date_B)
my_button_B.pack(pady=20)

my_label_B = tk.Label(root, text='')
my_label_B.pack(pady=20)

root.mainloop()
