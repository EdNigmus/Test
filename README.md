# Langage : PYTHON

> ## Les TUPLES
https://python.doctor/page-apprendre-tuples-tuple-python

Les **tuples** ou **n-uplet** en français sont en Python des structures de données similaires aux listes, mais avec une différence clé : ils sont *immuables*, ce qui signifie qu'une fois qu'un tuple est créé, *il ne peut pas être modifié (on ne peut pas ajouter, supprimer ou changer ses éléments)*. C’est utile quand on veut s'assurer que les données restent constantes tout au long du programme.

- **Les `TUPLES`**
  
  - CREATION d'un **tuple**
    - à plusieurs éléments
    - avec 1 élément
  - ACCEDER AUX éléments
    
    ### Opérations courantes
    ---
    - On utilise la méthode `len()` pour connaitre la longueur ou taille du tuple, c'est à dire le nombre d'éléments contenu dans le tuple.
        ```
        tuple = ("avion", "Bar", "Cake aux raisins")
        print(len(tuple))

        retournera : 3
        ```

    - Concaténer (*mettre bout à bout*) plusieurs tuples, pour cela on utilise le symbole mathématique ou opérateur **`+`**
        ```
        t1 = (1, 2)
        t2 = (3, 4)
        t3 = t1 + t2

        t3 contiendra (1, 2, 3, 4) 
        ```

    - Répéter un tuple avec l'opérateur **`*`**
        ```
        t1 = (1, 2)
        t4 = t1 * 3

        t4 contiendra (1, 2, 1, 2, 1, 2 )
        ```

    - **Appartenance** : En Python, l'appartenance fait référence à la vérification de la présence d'un élément dans une collection (comme une liste, un dictionnaire, un ensemble, etc.). Cela se fait principalement à l’aide des opérateurs `in` et `not in`.
        ```
        Syntaxe : element in collection
                  element not in collection

        fruits = ("pomme", "poires", "cerise")
        print('pomme' in fruits) # retournera True 
        print('raisin' not in fruits)  # retournera True
        print('raisin' in fruits) # retournera False
        ``` 
    
