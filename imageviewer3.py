from tkinter import *
from PIL import Image,ImageTk
import os

mw=Tk()
mw.title('Image Viewer')

path ='images'
files_list = os.listdir(path)
for f in files_list:
    if '.png' in f or '.jpg' in f :
        print(f)

img = ImageTk.PhotoImage(Image.open('images/'+files_list[1]))
img_label = Label(mw, image=img)
img_label.pack()

mw.mainloop()

