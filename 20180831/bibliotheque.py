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

#def lettre(x):
#    global t, n
#    u.set(str(t))

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

def changeMode():
    lblmode = _mode.get().rstrip()
    if lblmode == "Simple":
        _mode.set("Scientifique")
        btnresult.destroy()
        btnadd.destroy()
        btnsous.destroy()
        btnmult.destroy()
        btndiv.destroy()
        btnmodulo.destroy()
        ecranScientifique()

    if lblmode == "Scientifique":
        _mode.set("Simple")
        btnBaseHex.destroy()
        btnBaseBin.destroy()
        btnBinHex.destroy()
        btnBinBase.destroy()
        btnHexBin.destroy()
        btnHexBase.destroy()
        entree4.destroy()
        lblhex.destroy()
        ecran()

def conversion(_conversion):
    global t, n
    z.set("0")
    if _conversion == "baseToHex":
        z.set(hex(t).split("x")[-1])
    elif _conversion == "baseToBin":
        z.set(bin(t).split("b")[-1])
    elif _conversion == "binToHex":
        try:
            z.set((hex(int(str(t), 2))).split("x")[-1])
        except : 
            z.set("Non binaire")
    elif _conversion == "binToBase":
        try:
            z.set(int(str(t), 2))
        except : 
            z.set("Non binaire")
    elif _conversion == "hexToBin":
        try:
            z.set(bin(int(txthex.get(), 16)).split("b")[-1])
        except : 
            z.set("Non hexadecimal")
    elif _conversion == "hexToBase":
        try:
            z.set(int(txthex.get(), 16))
        except : 
            z.set("Non hexadecimal")

    t, n = 0, 1
    u.set("0")


def ecran__init__():
    global z, u, _mode
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
    btnclear = Button(root, text = "C", command = lambda : [clear(u), clear(z)])
    btnclear.grid(column = 0, row = 3)
    btn0 = Button(root, text = "0", command = lambda : x(0))
    btn0.grid(column = 1, row = 3)
    btnswitch = Button(root, text = "Mode", command = lambda : changeMode())
    btnswitch.grid(column = 4, row = 0, stick = "W")

    u = StringVar()
    entree2 = Entry(root, textvariable = u)
    entree2.grid(column = 4, row = 2, ipadx = 40)
    u.set("0")
    z = StringVar()
    entree = Entry(root, textvariable = z)
    entree.grid(column = 4, row = 3, ipadx = 40)
    z.set("0")
    _mode = StringVar()
    entree3 = Entry(root, textvariable = _mode)
    entree3.grid(column = 4, row = 0, stick = "E")
    _mode.set("Simple")

    btnquit = Button(root, text = 'Quitter', command = root.destroy)
    btnquit.grid(column = 4, row = 1, stick = "E")

def ecran():
    global btnresult, btnadd, btnsous, btnmult, btndiv, btnmodulo
    btnresult = Button(root, text = "=", command = aegal)
    btnresult.grid(column = 2, row = 3)
    btnadd = Button(root, text = "+", command = lambda : operation("+"))
    btnadd.grid(column = 3, row = 0)
    btnsous = Button(root, text = "-", command = lambda : operation("-"))
    btnsous.grid(column = 3, row = 1)
    btnmult = Button(root, text = "*", command = lambda : operation("*"))
    btnmult.grid(column = 3, row = 2)
    btndiv = Button(root, text = "/", command = lambda : operation("/"))
    btndiv.grid(column = 3, row = 3)
    btnmodulo = Button(root, text = "%", command = lambda : operation("%"))
    btnmodulo.grid(column = 4, row = 1, stick = "W")

def ecranScientifique():
    global btnBaseHex, btnBaseBin, btnBinHex, btnBinBase, btnHexBin, btnHexBase, entree4, txthex, lblhex

    btnBaseHex = Button(root, text = "Base -> Hex", command = lambda : conversion("baseToHex"))
    btnBaseHex.grid(column = 3, row = 0)
    btnBaseBin = Button(root, text = "Base -> Bin ", command = lambda : conversion("baseToBin"))
    btnBaseBin.grid(column = 3, row = 1)
    btnBinHex = Button(root, text = " Bin -> Hex  ", command = lambda : conversion("binToHex"))
    btnBinHex.grid(column = 3, row = 2)
    btnBinBase = Button(root, text = " Bin -> Base  ", command = lambda : conversion("binToBase"))
    btnBinBase.grid(column = 3, row = 3)
    btnHexBin = Button(root, text = " Hex -> Bin  ", command = lambda : conversion("hexToBin"))
    btnHexBin.grid(column = 3, row = 4)
    btnHexBase = Button(root, text = " Hex -> Base  ", command = lambda : conversion("hexToBase"))
    btnHexBase.grid(column = 3, row = 5)

    lblhex = Label(root, text = "Saisir la valeur en hexadecimale :" )
    lblhex.grid(column = 4, row = 4)
    txthex = StringVar()
    entree4 = Entry(root, textvariable = txthex)
    entree4.grid(column = 4, row = 5, ipadx = 40)
    txthex.set("0")