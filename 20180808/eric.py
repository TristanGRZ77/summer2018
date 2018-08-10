import os

try:
    from io import StringIO         # Python 3
except:
    from StringIO import StringIO   # Python 2

def saisie_int(message, output_fd=StringIO()):
    try:
        return int(message)
    except:
        error_message = 'La valeur {} n\'est pas un nombre\n'.format(message)
        output_fd.write(error_message)
        raise ValueError(error_message)

def saisie_ope(message, output_fd=StringIO()):
    if message in [ '+', '-', '/', '*' ]:
        return message
    else:
        error_message = '{} n\'est pas un operateur supporte\n'.format(message)
        output_fd.write(error_message)
        raise ValueError(error_message)

def operation(x, y, signe, output_fd=StringIO()):
    '''
    Render a simple operation
    Raises a ValueError if operator is unknown
    '''
    if '+' in signe:
        result = x + y
        output_fd.write("La somme de {0} et de {1} vaut {2}\n".format(x, y, result))
        return result

    if '*' in signe:
        result = x * y
        output_fd.write("Le produit de {0} et de {1} vaut {2}\n".format(x, y, result))
        return result

    if '/' in signe:
        result = int(x / y)
        output_fd.write("Le quotient de {0} par {1} vaut {2}\n".format(x, y, result))
        return result

    if '-' in signe:
        result = x - y
        output_fd.write("La difference entre {0} et {1} vaut {2}\n".format(x, y, result))
        return result

    raise ValueError

def lireFichier(data_file, error_file, result_file):
    fichier_donnees = os.path.abspath(data_file)
    error_file = os.path.abspath(error_file)
    result_file = os.path.abspath(result_file)

    with open(fichier_donnees, 'r') as content_file, \
         open(result_file, 'w') as result_file, \
         open(error_file, 'w') as error_file:
            for ligne_tmp in content_file:
                try:
                    ligne(
                        ligne_tmp,
                        error_output_fd=error_file,
                        result_output_fd=result_file
                    )
                except Exception:
                    pass

def line_to_operation(line, output_fd=StringIO()):
    '''
    Split a line into a list of 2 operands plus operator
    Output is a valid input for operation()
    Remove trailing chars if any and ignore anything after the third word
    '''
    field_1, field_2, field_3 = line.rstrip().split(';')[0:3]

    return [
        saisie_int(field_1, output_fd),
        saisie_int(field_2, output_fd),
        saisie_ope(field_3, output_fd),
    ]

def ligne(ligne, error_output_fd=StringIO(), result_output_fd=StringIO()):
    x, y, z = line_to_operation(ligne, output_fd=error_output_fd)
    return operation(x, y, z, output_fd=result_output_fd)

if __name__ == '__main__':
    lireFichier(
        "calcul.txt",
        'erreur.txt',
        'resultat.txt',
    )