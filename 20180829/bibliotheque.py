from Tkinter import*
import Tkinter as Tk
from math import *

# t correspond au chiffre saisi
# y correspond a l'operateur utilise 
# n correspond au nombre de valeurs que compose un facteur

root = Tk.Tk()
t, y, n = 0, 0, 1

# fonction qui permet l'affichage de facteurs a plusieurs chiffres

def nombre(x):
    global t, n   
    t = t * 10 + x
    u.set(str(t))

# fonction liee aux boutons chiffres qui saisissent les valeurs desirees

def x(_nombre):
    nombre(_nombre)

# t1 correspond au deuxieme facteur de l'operation
# fonction d'operation

def operation(_signe):
    global y, t1, t, n
    y, t1, n = _signe, t, 1
    t = 0
        
def aegal():
    global t, t1, n
    z.set("0")
    if y == '+':
        z.set(str((t1 + t)))
        t = t1 + t
    elif y == '-':
        z.set(str((t1 - t)))
        t = t1 - t
    elif y == '*':
        z.set(str((t1 * t)))
        t = t1 * t
    elif y == '/':
        if t == 0:
            z.set(str("Erreur, impossible"))
        else:
            z.set(str((t1 / t)))
            t = t1 / t
    elif y == '%':
        if t == 0:
            z.set(str("Erreur, impossible"))
        else:
            z.set(str((t1 % t)))
            t = t1 % t

    t1, n = 0, 1
    clear(u)

def clear(_clear):
    global t, t1, n, z, u, y
    t, t1, n, y = 0, 0, 0, 0
    _clear.set(str('0'))

def ecran():
    global z
    global u
    
    btn1 = Button(root, text = "1", command = lambda : x(1))
    btn1.grid(column = 0, row = 0)
    btn2 = Button(root, text = "2", command = lambda : x(2))
    btn2.grid(column = 1, row = 0)
    btn3 = Button(root, text = "3", command = lambda : x(3))
    btn3.grid(column = 2, row = 0)
    btn4 = Button(root, text = "4", command = lambda : x(4))
    btn4.grid(column = 0, row = 1)
    btn5 = Button(root, text = "5", command = lambda : x(5))
    btn5.grid(column = 1, row = 1)
    btn6 = Button(root, text = "6", command = lambda : x(6))
    btn6.grid(column = 2, row = 1)
    btn7 = Button(root, text = "7", command = lambda : x(7))
    btn7.grid(column = 0, row = 2)
    btn8 = Button(root, text = "8", command = lambda : x(8))
    btn8.grid(column = 1, row = 2)
    btn9 = Button(root, text = "9", command = lambda : x(9))
    btn9.grid(column = 2, row = 2)
    btnc = Button(root, text = "C", command = clear)
    btnc.grid(column = 0, row = 3)
    btn0 = Button(root, text = "0", command = lambda : x(0))
    btn0.grid(column = 1, row = 3)
    btnr = Button(root, text = "=", command = aegal)
    btnr.grid(column = 2, row = 3)
    btna = Button(root, text = "+", command = lambda : operation("+"))
    btna.grid(column = 3, row = 0)
    btns = Button(root, text = "-", command = lambda : operation("-"))
    btns.grid(column = 3, row = 1)
    btnm = Button(root, text = "*", command = lambda : operation("*"))
    btnm.grid(column = 3, row = 2)
    btnd = Button(root, text = "/", command = lambda : operation("/"))
    btnd.grid(column = 3, row = 3)

    btnd = Button(root, text = "%", command = lambda : operation("%"))
    btnd.grid(column = 4, row = 1, stick = "W")

    u = StringVar()
    entree2 = Entry(root, textvariable = u)
    entree2.grid(column = 4, row = 2)
    u.set("0")

    z = StringVar()
    entree = Entry(root, textvariable = z)
    entree.grid(column = 4, row = 3)
    z.set("0")

    btnquit = Button(root, text = 'Quitter', command = root.destroy)
    btnquit.grid(column = 4, row = 0)