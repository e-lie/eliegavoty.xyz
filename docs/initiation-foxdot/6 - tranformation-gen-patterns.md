---
sidebar_position: 5
---

# 5 - Transformations et générateurs de Patterns














Les Pattern sont accompagnés de plusieurs méthodes permettant de manipuler le contenu.

`help(Pattern)`

Pattern standard : `print(P[:8])`

Mélanger le Pattern en le rendant aléatoire : `print(P[:8].shuffle())`

Ajouter un Pattern inversé au motif : `print(P[:8].palindrome())`

Décaler le Pattern de n (par défaut 1):

```python
print(P[:8].rotate())
print(P[:8].rotate(3))
print(P[:8].rotate(-3))
```

Prend le Pattern et l'ajoute autant de fois que nécessaire pour atteindre le nombre n d'éléments.

```python
print(P[:8].stretch(12))
print(P[:8].stretch(20))
```

Inverse un Pattern : `print(P[:8].reverse())`

Boucle un Pattern n nombre de fois : `print(P[:8].loop(2))`

Ajouter un décalage : `print(P[:8].offadd(5))`

Ajouter un décalage multiplié : `print(P[:8].offmul(5))`

Stutter - Répéter chaque élément n fois : `print(P[:8].stutter(5))`

Amen - Fusionne et lace les deux premiers et derniers éléments de telle sorte qu'une
le pattern de batterie `"x-o-"` devienne `"(x[xo])-o([-o]-)"` et imite le rythme du fameux "amen break".

```python
d1 >> play(P["x-o-"].amen())
print(P[:8].amen())
```

Bubble - Fusionne et lace les deux premiers et derniers éléments de telle sorte que la
le pattern de batterie `"x-o-"` devienne `"(x[xo])-o([-o]-)"`.

```python
d1 >> play(P["x-o-"].bubble())
print(P[:8].bubble())
```