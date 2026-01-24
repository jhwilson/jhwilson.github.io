---
layout: page
title: PHYS 7364 - Spring 2022
description: Condensed Matter Physics II Spring 2022 
img: assets/img/superconductor.jpg
importance: 1
---

- Prof. Justin H. Wilson
- Email: jhwilson@lsu.edu

# [Final Exam](/assets/pdf/phys7364_final.pdf) DUE 12 May at 12:00pm

**The first five classes will occur over Zoom**

# Course description

Welcome to Condensed Matter Physics II! In this course, we will be focusing on two important topics in modern condensed matter theory: Many body theory and topology in condensed matter systems. These ideas and techniques have become quite important in modern condensed matter physics, with the Nobel prize in 2016 being given for ["for theoretical discoveries of topological phase transitions and topological phases of matter."](https://www.nobelprize.org/prizes/physics/2016/summary/) At the same time, many complex phenomena require _interactions_ between many particles, leading to new emergent phenomena that cannot be figured out by looking at the consituent particles; we will start to build up these techniques. 

## Lectures

MWF 10:30-11:20am, 106 Nicholson

Lectures 1/19, 1/21, 1/24, 1/26, and 1/28 will be given over Zoom (link to be emailed).

Recordings will be on the course's [moodle](https://moodle.lsu.edu/login/index.php).

## Books

The first part of the course will draw largely from [Berry Phases in Electronic Structure Theory by David Vanderbilt](https://www.cambridge.org/core/books/berry-phases-in-electronic-structure-theory/DDD71CA4FE9AF5F3A2FB300E602F394A#). We will also draw some parts from [Introduction to Many-Body Physics by Piers Coleman](https://www.amazon.com/Introduction-Many-Body-Physics-Piers-Coleman/dp/0521864887). Other books that could be useful:

- [Topological Insulators and Topological Superconductors by Andrei Bernevig and Taylor Hughes](https://www.amazon.com/Topological-Insulators-Superconductors-Andrei-Bernevig/dp/069115175X)
- [Topological Phases of Matter by Roderich Moessner and Joel Moore](https://www.amazon.com/Topological-Phases-Matter-Roderich-Moessner/dp/1107105536)
- [Condensed Matter Field Theory by Alexander Altland and Ben Simons](https://www.amazon.com/Condensed-Matter-Theory-Alexander-Altland/dp/0521769752)
- [Quantum Field Theory and Condensed Matter: An Introduction by R. Shankar](https://www.amazon.com/Quantum-Field-Theory-Condensed-Matter/dp/0521592100)

Relevant papers will be sent out or printed as needed.

# Grade breakdown

- 60% Homework
- 20% Final presentation
- 20% (Take-home) final

# Homework 

Homework can be "collaborative," but everyone needs to write-up their own. When stepping through logic and math, use complete sentences and explain what you are doing. 

Homeworks use the class file [jhwhw.cls](/assets/tex/jhwhw.cls). See [this stack exchange post](https://tex.stackexchange.com/questions/31183/class-file-for-homework-assignments/31230#31230) for information on how to use it.

- Homework 1 (Due Jan 28): [pdf](/assets/pdf/phys7364_hw1.pdf) / [tex](/assets/tex/phys7364_hw1.tex)
- Homework 2 (Due Feb 11): [pdf](/assets/pdf/phys7364_hw2.pdf) / [tex](/assets/tex/phys7364_hw2.tex) -- [benzene.py](/assets/code/benzene.py)
- Homework 3 (Due Feb 25): [pdf](/assets/pdf/phys7364_hw3.pdf) / [tex](/assets/tex/phys7364_hw3.tex) -- [chain_3_cycle.py](/assets/code/chain_3_cycle.py)
- Homework 4 (Due Mar 21; 10:30am): [pdf](/assets/pdf/phys7364_hw4.pdf) / [tex](/assets/tex/phys7364_hw4.tex)
- Homework 5 (Due Apr 4; 10:30am): [pdf](/assets/pdf/phys7364_hw5.pdf) / [tex](/assets/tex/phys7364_hw5.tex) -- [haldane_bsr.py](/assets/code/haldane_bsr.py), [haldane_bcurv.py](/assets/code/haldane_bcurv.py), [haldane_topo.py](/assets/code/haldane_topo.py)
- Homework 6 (Due Apr 18; 10:30am): [pdf](/assets/pdf/phys7364_hw6.pdf) / [tex](/assets/tex/phys7364_hw6.tex)
- Homework 7 (Due May 2; 10:30am): [pdf](/assets/pdf/phys7364_hw7.pdf) / [tex](/assets/tex/phys7364_hw7.tex)

# Final presentation

Take 1 paper from the [cond-mat arXiv](https://arxiv.org/archive/cond-mat) that will appear between now and end of March (cross-listings are OK).  Make a presentation about this material that answers the following questions:
- What question did the authors pursue in this work?
- _Why_ did the authors pursue it (motivation)
- What experimental or theoretical techniques did they use?
  - Papers often leave out details of the techniques. Research what was used and fill in some of the gaps. 
- What did they conclude?
- Is there anything you would change or is there a new insight you gained from this work?

# Course outline
(average of approximately 2 days per item)

* Electronic Structure Theory
    1. Bloch's theorem
    2. Tight-binding models
    3. Linear Response
* Second quantization
    1. Free fermions
    2. Jordan-Wigner
    3. Superconductor (mean-field ansatz)
    4. Kitaev Chain and Majorana fermions
* Berry phase
    1. Theory
    2. SSH model -- [Topological Classification]({% post_url 2022-02-20-SSH-model %})
    3. Charge pumping
* Quantum Hall Effect -- [Lecture notes for 1 and 2 below](/assets/pdf/QHE%20lecture%20notes.pdf)
    1. With magnetic field
    2. [TKNN](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.49.405)
    3. Without a magnetic field (anomalous Hall effect) -- [Haldane model](/assets/pdf/Haldane%20model.pdf)
* Path integrals & Green's functions
    1. Single-particle 
    2. Wick's theorem
    3. Free Bosons
    4. Free fermions
* Zero-temperature Feynman diagrams
    1. Hartree-Fock 
    2. Self-energy
    3. Response functions