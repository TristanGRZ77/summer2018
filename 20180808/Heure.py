from Tkinter import *
import time
import threading

# 2 objet montre : demarre a l'heure courante, a une propriete mise a jour
# 3 dans le cadre, afficher une montre
# 4 dans le cadre, afficher deux montres
# gerer les evenements fermetures (soit par x, soit par bouton)
# utiliser un thread par horloge



#class maMontre:
#    def __init__(self, tempo, target, args= [], kwargs={}):
#        self._target = target
#        self._args = args
#        self._kwargs = kwargs
#        self._tempo = tempo
#
#    def _run(self):

#class horloge (Tk.Canvas):
#    def __init__(self, parent):
#        Tk.Canvas.__init__(self, parent, width=150, height=120)
#
#        self.create_rectangle(6, 60, 150, 114)
#        self.create_rectangle(6, 6, 150, 60)

def temps():
    global label
    while True: 
        heure = time.strftime('%H:%M:%S', time.localtime())
        label.config(text = heure)
        time.sleep(0.1)

fenetre = Tk()
bouton1 = Button(fenetre, text = "Fin", command = fenetre.quit)
bouton1.pack()

label = Label(fenetre, text = "")
label.pack()


#canvas = Canvas(fenetre, width = 150, height = 120)
#cadre1 = canvas.create_rectangle(6, 60, 150, 114)
#cadre2 = canvas.create_rectangle(6, 6, 150, 60)
#heure1 = canvas.create_text(78, 87, text = label)
#canvas.pack()

T = threading.Thread(target = temps)
T.start()

fenetre.mainloop()