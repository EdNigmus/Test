# Chatgpt : les listes en python
# ==============================

# En Python, les listes sont des structures de données ordonnées, modifiables (mutables) et hétérogènes (elles peuvent
# contenir diffrents types d’objets). Elles sont très utilisées pour stocker et manipuler des ensembles de données.

# Créer une liste
# La liste ou tableau dans d'autre langage, est stockée dans une variable.
numb_lst = [1, 2, 3.52, 4]
str_lst = ["Laurent", "Avion", "Salade"]
bol_lst = [True, False]
mixte_lst = [52, "texte", True, 3.14159]

# Affiche une liste contenue de la variable "numb_lst" 
print (numb_lst)
print()

# Accéder et afficher un élément d'une liste 
# l'élément que l'on veut afficher ici est indiqué entre crochet. Se sera l'élément à l'index tant... que l'on veut afficher contenu dans une variable.
print(mixte_lst[3]) # affichera "3.14159"
print(mixte_lst[0]) # affichera le 1er élément de la liste, soit "52"
print(str_lst[-1]) # affichera le dernier élément de la liste, ici "Salade"



