from Tkinter import*
import Tkinter as Tk
from math import *

# t correspond au chiffre saisi
# y correspond a l'operateur utilise 
# n correspond au nombre de valeurs que compose un facteur

t, y, n = 0, 0, 1

# fonction qui permet l'affichage de facteurs a plusieurs chiffres

def nombre(x):
        global t, n        
        t = t * 10 + x
        z.set(str(t))

# fonctions liees aux boutons chiffres qui saisissent les valeurs desirees

def x(_nombre):
    nombre(_nombre)
        
#def x0():
#        nombre(0.)

#def x1():
#        nombre(1.)
        
#def x2():
#        nombre(2.)
                
#def x3():
#        nombre(3.)

#def x4():
#        nombre(4.)
        
#def x5():
#        nombre(5.)
        
#def x6():
#        nombre(6.)

#def x7():
#        nombre(7.)
        
#def x8():
#        nombre(8.)
        
#def x9():
#        nombre(9.)

# t1 correspond au deuxieme facteur de l'operation
# fonctions d'operation

def aplus():
        global y, t1, t, n
        y, t1, n = '+', t, 1
        t = 0
                
def amoins():
        global y, t1, t, n
        y, t1, n = '-', t, 1
        t = 0
                        
def afois():
        global y, t1, t, n
        y, t1, n = '*', t, 1
        t = 0

def adiv():
        global y, t1, t, n
        y, t1, n = '/', t, 1
        t = 0
                        
def aegal():
        global t, t1, n
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
        t1, n = 0, 1
        root.after(1500, clear)

def clear():
        global t, t1, n, z, y
        t, t1, n, y = 0, 0, 0, 0
        z.set(str('0'))
        
root = Tk.Tk()

btn1 = Button(root, text = "1", command = x(1))
btn1.grid(column = 0, row = 0)
btn2 = Button(root, text = "2", command = x2)
btn2.grid(column = 1, row = 0)
btn3 = Button(root, text = "3", command = x3)
btn3.grid(column = 2, row = 0)
btn4 = Button(root, text = "4", command = x4)
btn4.grid(column = 0, row = 1)
btn5 = Button(root, text = "5", command = x5)
btn5.grid(column = 1, row = 1)
btn6 = Button(root, text = "6", command = x6)
btn6.grid(column = 2, row = 1)
btn7 = Button(root, text = "7", command = x7)
btn7.grid(column = 0, row = 2)
btn8 = Button(root, text = "8", command = x8)
btn8.grid(column = 1, row = 2)
btn9 = Button(root, text = "9", command = x9)
btn9.grid(column = 2, row = 2)
btnc = Button(root, text = "C", command = clear)
btnc.grid(column = 0, row = 3)
btn0 = Button(root, text = "0", command = x0)
btn0.grid(column = 1, row = 3)
btnr = Button(root, text = "=", command = aegal)
btnr.grid(column = 2, row = 3)
btna = Button(root, text = "+", command = aplus)
btna.grid(column = 3, row = 0)
btns = Button(root, text = "-", command = amoins)
btns.grid(column = 3, row = 1)
btnm = Button(root, text = "*", command = afois)
btnm.grid(column = 3, row = 2)
btnd = Button(root, text = "/", command = adiv)
btnd.grid(column = 3, row = 3)

z = StringVar()
entree = Entry(root, textvariable = z)
entree.grid(column = 4, row = 3)
z.set("0.")

btnquit = Button(root, text = 'Quitter', command = root.destroy)
btnquit.grid(column = 4, row = 0)
root.mainloop() 