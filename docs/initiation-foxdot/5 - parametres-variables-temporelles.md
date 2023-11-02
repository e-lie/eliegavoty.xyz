---
title: 5 - Paramètres et variables temporelles
sidebar_position: 4
---

## Paramètres des Players

Vous pouvez définir des variables en dehors d'un joueur

```python
pitches = P[0,1,2,3,4]
harmony = pitches + 2

print(pitches)
print(harmony)

p1 >> pluck(pitches)
p2 >> star(harmony)
```

Si vous définissez la durée de la seconde, cela pourrait ne pas avoir l'effet désiré.

```python
p1 >> pluck(pitches)
p2 >> star(harmony, dur=1/2)
```

Il est possible pour un objet joueur de suivre exactement ce que fait un autre joueur.
Pour qu'un joueur en suive un autre, il suffit d'utiliser la méthode follow :

```python
p1 >> pluck(pitches)

p2 >> star(dur=1/2).follow(p1) + 2
```

Vous pouvez également faire référence de manière explicite à des attributs tels que la hauteur ou la durée :

`p2 >> star(p1.pitch) + 2  # c'est la même chose que .follow(p1)`

Fonctionne aussi pour d'autres attributs

```python
p1 >> pluck(pitches)
p2 >> star(dur=p1.dur).follow(p1) + 2
```

Vous pouvez référencer et tester la valeur actuelle.
L'operateur `==` renvoie un 1 si elle est vraie et un 0 si elle est fausse.

```python
print(p1.degree)
print(p1.degree == 2)
```

Cela vous permet de faire des conditionnels comme

```python
p1 >> pluck([0,1,2,3], amp=(p1.degree==1))

p1 >> pluck([0,1,2,3], amp=(p1.degree>1))
```

Ou changez-le en un autre ampli en le multipliant par 4.

`p1 >> pluck([0,1,2,3], amp=(p1.degree==1)*4)`

Chaîner des conditionnels multiples

`p1 >> pluck([0,1,2,3], amp=(p1.degree==1)*4 + (p1.degree==2)*1)`

Ce qui est la même chose que

`p1 >> pluck([0,1,2,3], amp=p1.degree.map({1:4, 2:1}))`



## 3 variables temporelles

`var([0,3], 4)` crée une variable temporelle (TimeVar) dont la valeur évolue selon la Clock de FoxDot. Ici l'expression indique que la variable prendra la valeur 0 puis 3 en changeant tous les 4 temps (la durée).

par exemple `bb >> pluck(var([0,3], 4), dur=1)` jouera : 0,0,0,0,3,3,3,3,0 ...
et `bb >> pluck(var([0,3], 4), dur=2)` jouera : 0,0,3,3,0 ...

La durée peut peut aussi être une liste (un Pattern) : 

```python
a = var([0,3],[4,2]) # => 0,0,0,0,2,2,0,0,0,0,2,2,...
```

Voir une durée aléatoire:

```python
a = var([0,3], PRand(0,4))
```

When a TimeVar is used in a mathematical operation, the values it affects also become TimeVars
that change state when the original TimeVar changes state – this can even be used with patterns:

```python
a = var([0,3], 4)
print(int(Clock.now()), a + 5)   # When beat is 0, a is 5 => 5

print(int(Clock.now()), a + 5)   # When beat is 4, a is 8 => 8

b = PRange(4) + a
print(int(Clock.now()), b)   # After 8 beats, the value changes to 0
# >>> P[0, 1, 2, 3]

print(int(Clock.now()), b)   # After 12 beats, the value changes to 3
# >>> P[3, 4, 5, 6]

Les TimeVar sont très utiles pour créer des progressions harmoniques(chord progressions) dans vos Players !

```python
chords = var([0,4,5,3], 4)
b1 >> bass(chords, dur=PDur(3,8))
p1 >> pads(chords + (0,2), dur=PDur(7,16))
```

Vous pouvez additionner une TimeVar à un pattern à un Player.

```python
b1 >> bass(a, dur=PDur(3,8)) + var([0,1],[3,1])

b = a + var([0,10],8)

print(int(Clock.now()), (a, b))
```
<!-- 
Updating the values of one 'var' will update it everywhere else

```python
a.update([1,4], 8)

print(int(Clock.now()), (a, b))
```

Vars can be named ... And used later

```python
var.chords = var([0,4,5,4],4)

b1 >> pluck(var.chords)
```

Any players using the named var will be updated

```python
var.chords = var([0,1,5,3],4)
``` -->

### Variables continues `linvar`, `expvar`, `sinvar`

Pour décrire une valeur qui change graduellement dans le temps de façon continue on peut utiliser trois autres fonctions de variables:

`a = linvar([0,1],16)`

Evaluez le code suivant plusieurs fois pour constater le changement continu:

`print(int(Clock.now()), a)`

Comme toujours on peut utilisez cela pour n'importe quel paramètre d'un synthé.

`p1 >> blip([0,1,5], amp=a, dur=.25)`

Autre exemple: increase the high-pass filter cutoff over 32 beats

```
p1 >> play("x-o-", hpf=linvar([0,4000],[32,0]))
```

#### Other types include "sinvar" and "expvar"

```python
print("Linear:", linvar([0, 1], 8))
print("Sinusoidal:", sinvar([0, 1], 8))
print("Exponential:", expvar([0, 1], 8))
```

### Variables de pattern `Pvar`

Une 'Pvar' est une 'var' qui peuvent stocker et varier entre des Pattern (plutôt que des valeurs)

```python
pattern1 = P[0, 1, 2, 3]
pattern2 = P[4, 5, 6, 7]

print(var([pattern1, pattern2], 4))
```

Exemple musical:

```python
p1 >> pads(Pvar([P[0, 1, 2, 3], P[4, 5]], 8), dur=1/4)
```

On peut les utiliser pour changer la gamme (scale) par exemple tous les 16 beats.

`Scale.default = Pvar([Scale.major, Scale.minor],16)`

You even set the value to last forever once it is reached using a special value called "inf"

```python
x = var([0, 1, 2, 3], [4, 4, 4, inf])

print(x) # Keep pressing - it will eventually stop at 3
```


<!-- ###########################
# Offsetting the start time

# Another useful trick is offsetting the start time for the var. By
# default it is when the Clock time is 0 but you can specify a different
# value using the "start" keyword

print(linvar([0, 1], 8))
print(linvar([0, 1], 8, start=2))

# This can be combined with Clock.mod() to start a ramp at the start of the#
# next 32 beat cycle:

d1 >> play("x-o-", hpf=linvar([0,4000],[32,inf], start=Clock.mod(32))) -->