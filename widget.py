# Import necessary libraries

from tkinter import *

# Create Window

window = Tk()

# Set the window Title and Geometry

window.title('Demo Window')

window.geometry('400x300') 
lbl=Label(text="hi there how are you",fg="red",bg="yellow",height=2,width=200)
lbl.pack()
btn = Button(text="Begin",  height=1, bg="#1261A0")
btn.pack()
entry=Entry()
entry.pack()
Txt=Text(fg="black",bg="grey",height=10)
Txt.pack()
window.mainloop()
