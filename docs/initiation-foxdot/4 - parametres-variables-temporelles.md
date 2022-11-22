---
sidebar_position: 4
---

# 4 - Paramètres et variables temporelles

## 1 Paramètres des joueurs

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


## 2 Horloge (Clock) de FoxDot

Les boucles/patterns dans FoxDot sont bien entendu dépendants du temps qui s'écoule (comme toute musique). La `Clock` est l'objet responsable de compter l'écoulement des temps ou beats dans FoxDot. Tous les players (p1,a3,x7...) auxquels on assigne des synthés et patterns à jouer sont reliés à (ou programmés sur) cette horloge commune ce qui leur permet d'être tous synchronisés.

Il est intéressant de savoir manipuler un peu l'horloge pour :

- changer la vitesse de lecture ou bpm de la musique
- savoir désigner des points dans le futur pour déclencher des évènements musicaux plus tard
- Ajuster la synchronisation MIDI
- Savoir arrêter les joueurs ou utiliser plusieurs horloges désynchronisées (avancé)

### Changer le bpm

Par défaut le bpm de FoxDot est 120. Pour le changer on peut utiliser :

`Clock.bpm = 140`

### Désigner un point dans le futur

Utilisez `print()` sur `Clock.mod(4)`, `Clock.now()`, `Clock.mod(16)`.

Ces indications de moment dans le futur (en nombre de beat depuis l'allumage de FoxDot) servent principalement à controler les variables temporelles comme indiqué dans la partie suivante.

<!-- ### Programmer une fonction plus tard -->

<!-- On peut utiliser -->


## 3 variables temporelles


Generates the values: 0,0,0,0,3,3,3,3...

```python
a = var([0,3],4)            # Duration can be single value
print(int(Clock.now()), a)  # 'a' initally has a value of 0

print(int(Clock.now()), a)   # After 4 beats, the value changes to 3  => 4,3

print(int(Clock.now()), a)   # After another 4 beats, the value changes to 0  => 8, 0
```

Duration can also be a list : 

```python
a = var([0,3],[4,2])
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

Use 'var' with your Player objects to create chord progressions.

```python
a = var([0,4,5,3], 4)
b1 >> bass(a, dur=PDur(3,8))
p1 >> pads(a + (0,2), dur=PDur(7,16))
```

You can add a 'var' to a Player object or a var.

```python
b1 >> bass(a, dur=PDur(3,8)) + var([0,1],[3,1])

b = a + var([0,10],8)

print(int(Clock.now()), (a, b))
```

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
```

You can also use a 'linvar' that changes its values gradually over time
Change the value from 0 to 1 over 16 beats

`c = linvar([0,1],16)`

Run this multiple times to see the changes happening
`print(int(Clock.now()), c)`

Change the amp based off that linvar

`p1 >> pads(a, amp=c)`

a 'Pvar' is a 'var' that can store patterns (as opposed to say, integers)

```python
d = Pvar([P[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], P[0, 1, 2, 3, 4, 5, 4, 3, 2, 1]], 8)

print(int(Clock.now()), d)

p1 >> pads(a, amp=c, dur=1/4) + d
```

Change the scale every 16 beats

`Scale.default = Pvar([Scale.major, Scale.minor],16)`

You even set the value to last forever once it is reached using a special value called "inf"

```python
x = var([0, 1, 2, 3], [4, 4, 4, inf])

print(x) # Keep pressing - it will eventually stop at 3
```

### Other types of "var"

There are several sub-classes of "var" that return values between
the numbers specified. For example a "linvar" gradually change
values in a linear fashion:

```python
print(linvar([0,1],8)) # keep running to see the value change between 0 and 1
```

Example: increase the high-pass filter cutoff over 32 beats

```
p1 >> play("x-o-", hpf=linvar([0,4000],[32,0]))
```

#### Other types include "sinvar" and "expvar"

```python
print("Linear:", linvar([0, 1], 8))
print("Sinusoidal:", sinvar([0, 1], 8))
print("Exponential:", expvar([0, 1], 8))
```


### Pattern TimeVar

Sometimes we might want to store whole patterns within a var but
if we try to do so, they are automatically laced:

```python
pattern1 = P[0, 1, 2, 3]
pattern2 = P[4, 5, 6, 7]

print(var([pattern1, pattern2], 4))
```

To store whole patterns, you need to use a "Pvar" which does
not lace the values, but stores the patterns instead

```
print(Pvar([pattern1, pattern2], 4))

p1 >> pluck(Pvar([pattern1, pattern2], 4), dur=1/4)
```



###########################
# Offsetting the start time

# Another useful trick is offsetting the start time for the var. By
# default it is when the Clock time is 0 but you can specify a different
# value using the "start" keyword

print(linvar([0, 1], 8))
print(linvar([0, 1], 8, start=2))

# This can be combined with Clock.mod() to start a ramp at the start of the#
# next 32 beat cycle:

d1 >> play("x-o-", hpf=linvar([0,4000],[32,inf], start=Clock.mod(32)))