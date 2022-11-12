---
sidebar_position: 1
---

# 1 - Installer FoxDot


L'installation est officiellement décrite ici : https://foxdot.org/installation/#installing-foxdot

Voici une version traduite et détaillée de ce processus:

Downloads
Required

    Python
    SuperCollider 3.8 or higher
    Git

Optional

    SC3 plugins

Installing FoxDot

Follow the installation instructions for your downloads of Python and SuperCollider. When installing Python on Windows, click yes when asked if you want to add Python to your system path and yes if you want to install pip – this is used for automatically downloading/installing Python libraries such as FoxDot.

Install the latest version of FoxDot from the Python Package Index using pip from your command line (command prompt in Windows, terminal in MacOS and Linux) by executing:

$ pip install FoxDot

Please note, if you have Python 3 installed, the program might be called pip3, which helps discern between pip for Python 2 and 3.

Alternatively, you can build from the source on GitHub and keep up to date with the development version:

$ git clone https://github.com/Qirky/FoxDot.git
$ cd FoxDot
$ python setup.py install

Open SuperCollider and install the FoxDot Quark (this allows FoxDot to communicate with SuperCollider ) by entering the following in the editor and pressing Ctrl+Return; which "runs" a line of code:

Quarks.install("FoxDot")

Recompile the SuperCollider class library by going to Menu Language Recompile Class Library or pressing Ctrl+Shift+L.

If you can't install git on your machine, you can download a startup file, called foxdot.scd. Open this in SuperCollider and evaluate the code by pressing Ctrl+Return.
