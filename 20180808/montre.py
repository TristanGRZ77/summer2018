import time
import Tkinter as Tk
from Tkinter import *

#def tick():
#    global time1
#    time2 = time.strftime("%H:%M:%S")
#    if time2 != time1:
#        time1 = time2
#        clock.config(text = time2)
#        clock.after(1000, tick)

def test():
    #time2 = time.strftime("%H:%M:%S")     
    #clock.config(text = "toto") 
    print "test"
    clock.after(1000, test())
    #canvas.create_text(100, 150, text = time.strftime("%H:%M:%S")) 
    

root = Tk()

time1 = ""
clock = Label(root, font = ("times", 20))
canvas = Canvas(root, width = 200, height = 200)
cadre1 = canvas.create_rectangle(10, 10, 190, 190)
cadre2 = canvas.create_line(10, 100, 190, 100)
#heure = canvas.create_text(100, 150, text = clock)

# time2 = time.strftime("%H:%M:%S")
# if time2 != time1:
#     time1 = time2
# heure =  
canvas.create_text(100, 150, text = time.strftime("%H:%M:%S")) 
clock.after(1000, test())

canvas.pack()

#tick()
root.mainloop()

#time1 = time.strftime('%H:%M:%S', time.localtime())
#time2 = time.strftime('%H:%M:%S', time.localtime())

#root = Tk.Tk()
#root.title('Horloge') 
#Horloge()
#root.mainloop() 