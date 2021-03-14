import tkinter as tk


def set_message():
    number_in_str = number_input.get()

    if number_in_str == '':
        output_label.configure(text='โปรใส่ตัวเลข')
        return

    number_in = int(number_input.get())

    if number_in == 0:
        output_label.configure(text='error')

    output = ''
    for i in range(1, 13):
        output += str(number_in) + ' x ' + str(i)
        output += ' = ' + str(number_in * i) + '\n'

    output_label.configure(text=output)


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
