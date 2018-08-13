class operation(object):

    def __init__(self):
        self._valeurx = 1
        self._valeury = 2

    def _get_valeurx(self):
        print("Valeur de x : ")
        return self._valeurx

    def _set_valeurx(self, x):
        print("Nouvelle valeur de x : {}".format(x))
        self._valeurx = x

    def _get_valeury(self):
        print("Valeur de y : ")
        return self._valeury

    def _set_valeury(self, y):
        print("Nouvelle valeur de y : {}".format(y))
        self._valeury = y

    def _get_operateur(self):
        print("Operateur : ")
        return self._operateur

    def _set_operateur(self, z):
        print("Nouvel operateur : {}".format(z))
        self._operateur = z

    valeurx = property(_get_valeurx, _set_valeurx)
    valeury = property(_get_valeury, _set_valeury)
    operateur = property(_get_operateur, _set_operateur)

a = operation()
a.valeurx = raw_input("Saisir la nouvelle valeur de x : ")
a.valeury = raw_input("Saisir la nouvelle valeur de y : ")
a.operateur = raw_input("Saisir l'operateur : ")





#= "Addition"
#        self.s = "Soustraction"
#        self.m = "Multiplication"
#        self.d = "Division"
