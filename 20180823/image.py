from Tkinter import *

root = Tk()
global x
global y
global sprite

largeurEcran = 128
hauteurEcran = 128
y = hauteurEcran / 2
x = largeurEcran / 2
img = PhotoImage(file = "/Users/tristanbouteville/Documents/Yacht.512.ppm")
largeurImage= img.width()
hauteurImage = img.height()

xmax = largeurEcran - (largeurImage/2) - 1
xmin = (largeurImage / 2) - 1
ymax = hauteurEcran - (hauteurImage/2) - 1
ymin = (hauteurImage / 2) + 1

def home():
    action(largeurEcran/2,hauteurEcran/2)

def boutonHaut():
    global x
    global y
    if (y < ymin):
        y = ymin
    else:
        y -= 1
    action(x,y)

def boutonBas():
    global x
    global y
    if (y > ymax):
        y = ymax
    else:
        y += 1
    action(x,y)

def boutonGauche():
    global x
    global y
    if (x < xmin):
        x = xmin
    else:
        x -= 1
    action(x,y)

def boutonDroit():
    global x
    global y
    if (x > xmax):
        x = xmax
    else:
        x += 1
    action(x,y)

def action(_x, _y):
    can.delete("all")
    can.create_image(_x, _y, image = img)

can = Canvas(root, width = largeurEcran, height = hauteurEcran, bg = "black")
can.pack(expand = 1, fill = BOTH)

Button(root, text = "Recentrer l'image", command = home ).pack()

btng = Button(root, text = "Gauche", command = boutonGauche )
btng.pack()

btnd = Button(root, text = "Droite", command = boutonDroit )
btnd.pack()

btng = Button(root, text = "Haut", command = boutonHaut )
btng.pack()

btnd = Button(root, text = "Bas", command = boutonBas )
btnd.pack()

home()

root.mainloop()