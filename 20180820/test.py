from Tkinter import *
from datetime import datetime  
from datetime import timedelta

heure1 = datetime.now()
heure2 = datetime.now()

#def horloge1():
#    global heure1
#    heures = a.get()
#    minutes = d.get()
#    secondes = g.get()
#    heure1 = heure1.replace(hour=int(heures), minute=int(minutes), second=int(secondes))

def horloge(_heure, x, y, z):
    heures = x
    minutes = y
    secondes = z
    _heure = _heure.replace(hour = int(heures), minutes = int(minutes), second = int(secondes))

def tick(_heure, _montre):
    _heure += timedelta(seconds = 1)
    _montre.config(text = _heure)
    _montre.after(1000, tick)

root = Tk()

a = Entry(root)
a.pack()
a.focus_set()
#btnh = Button(root, text = "Appuyer une fois les heures saisies", command = heu)
#btnh.pack()

montre1 = Label(root, font = ("times", 20))
montre1.pack()
tick(heure1, montre1)

# montre2 = Label(root, font = ("times", 20))
# montre2.pack()
# tick(heure2, montre2)

# b = Entry(root)
# b.pack()
# b.focus_set()
# #btnm = Button(root, text = "Appuyer une fois les minutes saisies", command = min)
# #btnm.pack()

# c = Entry(root)
# c.pack()
# c.focus_set()
# #btns = Button(root, text = "Appuyer une fois les secondes saisies", command = sec)
# #btns.pack()

# btn1 = Button(root, text = "Regler l'heure 1", command = horloge(heure1, a.get(), b.get(), c.get()))
# btn1.pack()

# a2 = Entry(root)
# a2.pack()
# a2.focus_set()
# #btnh2 = Button(root, text = "Appuyer une fois les heures saisies", command = heu2)
# #btnh2.pack()

# b2 = Entry(root)
# b2.pack()
# b2.focus_set()
# #btnm2 = Button(root, text = "Appuyer une fois les minutes saisies", command = min2)
# #btnm2.pack()

# c2 = Entry(root)
# c2.pack()
# c2.focus_set()
# #btns2 = Button(root, text = "Appuyer une fois les secondes saisies", command = sec2)
# #btns2.pack()

# btn2 = Button(root, text = "Regler l'heure 2", command = horloge(heure2, a2.get(), b2.get(), c2.get()))
# btn2.pack()

root.mainloop()

#def horloge1():
#    global heure1
#    heures = a.get()
#    minutes = d.get()
#    secondes = g.get()
#    heure1 = heure1.replace(hour=int(heures), minute=int(minutes), second=int(secondes))

#def horloge2():
#    global heure2
#    heures = a2.get()
#    minutes = d2.get()
#    secondes = g2.get()
#    heure2 = heure2.replace(hour=int(heures), minute=int(minutes), second=int(secondes))

#def tick1():
#    global heure1
#    heure1 += timedelta(seconds=1)
#    montre1.config(text = heure1)
#    montre1.after(1000, tick1)

#def tick2():
#    global heure2
#    heure2 += timedelta(seconds=1)
#    montre2.config(text = heure2)
#    montre2.after(1000, tick2)

#def heu():
#    heures = a.get()

#def min():
#    minutes = d.get()

#def sec():
#    secondes = g.get()

#def heu2():
#    heures = a2.get()

#def min2():
#    minutes = d2.get()

#def sec2():
#    secondes = g2.get()