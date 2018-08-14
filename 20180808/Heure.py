from Tkinter import *
import time
import threading

def temps():
    global label
    while True:
        heure = time.strftime('%H:%M:%S', time.localtime())
        label.config(text = heure)
        time.sleep(0.1)

fenetre = Tk()
label = Label(fenetre, text = "")
label.pack()

T = threading.Thread(target = temps)
T.start()

fenetre.mainloop()