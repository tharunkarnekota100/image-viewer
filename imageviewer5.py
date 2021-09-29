from tkinter import *
from PIL import Image,ImageTk
import os

mw=Tk()
mw.title('Image Viewer')

path ='images'
files_list = os.listdir(path)
img_list = []
for f in files_list:
    if '.png' in f or '.jpg' in f :
        img_with_path =path + '/'+f
        img_list.append(img_with_path)

print(img_list)
img = ImageTk.PhotoImage(Image.open(img_list[5]))             #only change is here
img_label = Label(mw, image=img)
img_label.pack()

mw.mainloop()

#files list contain all formats
#here we create a new list [img_list]contain only .jpg .png format files