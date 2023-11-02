---
title: Installation de FoxDot/Renardo
sidebar_position: 1
---

FoxDot n'est pas en l'état simple à installer pour tout un chacun, il implique le bon fonctionnement de plusieurs sous parties liées au développement (Python, Git, Supercollider)
Renardo est un fork en cours d'élaboration qui vise à maintenir FoxDot et également à simplifier l'installation.

Expliquons d'abord un peu la structure de l'ensemble.

## Comprendre la structure de Renardo/FoxDot

![foxdot architecture diagram](/img/foxdot_workshop_3.jpg)

<!-- L'installation est officiellement décrite ici : https://foxdot.org/installation/#installing-foxdot -->

FoxDot/renardo est une librairie Python qui envoie des messages OSC (les notes à jouer) à SuperCollider qui se charge lui de générer le son en se connectant. Il faudra donc:

- Installer SuperCollider et vérifier qu'il fonctionne et sait se connecter à la carte son
- Installer un module dans SuperCollider qui permet à FoxDot de communiquer avec SC (nécessite git)
- Installer FoxDot/renardo comme une librairie Python.

## Installeur automatique sur Linux basé sur Ansible

- Installer `python-pip` ou `python3-pip` avec le gestionnaire de paquet
- Clonez l'installer suivant: `git clone https://github.com/e-lie/reanardo_reaper_installer renardo_installer && cd renardo_installer`

Ensuite au choix : installer le paquet `ansible` avec le gestionnaire de paquet ou créer un environnement virtuel python pour installer Ansible

## Installation manuelle (éléments)

### Installer Python

- https://python.org

### Installer FoxDot

FoxDot s'installe comme une librairie Python. Cependant le logiciel n'est plus maintenu par son créateur donc la version disponible PyPI et installable directement avec pip n'est pas compatible avec python 3.11 et supérieur. Une solution raisonnable est d'installer un fork disponible sur GitHub : https://github.com/TheNuSan/FoxDot:

    - `git clone https://github.com/TheNuSan/FoxDot`
    - `cd FoxDot && pip install -e .`

Renardo vise à remédier à cette situation en introduisant mais n'est pas encore prêt pour une installation facile. 

### Installer Git

- Souvent préinstallé sur Linux et MacOS. Sinon se référer au site officiel: https://git-scm.com/

Pour tester l'installatino taper `git status` dans un terminal et vérifiez que la commande existe

### Installer SuperCollider

- Sur la plupart des distributions Linux avec le gestionnaire de paquet (`sudo apt install supercollider sc3-plugins` / `sudo pacman -S supercollider sc3-plugins` par exemple)
- Sur Windows et MacOs avec de l'installer : https://supercollider.github.io/downloads

### Installation du module FoxDot dans Supercollider (nécessite git)

Ouvrez SuperCollider (souvent appelé `scide`) et installez le `Quark` FoxDot (cela permet à FoxDot de communiquer avec SuperCollider) en entrant la commande suivante dans l'éditeur puis en appuyant sur Ctrl+Entrée; ce qui "lance" la ligne de code:

`Quarks.install("FoxDot")`

Redémarrez l'éditeur SuperCollider et lancez la commande suivante : `FoxDot.start()`

Enfin pour lancez l'éditeur FoxDot, ouvrez un terminal/ invite de commande et lancez `python -m FoxDot`

## Démarrage manuel

- Sous Linux seulement et si vous utilisez jack (pas pipewire) :  démarrer le serveur Jack avec cadence ou qjackctl
- Démarrer SuperCollider IDE et lancez `FoxDot.start;` à évaluer avec CTRL+Enter
- Lancez FoxDot/renardo : `python3 -m FoxDot` ou `python -m FoxDot`