# Chatgpt : les Tuples en python
# ==============================
# https://python.doctor/page-apprendre-tuples-tuple-python

# CREATION d'un Tuple, 2 syntaxes possibles.
# -------------------------------------------------
print("CREATION d'un Tuple avec plusieurs éléments")
tuple = (1, 2, 3)
print("- tuple = (1, 2, 3,)")
print("Création d'un Tuple avec un seul élément")
tuple1Ele = ("bateau",)
print("- tuple = ('bateau',)", "\n")

# ACCEDER aux éléments
# --------------------------------------------------
print("ACCEDER aux éléments")
tuple = ("a", "b", "c")
print("tuple = ('a', 'b', 'c')")
print("à l'index [0] il y a l'élément : ", tuple[0], "\n")

# ----------------------------------------------------
#               Opérations courantes
# ----------------------------------------------------

# LONGUEUR
print("LONGUEUR ou nombre d'élément via la méthode 'len()'")
# déclaration du tuple
tuple = ("aviation", "bar", "cake aux raisins")
# stocker le retour de la méthode len() dans un variable
nbrEleTuple = len(tuple)
print("Le nombre d'éléments est de : ", nbrEleTuple, "\n")

# CONCATENATION
print("CONCATENER plusieurs tuples. On utilise le symbole '+'" )
t1 = (1, 2)
print("tuple 1 : ", t1)
t2 = (3, 4)
print("tuple 2 : ", t2)
t3 = t1 + t2
print("Concaténation des 2 tuples : ", t3, "\n")

# REPETITION d'un tuple
print("REPETER une tuple via l'opérateur '*'")
t4 = t1 * 3
print("Répétition du tuple t1 : ", t4, "\n")

# APPARTENANCE
print("L'APPARTENANCE s'utilise via les 'in' ou 'not in'")
prenoms = ("biloutte", "albert", "toto")
print("biloutte" in prenoms, ": Il est vrais que le prénom existe")
print("biloutte" not in prenoms, ": Il est faux que le prénom n'existe pas", "\n")


