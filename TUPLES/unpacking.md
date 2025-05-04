# Le Déballage ou unpacking

https://geekflare.com/fr/python-unpacking-operators/

- **le déballage**. En Python, le déballage (ou **unpacking**) fait référence au processus de distribution automatique des éléments d'une séquence (comme une liste ou un tuple) dans des variables individuelles.
  
    ```
      info_personne = ("phil", 56, True)
      nom, age, actif = info_personne
      print(nom, age, actif)

      Retournera : phil 56 True
    ```
    ![image](unpacking4.jpg)

> DEBALLER AVEC L'OPERATEUR *

- **Déballer** une liste avec l'opérateur `*`
  
  L’opérateur astérisque (`*`) est utilisé pour décompresser toutes les valeurs d’un itérable qui n’ont pas encore été assignées.

  Supposons que vous souhaitiez obtenir le premier et le dernier élément d’une liste sans utiliser d’index, nous pourrions le faire avec l’opérateur astérisque :

    ```
      first, *unused, last = [1, 2, 3, 5, 7]
      print(first)  # retournera : 1
      print(last)   # retournera : 7
      print(unused) # retournera [2, 3, 5]
    ```

  Toutes les valeurs non utilisées sont obtenues via l'opérateur `*`

- Pour déballer les valeurs d'un itérable en une seule variable, voir l'exemple suivant :
  Remarquer la virgule après variable, elle est nécessaire pour ne pas avoir d'erreur.
  
    ```
      *string, = 'Géodésie'
      print(string) # retournera : ['G', 'é', 'o', 'd', 'é', 's', 'i', 'e']

      *string, = 'Géodésie', 'droite-courbe'
      print(string) # retournera : ['Géodésie', 'droite-courbe']
    ```
  
- Un autre exemple serait l’utilisation de la *fonction* `range ()`, qui renvoie une séquence de nombres.

    ```
      *number, = range(5)
      print(number) # retournera : [0, 1, 2, 3, 4]
    ```