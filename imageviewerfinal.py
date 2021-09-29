from tkinter import *
from PIL import Image, ImageTk
import os

mw = Tk()
mw.title('Image Viewer')

path = 'images'
files_list = os.listdir(path)            #files_list:gives only name of file,,like: tharun.jpg
img_list = []                            #img_list:gives name with address ,,like:images/tharun.jpg
for f in files_list:
    if '.png' in f or '.jpg' in f:
        img_with_path = path + '/' + f
        img_list.append(img_with_path)

img = ImageTk.PhotoImage(Image.open(img_list[0]))              #0 : img_num , when we open ,it should opens from first photo
img_label = Label(mw, image=img)
img_label.grid(row=0, column=0, columnspan=3)

img_num= 0

def forward_func(num):
    global img,img_num
    back_btn.config(state='normal')
    img_num=num+1
  #  print(img_num, len(img_list))
    img = ImageTk.PhotoImage(Image.open(img_list[img_num]))
    img_label.config(image=img)                             #pack,grid,config belongs to display
    if len(img_list)==img_num+1:
        forward_btn.config(state='disabled')

def back_func(num):
    global img,img_num
    forward_btn.config(state='normal')
    img_num=num-1
    img = ImageTk.PhotoImage(Image.open(img_list[img_num]))
    img_label.config(image=img)
    if img_num==0:                                   #img_num=0 is first image
        back_btn.config(state='disabled')



back_btn = Button(mw, text='<<', font=('', 20),state='disabled', command=lambda: back_func(img_num))
back_btn.grid(row=1, column=0, padx=10, pady=20, sticky=W)

exit_btn = Button(mw, text='exit', font=('', 20), command=mw.quit)
exit_btn.grid(row=1, column=1, padx=10, pady=20)

forward_btn = Button(mw, text='>>', font=('', 20), command=lambda: forward_func(img_num))
forward_btn.grid(row=1, column=2, padx=10, pady=20, sticky=E)

mw.mainloop()


#click on the left imageviewer project folder >> open in >> explorer :directs to the folder in filemanager

#in terminal shortcuts
#--onefile : -F
#--noconsole : -w [window based]

#tfscLi telugu francise sc lion
#rcppst:rc.b people st