---
sidebar_position: 2
---

# 2 - Jouer des notes avec un synthétiseur

Pour jouer de la musique, FoxDot utilise des `Players`. On donne ensuite des instruction à ces players sur comment générer de la musique.

Au démarrage de FoxDot, tous les noms composés d'une lettre et d'un chiffre (0 à 9) comme `p1` ou `t7`, `a9` ou `k0` sont des utilisés (assignés) à des `Players`.

Pour créer notre premier son il nous faut donner quelque chose (un synthétiseur et une note) à jouer à l'un des players à l'aide de l'opérateur `>>`. Par exemple : 

`p1 >> piano(0)` ou encore `b3 >> blip(2)`.

Ici et dans tous les tutoriels suivant, dès qu'un exemple se présente copiez le dans votre éditeur FoxDot et essayez le en l'activant avec `Control + Entrée`. 

Il existe aussi `Alt + Entrée` qui active une seule ligne alors que `Control + Entrée` active tout un bloc de code sans ligne vide.

Essayez librement ces deux combinaisons sur les 3 lignes suivantes;

```python
p1 >> piano(0)
b3 >> blip(2)
p1.stop()
b3.stop()
```

Pour jouer plusieur notes on peut utiliser une liste de note :

`p1 >> blip([0, 1, 2])`


Mais plus largement, vous aurez besoin de spécifier ainsi tous les paramètres de jeu ce que vous voulez changer...

Comme la durée (longueur) des notes.

`p1 >> blip([0, 0, 0], dur=[1, 2, 3])`

Ou l'amplitude, le "volume" de chaque note.

`p1 >> blip([0, 0, 0], amp=[1, 2, 3])`

Si la deuxième liste, l'amplitude dans cet exemple, est trop longue, alors la première liste (le degré) fait simplement une boucle, et sont appariés avec les éléments restants de la deuxième liste (l'amplitude).

`p1 >> blip([0, 2, 4], amp=[1, 2, 3, 1, 5])`

Plus généralement, toutes les listes sont parcourues quelle que soit leur longueur

`p1 >> blip([0, 2, 4], dur=[1, 2], amp=[1, 2, 3, 1, 5])`

Les arguments peuvent être des entiers, des nombres à virgule (floats), des fractions, des listes, des tuples, ou un mélange

```python
p1 >> blip([0, 0, 0], dur=2)

p1 >> blip([0, 0, 0], dur=1.743)

p1 >> blip([0, 0, 0], dur=[0.25, 0.5, 0.75])

p1 >> blip([0, 0, 0], dur=[1/4, 1/2, 3/4])

p1 >> blip([0, 0, 0], dur=[1/4, 0.25, 3])
```

On peut également mettre des listes dans des listes. Les listes de valeurs sont parcourues au fur et à mesure que le joueur joue des notes.

`p1 >> blip([0, 0, 0], dur=[1, [2, .5], 4])`

La liste de durée suivante équivaut à :  1,2,3,1,.5,4

Si vous ne comprenez pas encore tout cela, ne vous inquiétez pas, vous en saurez plus sur les `Patterns` dans le tutoriel dédié plus tard.

Les valeurs entre parenthèses plutôt que crochets (on parle de tuples en langage python) sont utilisées simultanément c'est-à-dire que dans cet exemple p1 jouera 3 notes individuelles, puis un accord de 3 notes ensemble en même temps.

`p1 >> blip([0, 2, 4, (0, 2, 4)])`

Vous pouvez également attribuer directement des valeurs aux attributs des objets du lecteur.

`p1.oct = 5`

Pour voir tous les noms des attributs des joueurs vous pouvez exécuter

print(Player.get_attributes())

Nous en reparlerons plus tard dans le tutoriel sur les attributs du joueur.

Pour jouer plusieurs séquences de notes à la fois, il suffit de faire la même chose avec une autre séquence et un autre Player :

```python
p1 >> blip([0, 2, 3, 4], dur=1/2)

p2 >> pads([(0, 2, 4), (3, 5, 7)], dur=8)
```

Pour ne jouer que ce joueur, en mettant les autres en sourdine

`p1.solo()`

Et enlever la sourdine:

`p1.solo(0)`

<!-- Arrêtez (et non pas seulement coupez le son) des autres joueurs.
p1.only() -->

# Utilisez Ctrl+. pour tout arrêter (littéralement tout effacer de l'horloge d'exécution)
Clock.clear()