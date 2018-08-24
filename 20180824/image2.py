from Tkinter import *

w = True

root = Tk()
global x
global y

# Definition des variables

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

# Fonction qui replace l'image au centre

def home():
    stop2()
    action(largeurEcran/2,hauteurEcran/2)

# Boutons directionnels et deplacements

def boutonHaut():
    global x
    global y
    global w
    if (y < ymin):
        y = ymin
    if w != True:
        w = True
        return root.mainloop()
    else:
        y -= 1
        deplacementHaut()
    action(x,y)

def boutonBas():
    global x
    global y
    global w
    if (y > ymax):
        y = ymax
    if w != True:
        w = True
        return root.mainloop()
    else:
        y += 1
        deplacementBas()
    action(x,y)

def boutonGauche():
    global x
    global y
    global w
    if (x < xmin):
        x = xmin
    if w != True:
        w = True
        return root.mainloop()
    else:
        x -= 1
        deplacementGauche()
    action(x,y)

def boutonDroit():
    global x
    global y
    global w
    if (x > xmax):
        x = xmax
    if w != True:
        w = True
        return root.mainloop()
    else:
        x += 1
        deplacementDroit()
    action(x,y)

def deplacementHaut():
    can.after(100, boutonHaut)

def deplacementBas():
    can.after(100, boutonBas)

def deplacementGauche():
    can.after(100, boutonGauche)

def deplacementDroit():
    can.after(100, boutonDroit)

# Fonction qui arrete le deplacement de l'image

def stop():
    global w
    w = False

# Fonction liee a la fonction home, qui arrete le deplacement de l'image et replace les coordonees du centre de l'image au centre de la fenetre, 
# ce qui permet de pouvoir utiliser a nouveau les boutons directionnels depuis le centre de la fenetre et non la ou l'image s'est arretee

def stop2():
    global w
    global x
    global y
    w = False
    action(160, 160)
    x = 160
    y = 160

# Actualise les coordonees du centre de l'image

def action(_x, _y):
    can.delete("all") 
    can.create_image(_x, _y, image = img)

# Affiche la fenetre

def affichage():
    can.grid(column = 1, row = 0)

    Button(root, text = "Recentrer l'image", command = home ).grid(column = 1, row = 2)

    Button(root, text = "Gauche", command = boutonGauche ).grid(column = 0, row = 2)

    Button(root, text = "Droite", command = boutonDroit ).grid(column = 2, row = 2)

    Button(root, text = "Haut", command = boutonHaut ).grid(column = 1, row = 1)

    Button(root, text = "Bas", command = boutonBas ).grid(column = 1, row = 3)

    Button(root, text = "Stop", command = stop).grid(column = 1, row = 4)

    home()

affichage()
root.mainloop()