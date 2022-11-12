---
sidebar_position: 3
---


# 3 - Jouer des samples (batterie et autres sons)


FoxDot peut aussi être utilisé pour séquencer et manipuler des échantillons audio (samples).
* Pour cela, il suffit d'utiliser `play` qui est un synthétiseur spécial.
* Le premier argument de play doit être une chaîne de caractères au lieu d'une liste de nombres comme vous le feriez pour tout autre synthétiseur.
* Chaque caractère représente un fichier audio différent, qui est stocké dans les sous-répertoires du dossier `FoxDot/snd/`.

Pour voir quel caractère correspond à quel fichier audio, exécutez:

`print(Samples)`

Maintenant jouons un sample avec 

`bd >> play("x")`

Un caractère fait référence à un son et l'espace blanc est utilisé pour le silence, donc
vous pouvez étaler les sons dans le temps :

```python
bd >> play("o..o..x..")

hh >> play(".-")
```

Vous pouvez alterner sample joué à tour de boucle en utilisant des parenthèses rondes (pour faire des `Patterns` imbriqués).
Qui joue comme : `"x-o.=vo."`

`d1 >> play("(x=)(-v)o.")`

Ce qui suit est identique à `"x-*-x-*="`

`hh >> play("x-*(-=)")`

Mettre des caractères entre crochets les jouera tous en l'espace d'un temps.
Et seront joués comme un seul caractère, pas simultanément, mais en succession rapide.

```python
d1 >> play("x-o[-o]")

d1 >> play("x-o[---]")

d1 >> play("x-o[-----]")

d1 >> play("x-o[--------------]")
```

et peuvent être mis entre parenthèses comme s'ils étaient eux-mêmes un caractère.

```python
d1 >> play("x[--]o(=[-o])")
d1 >> play("x([--]x)o(=[-o])", dur=P[4/10, 3/10, 3/10]*2).stop()
```

Vous pouvez combiner les parenthèses comme vous le souhaitez : les modèles suivants sont identiques

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

Chaque personnage est associé à un dossier de fichiers sonores et vous pouvez sélectionner différents

échantillons en utilisant l'argument du mot clé "sample".

```python
d1 >> play("(x[--])xu[--]")

d1 >> play("(x[--])xu[--]", sample=1)

d1 >> play("(x[--])xu[--]", sample=2)
```

Changez l'échantillon pour chaque battement

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









