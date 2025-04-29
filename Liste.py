# Chatgpt : les listes en python
# ==============================

# En Python, les listes sont des structures de données ordonnées, modifiables (mutables) et hétérogènes (elles peuvent
# contenir diffrents types d’objets). Elles sont très utilisées pour stocker et manipuler des ensembles de données.

# CREER une liste
# La liste ou tableau dans d'autre langage, est stockée dans une variable. Elle est placée en tre crochets.
numb_lst = [1, 2, 3.52, 4]
str_lst = ["Laurent", "Avion", "Salade"]
bol_lst = [True, False]
mixte_lst = [52, "texte", True, 3.14159]

# AFFICHER une liste contenue de la variable "numb_lst" 
print("Afficher le contenu de 'numb_lst'")
print (numb_lst)
print()

# ACCEDER et afficher un élément d'une liste 
# l'élément que l'on veut afficher ici est indiqué entre crochet. Se sera l'élément à l'index tant... que l'on veut afficher contenu dans une variable.
print("Accéder et afficher un élément d'une liste")
print(mixte_lst[3]) # affichera "3.14159"
print(mixte_lst[0]) # affichera le 1er élément de la liste, soit "52"
print(str_lst[-1]) # affichera le dernier élément de la liste, ici "Salade"
print()

# MODIFIER un élément de la liste
# ici dans la liste contenue dans la variable "str_lst" à l'index 0 qui est le 1er élément, je le remplace par la string "Béatrice"
# L'index 0 est "Laurent" qui sera donc remplacé par "Béatrice"
print("Modifier une élément de la liste 'str_lst'")
str_lst[0] = "Béatrice" 
print(str_lst)
print()

# AJOUTER "append()" des éléments à une liste existante
print("Ajouter des éléments à la liste 'Tarte_pommes'")
Tarte_pommes = [] # Ici la liste est vide, mais existe. 
print(Tarte_pommes, "<- ici la liste est vide") 
# Pour ajouter un élément dans la liste on utilise la méthode 'append()' qui ajoute un élément à la fin de la liste.
Tarte_pommes.append("pommes")
print(Tarte_pommes)