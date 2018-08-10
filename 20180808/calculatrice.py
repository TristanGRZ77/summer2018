def saisie(_saisie):
    try:
        int(_saisie)
        return int(_saisie)
        return True
    except:
        return False

def operation(x,y, _saisie2):
    if (saisie(x) != False) & (saisie(y) != False) & (_saisie2 != False):
        if '+' in _saisie2:
            print(saisie(x) + saisie(y))
        if '-' in _saisie2:
            print(saisie(x) - saisie(y))
        if '*' in _saisie2:
            print(saisie(x) * saisie(y))
        if '/' in _saisie2:
            print(saisie(x) / saisie(y))   

fichier = open("calcul.txt", "r")
x = fichier.readline()
y = fichier.readline()
_saisie2 = fichier.readline()
fichier.close()

operation(x,y, _saisie2)
if (saisie(x) != True):
    fichier2 = open("erreur.txt", "w")
    fichier2.write("La valeur {0} n'est pas un nombre")
    fichier2.close()
if (saisie(y) != True):
    fichier2 = open("erreur.txt", "a")
    fichier2.write("La valeur {0} n'est pas un nombre")
    fichier2.close()
if (_saisie2 != True):
    fichier2 = open("erreur.txt", "a")
    fichier2.write("La valeur {0} n'est pas un signe")
    fichier2.close() 
