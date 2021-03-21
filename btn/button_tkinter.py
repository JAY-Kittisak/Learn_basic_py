# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()
# img = Image.open('afadsf.jpg')
# photo = ImageTk.PhotoImage(img)

# lbl = Label(image=img)
# lbl.pack()


# root.mainloop()

from tkinter import *
# pip install Pillow
from PIL import Image, ImageTk


def basic():
    root = Tk()
    root.option_add("*Font", "consolas 20")
    img = Image.open("C:/Users/AKIRA/Desktop/Python/Learn_basic_py/btn/afadsf.jpg")
    img = img.resize((int(img.width * .5), int(img.height * .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(image=photo)
    lbl.pack()
    Label(root, text="วัดพระธาตุแช่แห้ง จังหวัดน่าน").pack()
    root.mainloop()


def adv():
    images = ['phumin-1', 'phumin-2', 'phumin-3']
    root = Tk()
    root.option_add("*Font", "consolas 20")
    img_list = []
    for i, img in enumerate(images):
        img_list.append(ImageTk.PhotoImage(Image.open(f"{img}.jpg")))
        lbl = Label(image=img_list[i])
        lbl.grid(row=0, column=i)
        Label(root, text=f"{img}.jpg").grid(row=1, column=i)
    root.mainloop()


if __name__ == '__main__':
    basic()
    # adv()