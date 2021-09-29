from tkinter import *
from PIL import Image,ImageTk


mw=Tk()
mw.title('Image Viewer')

img = ImageTk.PhotoImage(Image.open('images/space.png'))             #we can use this image for label,button,background
img_label = Label(mw, image=img)
img_label.pack()

mw.mainloop()

#tkinter also supports file formats ,but mostly they are waste formats like zif
#so we another library called PIL: python image library ,,it also old version
#then new version of PIL is Pillow: pillow.pypi

#Imagetk will create a object for us as we need the images outside tkinter like any folder by mentioning path
#image will open image for us
#imagetk will link image to tkinter

#generally tkinter is a two step process ie create a label[entry/Label/buton] and add label to display[grid/pack]
#but for images it is three step process
#open image and create a [background/Label/button] and add  to display[grid/pack]
