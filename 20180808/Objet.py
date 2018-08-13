class operation(object):

    def __init__(self):
        self._valeurx = 1
        self._valeury = 2

    def _get_valeurx(self):
        return self._valeurx

    def _set_valeurx(self, x):
        print("Nouvelle valeur de x : {}".format(x))
        self._valeurx = x

    def _get_valeury(self):
        return self._valeury

    def _set_valeury(self, y):
        print("Nouvelle valeur de y : {}".format(y))
        self._valeury = y

    def _get_operateur(self):
        return self._operateur

    def _set_operateur(self, z):
        print("Nouvel operateur : {}".format(z))
        self._operateur = z

    valeurx = property(_get_valeurx, _set_valeurx)
    valeury = property(_get_valeury, _set_valeury)
    operateur = property(_get_operateur, _set_operateur)

import sys 
import re

def saisie_int(message):
    try:
        valeur = message
        return int(valeur)
    except:
        return ("La valeur {} n'est pas un nombre".format(valeur))
        pass

def saisie_ope(message):
    if message in [ '+', '-', '/', '*' ]:
        return message
    else:
        return ("La valeur {} n'est pas un operateur supporte".format(message))
        pass

def calcul(x, y, z):
    if '+' in z:
        try:
            print x + y
        except:
            print("Operation impossible")

    if '*' in z:
        try:
            print x * y
        except:
            print("Operation impossible")

    if '/' in z:
        try:
            print x / y
        except:
            print("Operation impossible")

    if '-' in z:
        try:
            print x - y
        except:
            print("Operation impossible")

a = operation()

a.valeurx = saisie_int(raw_input("Saisir la nouvelle valeur de x : "))
a.valeury = saisie_int(raw_input("Saisir la nouvelle valeur de y : "))
a.operateur = saisie_ope(raw_input("Saisir l'operateur : "))

x = a.valeurx 
y = a.valeury
z = a.operateur 

calcul(x, y, z)