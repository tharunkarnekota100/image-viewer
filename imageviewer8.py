from tkinter import *
from PIL import Image, ImageTk
import os

mw = Tk()
mw.title('Image Viewer')

path = 'images'
files_list = os.listdir(path)
img_list = []
for f in files_list:
    if '.png' in f or '.jpg' in f:
        img_with_path = path + '/' + f
        img_list.append(img_with_path)

img = ImageTk.PhotoImage(Image.open(img_list[0]))
img_label = Label(mw, image=img)
img_label.grid(row=0, column=0, columnspan=3)

img_num= 0

def forward_func(num):
    global img,img_num
    img_num=num+1
    img = ImageTk.PhotoImage(Image.open(img_list[img_num]))
    img_label.config(image=img)


back_btn = Button(mw, text='<<', font=('', 20))
back_btn.grid(row=1, column=0, padx=10, pady=20, sticky=W)

exit_btn = Button(mw, text='exit', font=('', 20), command=mw.quit)
exit_btn.grid(row=1, column=1, padx=10, pady=20)

forward_btn = Button(mw, text='>>', font=('', 20), command=lambda: forward_func(img_num))
forward_btn.grid(row=1, column=2, padx=10, pady=20, sticky=E)

mw.mainloop()


#forward button work
#note: we will get error after last image
#we will skip error in next program