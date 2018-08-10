def lireFichier(fichier):
    with open(fichier, 'r') as content_file:
        content = content_file.read()
        ligne(content)
        
def ligne(_ligne):
    seq = re.split(";|\n", _ligne)
    with open("calcul.txt", "r") as f:
        _ligne, seq = re.split(";|\n", _ligne), 3
        seq2 = zip(*[iter(_ligne)]*seq)
        print seq2

import re
lireFichier("calcul.txt")
