from Tkinter import *

# Definition des variables
root = Tk()
global x
global y
global _job

largeurEcran = 320
hauteurEcran = 320
y = hauteurEcran / 2
x = largeurEcran / 2
img = PhotoImage(file = "/Users/tristanbouteville/Documents/Yacht.512.ppm")
largeurImage= img.width()
hauteurImage = img.height()
xmax = largeurEcran - (largeurImage/2) - 1
xmin = (largeurImage / 2) - 1
ymax = hauteurEcran - (hauteurImage/2) - 1
ymin = (hauteurImage / 2) + 1
can = Canvas(root, width = largeurEcran, height = hauteurEcran, bg = "black")
tempsDeplacement = 100
_job = None
pasDeplacement = 10

# Fonction qui replace l'image au centre
def home():
    global x
    global y
    deplacementStop()
    x = largeurEcran/2
    y = hauteurEcran/2
    action(x,y)

# Boutons directionnels et deplacements
def deplacementHaut(_temps, _x, _y):
    global x
    global y
    global _job
    if (y < ymin):
        y = ymin
        deplacementStop()
    else:
        y -= pasDeplacement
        action(x,y)
        _job = can.after(tempsDeplacement, deplacementHaut, tempsDeplacement, x, y)

def deplacementBas(_temps, _x, _y):
    global x
    global y
    global _job
    if (y > ymax):
        y = ymax
        deplacementStop()
    else:
        y += pasDeplacement
        action(x,y)
        _job = can.after(tempsDeplacement, deplacementBas, tempsDeplacement, x, y)

def deplacementGauche(_temps, _x, _y):
    global x
    global y
    global _job
    if (x < xmin):
        x = xmin
        deplacementStop()
    else:
        x -= pasDeplacement
        action(x,y)
        _job = can.after(tempsDeplacement, deplacementGauche, tempsDeplacement, x, y)

def deplacementDroit(_temps, _x, _y):
    global x
    global y
    global _job
    if (x > xmax):
        x = xmax
        deplacementStop()
    else:
        x += pasDeplacement
        action(x,y)
        _job = can.after(tempsDeplacement, deplacementDroit, tempsDeplacement, x, y)

def boutonHaut():
    deplacementStop()
    deplacementHaut(tempsDeplacement, x, y)
    
def boutonBas():
    deplacementStop()
    deplacementBas(tempsDeplacement, x, y)

def boutonGauche():
    deplacementStop()
    deplacementGauche(tempsDeplacement, x, y)

def boutonDroit():
    deplacementStop()
    deplacementDroit(tempsDeplacement, x, y)

# Fonction qui arrete le deplacement de l'image
def deplacementStop():
    global _job
    if _job is not None:
        root.after_cancel(_job)
        _job = None

# Actualise les coordonees du centre de l'image
def action(_x, _y):
    can.delete("all") 
    can.create_image(_x, _y, image = img)

# Affiche la fenetre
def affichage():
    global _job
    _job = None
    can.grid(column = 1, row = 0)
    Button(root, text = "Recentrer l'image", command = home ).grid(column = 1, row = 2)
    Button(root, text = "Gauche", command = boutonGauche ).grid(column = 0, row = 2)
    Button(root, text = "Droite", command = boutonDroit ).grid(column = 2, row = 2)
    Button(root, text = "Haut", command = boutonHaut ).grid(column = 1, row = 1)
    Button(root, text = "Bas", command = boutonBas ).grid(column = 1, row = 3)
    Button(root, text = "Stop", command = deplacementStop ).grid(column = 1, row = 4)
    home()

affichage()
root.mainloop()