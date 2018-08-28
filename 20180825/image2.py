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
    affichageHome()
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
    affichageHaut()
    deplacementHaut(tempsDeplacement, x, y)
    
def boutonBas():
    deplacementStop()
    affichageBas()
    deplacementBas(tempsDeplacement, x, y)

def boutonGauche():
    deplacementStop()
    affichageGauche()
    deplacementGauche(tempsDeplacement, x, y)

def boutonDroit():
    deplacementStop()
    affichageDroit()
    deplacementDroit(tempsDeplacement, x, y)

# Affichage des labels

def affichageHaut():
    haut = Label(root, text = "  Haut  ", bg = "black", fg = "white").grid(column = 1, row = 0, sticky = W)

def affichageBas():
    bas = Label(root, text = "   Bas   ", bg = "black", fg = "white").grid(column = 1, row = 0, sticky = W)

def affichageGauche():
    gauche = Label(root, text = "Gauche", bg = "black", fg = "white").grid(column = 1, row = 0, sticky = W)

def affichageDroit():
    droite = Label(root, text = " Droite ", bg = "black", fg = "white").grid(column = 1, row = 0, sticky = W)

def affichageStop():
    stop1 = Label(root, text = "  Stop  ", bg = "black", fg = "white").grid(column = 1, row = 0, sticky = W)

def affichageHome():
    home1 = Label(root, text = "  Home  ", bg = "black", fg = "white").grid(column = 1, row = 0, sticky = W)

# Fonction qui arrete le deplacement de l'image
def deplacementStop():
    global _job
    if _job is not None:
        affichageStop()
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
    can.grid(column = 1, row = 1)
    Button(root, text = "Recentrer l'image", command = home ).grid(column = 1, row = 3, rowspan = 1)
    Button(root, text = "Gauche", command = boutonGauche ).grid(column = 1, row = 3, rowspan = 1, sticky = W)
    Button(root, text = "Droite", command = boutonDroit ).grid(column = 1, row = 3, rowspan = 1, sticky = E)
    Button(root, text = "Haut", command = boutonHaut ).grid(column = 1, row = 2)
    Button(root, text = "Bas", command = boutonBas ).grid(column = 1, row = 4)
    Button(root, text = "Stop", command = deplacementStop ).grid(column = 1, row = 5)
    home()

affichage()
root.mainloop()