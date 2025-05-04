# Particularité 
# -----------------------------------------
# Le DEBALLAGE ou UNPACKING
# https://geekflare.com/fr/python-unpacking-operators/
'''
    En Python, le déballage (ou unpacking) fait référence au processus de distribution automatique 
    des éléments d'une séquence (comme une listes,tuples, dictionnaires, ensembles) dans des variables individuelles.
'''

import os
os.system("clear")
print("DEBALLAGE ou unpacking")
print("----------------------")
info_personne = ("phil", 56, True) 
# déballe le tuple en attribuant chaque élément à une des variables ci-dessous.
# L'ordre à son importance.
nom, age, actif = info_personne
print("-> ", nom, age, actif)
print("-> ",nom, "\n")

# DEBALLAGE via une fonction avec argument(s) (*args)
print("Deballage avec une fonction prenant des arguments")
print("-------------------------------------------------")
def addition(a, b, c):
    return a + b + c
nombres = [1, 2, 3]
# Appel de la fonction prenant comme paramètre une liste d'éléments qui sera déballés dans les paramètres de la fonction.
# On passe en paramètre de la fonction ou on déballe la liste "nombres" dans la fonction via " * "
print(" - Résultat du passage dans la fonction du déballage : ", addition(*nombres), "\n")

# Déballage partiel avec l'opérateur étoile *
print("")
# ici *milieu déballe la liste [2, 3, 4]
a, *milieu, b = [1, 2, 3, 4, 5]
print(a)
print(milieu)
print(b, "\n")

# Déballage de dictionnaire (clé/valeur **)
def personne(nom, age):
    print(f"Bonjour {nom}, vous avez {age} ans.", "\n")
# dictionnaire    
info = {
    "nom": "Alice", 
    "age": 30
}
# **info déballe le dictionnaire pour faire correspondre les clés aux paramètres nommés
saluer = personne(**info)
print(saluer)

first, *unused, last = [1, 2, 3, 5, 7]    
print(first)
print(last)
print(unused)

*string, = 'Géodésie'
print(string)

*number, = range(5)
print(number)


print("\n"*2)


# Impossible de modifier un élément d'un tuple car ils sont immuables
# l'instruction ci-dessous déclanche une erreur
info_personne[0] = "Tao"
print("\n")