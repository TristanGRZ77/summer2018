import sys 

def saisie_int(message):
    try:
        valeur = input(message)
        return int(valeur)
    except:
        raise TypeError('La valeur {} n\'est pas un nombre\n'.format(valeur))

def saisie_ope(message):
    valeur = input(message).upper()
    if valeur in ['A', 'M']:
        return valeur

    if valeur == 'Q':
        sys.exit("Bye bye")

    raise ValueError('{} n\'est pas un operateur supporte\n'.format(valeur))

def operation(x, y, signe):
    if 'A' in signe:
        print(x + y)

    if 'M' in signe:
        print(x * y)


if __name__ == '__main__':
    while True:
        try:
            a = saisie_ope("Q pour arreter, A pour addition, M pour multiplication: ")
            operation(
                saisie_int("Saisir la premiere valeur: "),
                saisie_int("Saisir la seconde valeur: "),
                a
            )
        except TypeError as exception:
            print(exception)
        except ValueError as exception:
            print(exception)
