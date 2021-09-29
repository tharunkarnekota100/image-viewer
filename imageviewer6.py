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

img = ImageTk.PhotoImage(Image.open(img_list[3]))
img_label = Label(mw, image=img)
img_label.grid(row=0, column=0,columnspan=3)

back_btn = Button(mw, text='<<', font=('',20))
back_btn.grid(row=1, column=0,padx=10,pady=20,sticky=W)

exit_btn = Button(mw, text='exit', font=('',20), command=mw.quit)
exit_btn.grid(row=1, column=1,padx=10,pady=20)

forward_btn = Button(mw, text='>>', font=('',20))
forward_btn.grid(row=1, column=2,padx=10,pady=20)

mw.mainloop()

# here we create three buttons << >> exit
#working of exit
#one design mistake in it guess it