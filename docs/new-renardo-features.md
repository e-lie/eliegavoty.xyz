---
sidebar_position: 1
title: Extending the "scope" of livecoding in Renardo 
---

[Renardo](https://renardo.org) is a fork of FoxDot that I started in january 2024. The motivation is first to maintain this nice piece of software I love, and I hope the enthusiastic FoxDot community is happy about it.
The software is still in a refactoring process to make it more modular, with simpler code, while keeping most FoxDot features. I'm not moving as fast as I'd like and the user experience is not at it's best. It should be simpler to install for newcomers and more stable : I'm struggling with that part but I got plans for it, just time consumming.

The second motivation was to incorporate new features I have been thinking about/hacking inside FoxDot when I started livecoding and that's the topic of this page.
To sump this up, Renardo extends (/ will extend) the livecoding possibilities of FoxDot in 3 directions in different areas of computer music :

- Livecoding a DAW completely (Reaper in this case) from the python runtime/clock.
- Reopen the possibilities of SuperCollider sound synthesis from Renardo. (this already exists in FoxDot through a Python/SClang binding but looked limited to me and hard to use)
- Leverage more metaprogramming possibilities ( (live) writing code that triggers/automate livecoding in many ways). Metaprogramming also exists in FoxDot in a simple form but the possibilities are much larger.

Of course, all of this is already possible by hacking around. But it seems that one of the significant idea behing livecoding software and algorave movement is also to make generative possibilities accessible by creating a standard/stable/shared way to leverage the magic and document it for anyone to enjoy.

Those three directions are not directly about the core FoxDot langage and it's expressivity. I'd like to find the time to explore that too, but from the beginning I feel fine with the already pretty wide generative possibilities of FoxDot, and to me it was mostly lacking some fine control over the sound and the scheduling possibilities for performances.

Let's add some details.

### Livecoding Reaper DAW for mixing and synthesizers

Reaper, despite not beeing free nor open source, is a community oriented software, and a very powerful one for (live) mixing/mastering music (even multichannel). It is multiplateform and pretty hackable, especially using it's API. Based on this and the [reapy](https://pypi.org/project/python-reapy/) python library, I added a (still experimental) functionnality to :

- instanciate any plugin inside Reaper
- route MIDI notes automatically
- to control dynamically any plugin parameter without manual mapping

This mode is for now only working on Linux, not installable without advanced knowledge and stills require some initial manual work on the reaper side for the project to have the right setup, but I plan to stabilize and automate it fully.

This extension of possibilities is meaningful to me in the way it could fill a gap between practices and knowledge from mainstream computer music (using tracks and widely used plugins for mixing and sound synthesis) and the strenghts of livecoding (spontaneity, generative patterns, opensource community).

This leads to the somehow political question : is inviting the "blackbox plugin" industry as first class citizen into a open and free ecosystem a good idea ? That's a real issue that should be accessed along the way. But I also feel that since a lot of people use at some point commercial plugins to achieve a musical result, it would be nice to have them patternable and visible in the code too.

This is a demo video showing reaper livecoding with the nice opensource Vital synth:

<video width="640" height="360" controls>
  <source src="https://nx34151.your-storageshare.de/s/5JrrSjWjWWi3XsB/download/2024-09-29%2020-17-30.mp4"/>
</video>


### Livecoding SCLang from the Renardo runtime

FoxDot is based on SynthDefs dynamically instanciated into supercollider to send them notes and parameters from python runtime. But the sound synthesis code is hidden inside the library folder and not really meant for live editing. This makes customizing the sound precisely, a mysterious and somehow daunting task.

I felt it was a easy to implement and potentially very interesting feature to be able to livecode SCLang and Python at the same time even from the same file. Also one of the Renardo refactoring consist of externalizing the samples and synthdefs in the user config folder and providing a standard/cleaner way of downloading and sharing those "assets".

This feature will be usable in the next Renardo release when I find the time to publish it (://).

demo video:
<video width="640" height="360" controls>
  <source src="https://nx34151.your-storageshare.de/s/KKNan5ekYfaQ437/download/live%20synthdef%20demo.mp4"/>
</video>


### Metaprogramming

This is more a feature project than something existing even if I already use some similar mechanism for recording coded tracks or performance purposes.

Metaprogramming, writing code about the code and its objects, is pretty common in Python. Moreover, FoxDot somehow uses a metaprogramming pattern at it's core since the Python runtime gets Python code as input and executes it in the Clock thread. Two FoxDot examples exhibiting this:


```python
d1 >> play("<c{cc*}.c{..c}><x..><X.o.>", rate=1)

@nextBar(32):
def somefunction():
    d1.rate = 2

# Or with

Clock.future(16, somefunction)
```

I'd like to make this mechanism more developed and easier to use live with a new syntax and tools.


```python
with later(77):
    # execute any code 77 beats later
    c1.fadeout(13)

with every(16):
    # execute some code every 16 beats
    # for example pick eight new random notes for the synth
    c1.degree = PRand(0,7)[:8]

climax = TimeMarker() # define a abstract moment on the clock to be scheduled later

# Program a fadein before the climax
with before(climax, 16):
    players.fade(fvol=1.3)
    # other code actions

# Program a cut at climax time
with at(climax):
    c_all.mute(8)
    #

# Then each time we define a time value to the climax marker
# the fadein and cut are automatically scheduled around that moment
climax.time(later(8))

# We could also say climax time is cyclic or a Pattern
climax.time(every(64))
climax.time(P[32,16,48,24])
climax.time(PRand(1,4)[:8]*16)

# We could also use a similar syntax to define a state machine with n states,
# each state being a block of code to execute
# with time or value conditions to transition to other states.

# And many other things
```

Some remarks about this:

- This will clearly expose the user to all sorts of circularity problems and probably unexpected behaviors. It should be fun if used carefully and using a limiter (FoxDot/Renardo has one by default).

- This kind of syntax is rooted in the Object/Imperative/mutable state paradigm of coding music. I find interesting that FoxDot is hybrid in this regard because its standard syntax is close to the functional/declarative/evolving loop paradigm of Tidal/Strudel and it works great in that direction. But at the same time each player parameter is accessible for mutable modification. I like this idea of both paradigms being complementary depending of the result to express, in the same way Python is a multiparadigm langage.

- I think this kind of metaprogramming can help express higher level or longer period behavior of the music. It can lead to less live coding, for exemple composing a piece by scheduling each part, which to me can be desirable when trying to produce algorithmic track to somehow feed the music industry monster. It can also lead to more live coding if some longer term evolution can be expressed quickly, and/or abstracted away at start, freeing time and attention to enjoy livecoding "note scale" patterns.

### State of Renardo and contribution

I'd like to conclude this by ampheemphasising that Renardo is meant to be a community fork and not a personal project. We are already three direct members to the software repository and it's documentation. I shall move it to a collective github organisation at some point. Don't hesitate to reach me by email or on Telegram.

I haven't been advertising this fork a lot because, I feel the refactoring and modularization needs to be finished before it can be more usable and easy to contribute to. But you can still come with a pull request or any issue/remark and I will try to integrate it.



