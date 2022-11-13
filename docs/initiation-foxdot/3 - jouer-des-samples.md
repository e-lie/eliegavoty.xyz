---
sidebar_position: 3
---

# 3 - Jouer des samples (batterie et autres sons)

FoxDot peut aussi être utilisé pour jouer et manipuler des samples (échantillons audio).

* Pour cela, il suffit d'utiliser `play` qui est un synthétiseur spécial.

* Le premier argument de play doit être une **chaîne de caractères** au lieu d'une liste de nombres comme vous le feriez pour tout autre synthétiseur.

* Chaque caractère représente un fichier audio différent, qui est stocké dans les sous-répertoires du dossier `FoxDot/snd/`.

Pour voir quel caractère correspond à quel fichier audio, exécutez:

`print(Samples)`

Maintenant jouons un sample avec le code suivant (la dur par défaut est 0.5, donc chaque caractère dure un demi beat)

`bd >> play("x")`

Un caractère fait référence à un son et le point ou l'espace est utilisé pour le silence, donc
vous pouvez étaler les sons dans le temps :

```python
bd >> play("o..o..x..")

hh >> play(" -")
```

Vous pouvez alterner un sample joué à chaque tour de boucle en utilisant des parenthèses (pour faire des `Patterns` imbriqués) : `d1 >> play("x-*(-=)")`

Par exemple le code suivant `"x-*(-=o)"` joue la même chose que `"x-*-x-*=x-*o"`

Ou encore `"(x=)(-v)o."` est identique à `"x-o.=vo."`

### Plusieurs coups sur un seul temps avec les crochets

Mettre des caractères entre crochets les jouera tous en l'espace d'un temps.
Et seront joués comme un seul caractère, pas simultanément, mais en succession rapide.

```python
d1 >> play("x-o[-o]")

d1 >> play("x-o[---]")

d1 >> play("x-o[-----]")

d1 >> play("x-o[--------------]")
```

... et peuvent être mis entre parenthèses comme s'ils étaient eux-mêmes un caractère.

```python
d1 >> play("x[--]o(=[-o])")
```

Vous pouvez combiner les parenthèses comme vous le souhaitez : les exemples suivants sont identiques

```python
d1 >> play("x-o(-[-o])")

d1 >> play("x-o[-(o )]")
```

Les accolades sélectionnent un échantillon sonore au hasard si vous voulez plus de variété.

`d1 >> play("x-o{-=[--][-o]}")`

Les crochets combinent les motifs à jouer simultanément.

```python
d1 >> play("<X   ><-   ><#   ><V   >")

d1 >> play("<X   >< -  ><  # ><   V>")
```

Chaque caractère est associé à un dossier de fichiers sonores et vous pouvez sélectionner différents échantillons en utilisant l'argument du mot clé `sample`.

```python
d1 >> play("(x[--])xu[--]")

d1 >> play("(x[--])xu[--]", sample=1)

d1 >> play("(x[--])xu[--]", sample=2)
```

On peut, changez l'échantillon pour chaque coup (sample peut utiliser des patterns/listes comme presque tous les autres paramètres). 

`d1 >> play("(x[--])xu[--]", sample=[1,2,3])`


### Petite listes des principaux samples de base de FoxDot

Kick (grosse caisse) `A v V x X W`

Snare/Rim (caisse claire) `D i I o O t u`

Hihat (charleston) `: = - a n N`

Clap/Snap `* h H`

Cymbale/Crash `/ # e E`

Tom/Tom-like `m M p P w`

Percussion `& + d f l r R y`

SoundFX `\ b F k L Q Y z Z`

Voix `1 2 3 4 ! < ? c C`

Bell `T` Cymbale Ride `~` Bruits `@ %` Maracas `s S`

Autre `$ ; B g G j J K q U`









