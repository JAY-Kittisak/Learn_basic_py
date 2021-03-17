from tkinter import *
from tkinter import ttk
import tkcalendar as tkC

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("โปรแกรม JSR")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="โปรแกรม JSR",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="DarkSlateGray",fg="Snow")
        title.pack(side=TOP,fill=X)


#================== Manage Frame ===================================== 
        def grab_date_A():
            dataCAL = []
            data_cal_1 = cal.selection_get()
            print('data_cal_1>>>>>>>>🌌' , data_cal_1)
            dataCAL.append(data_cal_1)
            dataCAL[0] = dataCAL[0].strftime("%d/%m/%Y")
            my_label_A.config(text=dataCAL[0])
            print(dataCAL[0])

        def grab_date_B():
            dataCAL = []
            data_cal_1 = cal.selection_get()
            print('data_cal_1>>>>>>>>🌌' , data_cal_1)
            dataCAL.append(data_cal_1)
            dataCAL[0] = dataCAL[0].strftime("%d/%m/%Y")
            my_label_B.config(text=dataCAL[0])
            print(dataCAL[0])

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="DarkSlateGray")
        Manage_Frame.place(x=20,y=100,width=450,height=560)

        m_title=Label(Manage_Frame,text="เลือกตัวเลือก",bg="DarkSlateGray",fg="Snow",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=1,pady=0)

        lbl_1_roll=Label(Manage_Frame,text="Column 1.",bg="DarkSlateGray",fg="Snow",font=("times new roman",15,"bold"))
        lbl_1_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",10,"bold"))
        combo_gender['values']=('1','2')
        combo_gender.grid(row=1,column=1,padx=20,pady=10)

        lbl_2_roll=Label(Manage_Frame,text="Column 2.",bg="DarkSlateGray",fg="Snow",font=("times new roman",15,"bold"))
        lbl_2_roll.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        combo_2_gender=ttk.Combobox(Manage_Frame,font=("times new roman",10,"bold"))
        combo_2_gender['values']=('1','2')
        combo_2_gender.grid(row=2,column=1,padx=20,pady=10)

        lbl_3_roll=Label(Manage_Frame,text="Roll No.",bg="DarkSlateGray",fg="Snow",font=("times new roman",15,"bold"))
        lbl_3_roll.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_3_Roll=Entry(Manage_Frame,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_3_Roll.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        cal = tkC.Calendar(Manage_Frame, selectmone='day', year=2021, month=3, day=16)
        cal.grid(row=5,column=1,padx=0,pady=30)

        my_button_A = Button(Manage_Frame, text='Starting date', command=grab_date_A)
        my_button_A.grid(row=6,column=0,padx=0,pady=0)

        my_button_B = Button(Manage_Frame, text='End date', command=grab_date_B)
        my_button_B.grid(row=6,column=1,padx=0,pady=0)

        my_label_A = Label(Manage_Frame, text='')
        my_label_A.grid(row=7,column=0,padx=0,pady=10)

        my_label_B = Label(Manage_Frame, text='')
        my_label_B.grid(row=7,column=1,padx=0,pady=10)



#================== Detail Frame ===================================== 
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="DarkSlateGray")
        Detail_Frame.place(x=500,y=100,width=800,height=560)

root=Tk()
ob=Student(root)
root.mainloop()