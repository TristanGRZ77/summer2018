from Tkinter import *

def test():
    pass

root = Tk()

btn1 = Button(root, text = "1", bg = "green", fg = "blue", command = test)
btn1.pack()

root.mainloop()