# Chatgpt : les dictionnaires en python
# ==============================
# https://python.doctor/page-apprendre-dictionnaire-python

# CREATION d'un dictionnaire, 2 syntaxes possibles.
# -------------------------------------------------
# 1er syntaxe avec des accolades :
print("CREATION D'un Dictionnaire", " / ", "dico = {'clé' : 'valeur'}")
mon_dico = {"nom": "Arthur", "âge": 30, "ville": "Paris"}

mon_dico = {
    # clé : valeur
    "nom" : "Arthur",
    "âge" : 30,
    "ville" : "Paris"
}
print(mon_dico)
# 2ième syntaxe avec la fonction "dict()"
autre_dico = dict(nom='Bob', âge=25, ville='Lyon')
print(autre_dico, "\n")

# ACCEDER aux valeurs
# -------------------------------------------------
# On accède aux valeurs d'un dictionnaire en utilisant la clé correspondante :
print("ACCERDER aux valeurs"," / ", "dico['valeur']")
print(mon_dico["nom"], " et ", mon_dico["âge"], "\n") # la clé "nom" permet d'accèder à la valeur "Arthur"

# AJOUTER ou MODIFIER des éléments
# -------------------------------------------------
# ajout d'un nouvel élément
print("AJOUTER un nouvel élément (clé/valeur)", " / ", "dico['profession' = 'Developpeur']")
print("Dictionnaire d'origine -> ", mon_dico)
mon_dico["profession"] = "Développeur"
print("Ajout d'un élément     -> ", mon_dico, "\n")

# MODIFIER une valeur existante
# -------------------------------------------------
# Il est possible de modifier la valeur d'une clé, par exemple modifions l'âge.
print("MODIFIER la valeur d'une clé, par exemple l'âge.")
print("Age d'origine -> ", mon_dico["âge"])
mon_dico["âge"] = 42
print("Age modifié   -> ", mon_dico["âge"], "\n")

# SUPPRIMER des éléments 2 façons de faire 
# -------------------------------------------------
# 1/ avec l'instruction "del"
print("SUPPRIMER des éléments avec l'instruction `del'")
print("Dictionnaire d'origine -> ", mon_dico)
del mon_dico["ville"]
print("Dictionnaire modifier -> ", mon_dico, "\n")
# 2/ Récupérer la valeur et supprimer sa clé avec la méthode "pop()" 
print("SUPPRIMER des éléments avec la méthode `pop()`")
print("Dictionnaire à l'instant T       -> ", mon_dico)
age = mon_dico.pop("âge")
print("Valeur de la clé 'âge' récupérée -> ", age)
print("Nouveau dictionnaire             -> ", mon_dico, "\n") 

# PARCOURIR un dictionnaire
# -------------------------------------------------
# On va pouvoir parcourir un dictionnaire grace à une boucle "for/in"
print("PARCOURRIR et afficher le contenu du dictionnaire 'film'")
film = {
    "titre"  : "Rocky",
    "annee"  : 1976,
    "spport" : "DVD",
    "durée"  : "120mn",
    "numero" : 28,
    "realisateur" : "John G.Avildsen",
    "distributeur" : "United Artists"    
}
# Création liste "Acteurs"
Acteurs = ['Sylvester Stallone', 'Talia Shire', 'Burt Young', 'Carl Weathers']  
# on ajoute le contenu de la liste "Acteurs" dans le dictionnaire "films" à la clé "acteurs"
film["acteurs"] = Acteurs
# dans la boucle on dit, que pour chaque clé et valeur dans la liste de tuples(clé,valeur)
# on affiche la clé : valeur
for clé, valeur in film.items():
    print(clé, ":", valeur)
print()   
print("Affiche l'élément [0] à la clé ['acteurs'] dans le dictionnaire 'films'")
# Affiche l'élément [1] à la clé ["acteur"] dans le dictionnaire "film"     
print(film["acteurs"][1], "\n")

#--------------------------------------------------------------
#                       METHODES COURANTES
#--------------------------------------------------------------
    
print("AUTRES METHODES")
print("---------------")
# ne retourne que les clés du dictionnaires "film"
print("- La méthode keys()")
print(" ", film.keys(), "\n")
# ne retourne que les valeurs du dictionnaires "film"
print("- La méthode values()")
print(" ", film.values(), "\n")
# retourne une liste de tuple (clé,valeur)
print("- La méthode items()")
print(" ", film.items(), "\n")
# ici le 1er paramètre "acteurs" qui est une clé du dictionnaire "film" retournera sa valeur.
# Si se premier paramètrre n'existe pas, alors c'est le 2iè paramètre qui sera retourné "Inconnue".
print("- La méthode get()")
print(" ", film.get("acteurs","Inconnue"), "\n")

