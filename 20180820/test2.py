from Tkinter import *
from datetime import datetime  
from datetime import timedelta

heure1 = datetime.now()
heure2 = datetime.now()

def horloge1():
    global heure1
    heures = a.get()
    minutes = b.get()
    secondes = c.get()
    try:
        heure1 = heure1.replace(hour=int(heures), minute=int(minutes), second=int(secondes))
    except:
        print "La valeur saisie est incorrecte"

def horloge2():
    global heure2
    heures = a2.get()
    minutes = b2.get()
    secondes = c2.get()
    try:
        heure2 = heure2.replace(hour=int(heures), minute=int(minutes), second=int(secondes))
    except:
        print "La valeur saisie est incorrecte"

def tick1(): 
    global heure1
    heure1 += timedelta(seconds=1)
    montre1.config(text = heure1)
    montre1.after(1000, tick1)

def tick2():
    global heure2
    heure2 += timedelta(seconds=1)
    montre2.config(text = heure2)
    montre2.after(1000, tick2)

root = Tk()

montre1 = Label(root, font = ("times", 20))
montre1.pack()
tick1()

montre2 = Label(root, font = ("times", 20))
montre2.pack()
tick2()

a = Entry(root)
a.pack()
a.focus_set()

b = Entry(root)
b.pack()
b.focus_set()

c = Entry(root)
c.pack()
c.focus_set()

btn1 = Button(root, text = "Regler l'heure 1", command = horloge1)
btn1.pack()

a2 = Entry(root)
a2.pack()
a2.focus_set()

b2 = Entry(root)
b2.pack()
b2.focus_set()

c2 = Entry(root)
c2.pack()
c2.focus_set()

btn2 = Button(root, text = "Regler l'heure 2", command = horloge2)
btn2.pack()

root.mainloop()