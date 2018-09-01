from Tkinter import*
import Tkinter as Tk
from math import *

# t correspond au chiffre saisi
# y correspond a l'operateur utilise 
# n correspond au nombre de valeurs que compose un facteur

root = Tk.Tk()
#t, y, n = 0, 0, 1
effacer_resultat = 0
resultat_calcul = 0
# zone de stockage de la premiere operande
operande0 = 0
# zone de stockage de la seconde operande
operande1 = 0
# string temporaire de stockage des operandes
_operande = ""
# indicateur operande en cours
switch_operande = 0
signe = ""

# fonction liee aux boutons chiffres qui saisissent les valeurs desirees

# utliser les focntions de concatenation de string
# lorsque un signe est saisi, convertir en entier puis stocker la variable
# pareillement pour le second operande.
# lorsaue la touche egal est appuyer, les operations arithmetiques sont effectuees

def f_x(_nombre):
    global signe, _operande
    _operande = _operande + str(_nombre)
    if signe == "":
        _label_calcul.set(_operande)
        _label_resultat.set("")
    else:
        _label_calcul.set(label_calcul.cget("text") + str(_nombre))

def operation(_signe):
    global operande0, _operande, signe
    signe = _signe
    operande0 = int(_operande)
    _label_calcul.set(_operande + str(_signe))
    _operande = ""
        
def aegal():
    global signe, operande0, operande1, _operande
    operande1 = int(_operande)
    if signe == '+':
        resultat_operation = operande0 + operande1
    elif signe == '-':
        resultat_operation = operande0 - operande1
    elif signe == '*':
        resultat_operation = operande0 * operande1
    elif signe == '/':
        resultat_operation = operande0 / operande1
    elif signe == '%':
        resultat_operation = operande0 % operande1

    _label_resultat.set(str(resultat_operation))
    signe = ""
    _operande = ""

def clear(_clear):
    global operande0, operande1, _label_resultat, _label_calcul
    operande0, operande1 = 0, 0
    _label_resultat.set("")
    _label_calcul.set("")

def changeMode():
    lblmode = btnswitch.cget("text").rstrip()
    _label_resultat.set("")
    _label_calcul.set("")
    if lblmode == "Sim":
        btnswitch.config(text="Sci")
        btnresult.destroy()
        btnadd.destroy()
        btnsous.destroy()
        btnmult.destroy()
        btndiv.destroy()
        btnmodulo.destroy()
        ecranScientifique()

    if lblmode == "Sci":
        btnswitch.config(text="Sim")
        btnBaseHex.destroy()
        btnBaseBin.destroy()
        btnBinHex.destroy()
        btnBinBase.destroy()
        btnHexBin.destroy()
        btnHexBase.destroy()
        btnA.destroy()
        btnB.destroy()
        btnC.destroy()
        btnD.destroy()
        btnE.destroy()
        btnF.destroy()
        ecran()

def conversion(_conversion):
    global _operande
    _label_resultat.set("0")
    if _conversion == "baseToHex":
        try:
            resultat_operation = hex(int(_operande)).split("x")[-1]
            _label_resultat.set(resultat_operation)
        except:
            _label_resultat.set("Non decimal")

    elif _conversion == "baseToBin":
        try:
            resultat_operation = bin(int(_operande)).split("b")[-1]
            _label_resultat.set(resultat_operation)
        except:
            _label_resultat.set("Non decimal")

    elif _conversion == "binToHex":
        try:
            resultat_operation = hex(int(str(_operande), 2)).split("x")[-1]
            _label_resultat.set(resultat_operation)
        except : 
            _label_resultat.set("Non binaire")

    elif _conversion == "binToBase":
        try:
            resultat_operation = int(str(_operande), 2)
            _label_resultat.set(resultat_operation)
        except : 
            _label_resultat.set("Non binaire")

    elif _conversion == "hexToBin":
        try:
            resultat_operation = bin(int(_operande, 16)).split("b")[-1]
            _label_resultat.set(resultat_operation)
        except : 
            _label_resultat.set("Non hexadecimal")

    elif _conversion == "hexToBase":
        try:
            resultat_operation = int(_operande, 16)
            _label_resultat.set(resultat_operation)
        except : 
            _label_resultat.set("Non hexadecimal")

    signe = ""

def ecran__init__():
    global _label_calcul, label_calcul, _label_resultat, label_resultat, btnswitch, effacer_resultat

    root.columnconfigure(4, pad = 100)
    btn1 = Button(root, text = "1", command = lambda : f_x(1))
    btn1.grid(column = 0, row = 0)
    btn2 = Button(root, text = "2", command = lambda : f_x(2))
    btn2.grid(column = 1, row = 0)
    btn3 = Button(root, text = "3", command = lambda : f_x(3))
    btn3.grid(column = 2, row = 0)
    btn4 = Button(root, text = "4", command = lambda : f_x(4))
    btn4.grid(column = 0, row = 1)
    btn5 = Button(root, text = "5", command = lambda : f_x(5))
    btn5.grid(column = 1, row = 1)
    btn6 = Button(root, text = "6", command = lambda : f_x(6))
    btn6.grid(column = 2, row = 1)
    btn7 = Button(root, text = "7", command = lambda : f_x(7))
    btn7.grid(column = 0, row = 2)
    btn8 = Button(root, text = "8", command = lambda : f_x(8))
    btn8.grid(column = 1, row = 2)
    btn9 = Button(root, text = "9", command = lambda : f_x(9))
    btn9.grid(column = 2, row = 2)
    btnclear = Button(root, text = "C", command = lambda : [_label_resultat.set(""), _label_calcul.set("")])
    btnclear.grid(column = 0, row = 3)
    btn0 = Button(root, text = "0", command = lambda : f_x(0))
    btn0.grid(column = 1, row = 3)
    btnswitch = Button(root, text = "Sim", command = lambda : changeMode())
    btnswitch.grid(column = 4, row = 0, stick = "W")

    _label_resultat = StringVar()
    label_resultat = Tk.Label(textvariable=_label_resultat)
    label_resultat.grid(column = 4, row = 3, ipadx = 40)
    _label_resultat.set("")

    _label_calcul = StringVar()
    label_calcul = Tk.Label(textvariable=_label_calcul)
    label_calcul.grid(column = 4, row = 2, ipadx = 40)
    _label_calcul.set("")

    btnquit = Button(root, text = 'Quitter', command = root.destroy)
    btnquit.grid(column = 4, row = 0)
    effacer_resultat = 0

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
    global btnBaseHex, btnBaseBin, btnBinHex, btnBinBase, btnHexBin, btnHexBase, btnA, btnB, btnC, btnD, btnE, btnF

    btnA = Button(root, text = "a", command = lambda : f_x("a"))
    btnA.grid(column = 0, row = 4)
    btnB = Button(root, text = "b", command = lambda : f_x("b"))
    btnB.grid(column = 1, row = 4)
    btnC = Button(root, text = "c", command = lambda : f_x("c"))
    btnC.grid(column = 2, row = 4)
    btnD = Button(root, text = "d", command = lambda : f_x("d"))
    btnD.grid(column = 0, row = 5)
    btnE = Button(root, text = "e", command = lambda : f_x("e"))
    btnE.grid(column = 1, row = 5)
    btnF = Button(root, text = "f", command = lambda : f_x("f"))
    btnF.grid(column = 2, row = 5)
    btnBaseHex = Button(root, text = "Base -> Hex", command = lambda : conversion("baseToHex"))
    btnBaseHex.grid(column = 3, row = 0)
    btnBaseBin = Button(root, text = "Base -> Bin ", command = lambda : conversion("baseToBin"))
    btnBaseBin.grid(column = 3, row = 1)
    btnBinHex = Button(root, text = " Bin -> Hex  ", command = lambda : conversion("binToHex"))
    btnBinHex.grid(column = 3, row = 2)
    btnBinBase = Button(root, text = " Bin -> Base ", command = lambda : conversion("binToBase"))
    btnBinBase.grid(column = 3, row = 3)
    btnHexBin = Button(root, text = " Hex -> Bin  ", command = lambda : conversion("hexToBin"))
    btnHexBin.grid(column = 3, row = 4)
    btnHexBase = Button(root, text = " Hex -> Base ", command = lambda : conversion("hexToBase"))
    btnHexBase.grid(column = 3, row = 5)