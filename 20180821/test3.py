from Tkinter import *
import datetime as dt
from datetime import datetime  
from datetime import timedelta

#heure1 = datetime.now()
now = dt.datetime.now()
now = now.replace(microsecond = 0)
delta = dt.timedelta(seconds = 1)
heure1 = now.time()
heure2 = now.time()

def horloge1():
    global heure1
    heures = a.get()
    minutes = b.get()
    secondes = c.get()
    try:
        heure1 = heure1.replace(hour=int(heures), minute=int(minutes), second=int(secondes))
    except:
        o = Label(root, text = "La valeur saisie n'est pas un entier")
        o.grid(column = 0, row = 6)

def horloge2():
    global heure2
    heures = a2.get()
    minutes = b2.get()
    secondes = c2.get()
    try:
        heure2 = heure2.replace(hour=int(heures), minute=int(minutes), second=int(secondes))
    except:
        o2 = Label(root, text = "La valeur saisie n'est pas un entier")
        o2.grid(column = 2, row = 6)

def tick1(): 
    global heure1
    heure1 = ((dt.datetime.combine(dt.date(1,1,1), heure1) + delta).time())
    montre1.config(text = heure1)
    montre1.after(1000, tick1)

def tick2():
    global heure2
    heure2 = ((dt.datetime.combine(dt.date(1,1,1), heure2) + delta).time())
    montre2.config(text = heure2)
    montre2.after(1000, tick2)

def reglage1():
    global a
    global b
    global c

    m = Label(root, text = "Nouvelles heures :")
    m.grid(column = 0, row = 2)

    a = Entry(root)
    a.grid(column = 1, row = 2)
    a.focus_set()

    n = Label(root, text = "Nouvelles minutes :")
    n.grid(column = 0, row = 3)

    b = Entry(root)
    b.grid(column = 1, row = 3)
    b.focus_set()

    o = Label(root, text = "Nouvelles secondes :")
    o.grid(column = 0, row = 4)

    c = Entry(root)
    c.grid(column = 1, row = 4)
    c.focus_set()

    btn1 = Button(root, text = "Regler l'heure 1", command = horloge1)
    btn1.grid(column = 0, row = 5)

def reglage2():
    global a2
    global b2
    global c2

    m2 = Label(root, text = "Nouvelles heures :")
    m2.grid(column = 2, row = 2)

    a2 = Entry(root)
    a2.grid(column = 3, row = 2)
    a2.focus_set()

    n2 = Label(root, text = "Nouvelles minutes :")
    n2.grid(column = 2, row = 3)

    b2 = Entry(root)
    b2.grid(column = 3, row = 3)
    b2.focus_set()

    o2 = Label(root, text = "Nouvelles secondes :")
    o2.grid(column = 2, row = 4)

    c2 = Entry(root)
    c2.grid(column = 3, row = 4)
    c2.focus_set()

    btn2 = Button(root, text = "Regler l'heure 2", command = horloge2)
    btn2.grid(column = 2, row = 5)

root = Tk()

montre1 = Label(root, font = ("times", 20))
montre1.grid(column = 0, row = 0)
tick1()

montre2 = Label(root, font = ("times", 20))
montre2.grid(column = 2, row = 0)
tick2()

maj1 = Button(root, text = "Mise a jour de la premiere heure", command = reglage1) 
maj1.grid(column = 0, row = 1)

maj2 = Button(root, text = "Mise a jour de la seconde heure", command = reglage2)
maj2.grid(column = 2, row = 1)

root.mainloop()