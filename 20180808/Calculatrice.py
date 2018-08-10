def saisiex(x):
    try:
        int(x)
        return int(x)
    except:
        return False

def saisiey(y):
    try:
        int(y)
        return int(y)
    except:
        return False

def saisie2(_saisie2):
    if '+' | '-' | '*' | '/' in _saisie2:
        return True
    else:
        return False

def operation(x,y, _saisie2):
    if (saisiex != False) & (saisiey != False) & (saisie2 != False):
        if '+' in _saisie2:
            z = (saisiex(x) + saisiey(y))
            fichier = open("resultat.txt", "w")
            fichier.write("La somme de {0} et de {1} vaut {2}".format(x,y, z))
            fichier.close()
        if '-' in _saisie2:
            z = (saisiex(x) - saisiey(y))          
            fichier = open("resultat.txt", "w")
            fichier.write("La difference entre {0} et {1} vaut {2}".format(x,y, z))
            fichier.close()
        if '*' in _saisie2:
            z = (saisiex(x) * saisiey(y))
            fichier = open("resultat.txt", "w")
            fichier.write("Le produit de {0} et de {1} vaut {2}".format(x,y, z))
            fichier.close()
        if '/' in _saisie2:
            z = (saisiex(x) / saisiey(y))
            fichier = open("resultat.txt", "w")
            fichier.write("Le quotient de {0} par {1} vaut {2}".format(x,y, z))
            fichier.close() 
    else:
        erreur()

def operation2(x,y, _saisie2):
    if (saisiex != False) & (saisiey != False) & (saisie2 != False):
        if '+' in _saisie2:
            z = (saisiex(x) + saisiey(y))
            fichier = open("resultat.txt", "a")
            fichier.write("La somme de {0} et de {1} vaut {2}".format(x,y, z))
            fichier.close()
        if '-' in _saisie2:
            z = (saisiex(x) - saisiey(y))          
            fichier = open("resultat.txt", "a")
            fichier.write("La difference entre {0} et {1} vaut {2}".format(x,y, z))
            fichier.close()
        if '*' in _saisie2:
            z = (saisiex(x) * saisiey(y))
            fichier = open("resultat.txt", "a")
            fichier.write("Le produit de {0} et de {1} vaut {2}".format(x,y, z))
            fichier.close()
        if '/' in _saisie2:
            z = (saisiex(x) / saisiey(y))
            fichier = open("resultat.txt", "a")
            fichier.write("Le quotient de {0} par {1} vaut {2}".format(x,y, z))
            fichier.close() 
    else:
        erreur()

def erreur():
    if (saisiex != True):
        fichier2 = open("erreur.txt", "w")
        fichier2.write("La valeur {0} n'est pas un nombre".format(x))
        fichier2.close()
    if (saisiey != True):
        fichier2 = open("erreur.txt", "a")
        fichier2.write("La valeur {0} n'est pas un nombre".format(y))
        fichier2.close()
    if (_saisie2 != True):
        fichier2 = open("erreur.txt", "a")
        fichier2.write("La valeur {0} n'est pas un signe".format(_saisie2))
        fichier2.close()

def variable(k):
    for i in k:
        x = k[0][0+3*i]
        y = k[0][1+3*i]
        _saisie2 = k[0][2+3*i]

def lireFichier(fichier):
    with open(fichier, 'r') as content_file:
        content = content_file.read()
        ligne(content)
        
def ligne(_ligne):
    seq = re.split(";|\n", _ligne)
    with open("calcul.txt", "r") as f:
        _ligne, seq = re.split(";|\n", _ligne), 3
        seq2 = zip(*[iter(_ligne)]*seq)
        if i == 0:
            x = seq2[0][0]
            y = seq2[0][1]
            _saisie2 = [0][2]
            operation(x,y, _saisie2)
        if i == 1:
            x = seq2[0][3]
            y = seq2[0][4]
            _saisie2 = [0][5]
            operation2(x,y, _saisie2)
        if i == 2:
            x = seq2[0][6]
            y = seq2[0][7]
            _saisie2 = [0][8]
            operation2(x,y, _saisie2)
        if i == 3:
            x = seq2[0][9]
            y = seq2[0][10]
            _saisie2 = [0][11]
            operation2(x,y, _saisie2)
        
#        x = seq2[0][0+3*i]
#        y = seq2[0][1+3*i]
#        _saisie2 = seq2[0][2+3*i]
            

import re
# i = 0
# while i < 10:
#     lireFichier("calcul.txt")
#     i += 1

#try:
#    operation(x,y, _saisie2)


