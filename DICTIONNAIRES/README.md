# Langage : PYTHON

> ## Les DICTIONNAIRES
Les dictionnaires en Python sont des structures de données qui permettent de stocker des paires de clés et de valeurs. Chaque élément d'un dictionnaire est composé d'une clé unique et d'une valeur associée à cette clé. Ils sont particulièrement utiles lorsqu'on a besoin de récupérer des données rapidement à l'aide d'une clé, plutôt qu'en utilisant un indice comme dans les listes.

Dans d'autre langages on parlerait de tableau associatif.

#### SOMMAIRE :
---
- CREATION d'un dictionnaire
  - 2 façons possible : classique ou avec une fonction
    
- ACCEDER aux valeurs
- AJOUTER un élément au dictionnaire
- MODIFICATION d'une valeur par sa clé
- SUPPRIMER des éléments 2 façons de faire 
  - avec l'instruction **del**
  - avec la méthode `pop()`
- PARCOURIR un dictionnaire
  - Création liste "Acteurs" 
  - Ajout de la liste dans le dictionnaire "film" à la clé "acteurs"
  - Utilisation de la boucle **for-in** pour passer sur chaque item clé/valeur du dictionnaire
  - Affichage 
  - Affichage d'une élément de la liste à la clé "acteurs" dans le dictionnaire "film"
  
  #### METHODE Courantes
  ---
  - La méthode `keys()` renvoi les clés du dictionnaire
  
    ``` 
      mon_dico {"A":"1", "B":"2", "C":"3"}
      print(mon_dico.keyS()) 

      # retournera : dict_keys(['A', 'B', 'C'])
    ```
  - La méthode `values()` renvoi les valeurs du dictionnaire
  
    ```
      mon_dico {"A":"1", "B":"2", "C":"3"}
      print(mon_dico.values()) 

      # retournera : dict_values(['1', '2', '3'])
    ```

  - La méthode `items()` renvoi une liste de tuples (clé,valeur)

    ```
      mon_dico {"A":"1", "B":"2", "C":"3"}
      print(mon_dico.items()) 

      # retournera : dict_items([('A','1'), ('B','2'), ('C','3')])
    ```

  - La méthode `get()` permet de récupérer une valeur sans générer d'erreur si la clé n'existe pas.
    Elle renvoie **None** ou une valeur par défaut si précisée.

    ```
      mon_dico {"A":"1", "B":"2", "C":"3"}
      print(mon_dico.get("B","Cette clé n'existe pas"))

      # retournera : 2, car la clé existe. Sinon elle afficherait "Cette clé n'existe pas"
    ```
     



