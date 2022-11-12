---
sidebar_position: 1
---

# 1 - Installer FoxDot


L'installation est officiellement décrite ici : https://foxdot.org/installation/#installing-foxdot

Voici une version traduite et détaillée de ce processus:

A télécharger:

* Python
* SuperCollider
* Git

Suivez les instructions d'istallation pour télécharger et installer Python et SuperCollider. 

Pour installer la dernière version de FoxDot ouvrez un terminal (command prompt sur Windows, terminal sur MacOS and Linux) puis executez:

`$ pip3 install FoxDot`

<!-- Please note, if you have Python 3 installed, the program might be called pip3, which helps discern between pip for Python 2 and 3. -->

<!-- Alternatively, you can build from the source on GitHub and keep up to date with the development version:

$ git clone https://github.com/Qirky/FoxDot.git
$ cd FoxDot
$ python setup.py install -->

Ouvrez SuperCollider (souvent appelé `scide`) et installer le `Quark` FoxDot (cela permet à FoxDot de communiquer avec SuperCollider) en entrant la commande suivante dans l'éditeur puis en appuyant sur Ctrl+Entrée; ce qui "lance" la ligne de code:

`Quarks.install("FoxDot")`

Redémarrez l'éditeur SuperCollider et lancez la commande suivant `FoxDot.start()`

Enfin pour lancez l'éditeur FoxDot, ouvrez un terminal/ invite de commande et lancez `python3 -m FoxDot`
