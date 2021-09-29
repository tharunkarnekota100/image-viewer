from tkinter import *
from PIL import Image,ImageTk
import os

mw=Tk()
mw.title('Image Viewer')

path ='images'         # path ='C:\Users\Tharun\PycharmProjects\imageviewer\images'
files_list = os.listdir(path)
print(files_list)


img = ImageTk.PhotoImage(Image.open('images/space.png'))             #we can use this image for label,button,background
img_label = Label(mw, image=img)
img_label.pack()

mw.mainloop()



#os library will gives all the files in any folder ,here folder:images, files:photos in folder