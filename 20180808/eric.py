import sys 
import re

global fichier_resultat

def saisie_int(message):
    try:
        valeur = message
        return int(valeur)
    except:
        return fichier_erreur.write('La valeur {} n\'est pas un nombre\n'.format(valeur))

def saisie_ope(message):
    if message in [ '+', '-', '/', '*' ]:
        return message
    else:
        return fichier_erreur.write('{} n\'est pas un operateur supporte\n'.format(message))

def operation(x, y, signe):
    if '+' in signe:
        return x + y

    if '*' in signe:
        return x * y

    if '/' in signe:
        return x / y

    if '-' in signe:
        return x - y

def lireFichier(fichier_donnees):
    global fichier_resultat
    global fichier_erreur
    fichier_resultat = open("resultat.txt", "w")
    fichier_erreur = open("erreur.txt", "w")

    with open(fichier_donnees, 'r') as content_file:
        for ligne_tmp in content_file:
            ligne(ligne_tmp)

    fichier_resultat.close()
    fichier_erreur.close()
        
def ligne(_ligne):
    seq = _ligne.split(";")
    x = saisie_int(seq[0])
    y = saisie_int(seq[1])
    z = saisie_ope(seq[2])
    
    try:
        w = operation(x, y, z)
        if '+' in z:
            fichier_resultat.write("La somme de {0} et de {1} vaut {2}\n".format(x, y, w))

        if '*' in z:
            fichier_resultat.write("Le produit de {0} et de {1} vaut {2}\n".format(x, y, w))

        if '-' in z:
            fichier_resultat.write("La difference entre {0} et {1} vaut {2}\n".format(x, y, w))

        if '/' in z:
            fichier_resultat.write("Le quotient de {0} par {1} vaut {2}\n".format(x, y, w))
    except:
        pass

if __name__ == '__main__':
    lireFichier("calcul.txt")