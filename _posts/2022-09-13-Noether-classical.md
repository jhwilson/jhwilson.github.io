---
layout: distill
title: Noether's theorem in classical mechanics 
description: Noether's theorem states that symmetries lead to conservation laws. This is its general framework in classical mechanics.
date: 2022-09-13

authors:
    - name: Justin H. Wilson
      url: "https://jhwilson.com"
      affiliations:
        name: Dept. of Physics & Astronomy, LSU <br> Center for Computation and Technology, LSU
        
toc:
  - name: Introduction
  - name: General Statement
  - name: A symmetry of space and time
  - name: Rotating system
---

## Introduction

Noether's (first) theorem is one of the most important theorems in physics. It relates well known _conserved_ quantities of energy, momentum, charge, and more to fundamental symmetries of our equations of motion. It plays a role in classical mechanics as it does elsewhere in physics, but many text books separate out time/energy from momentum conservations and gloss over the most general proof -- which crucially misses cases where time and space must transform together to reveal a symmetry.

This post is meant to bridge that gap and provide a foundation to use Noether's theorem in more areas of physics.

## General statement

The statement is built on the idea of the action principle, and we will use the specific form

$$
\begin{equation}
 S[q] = \int dt \, L(q_1, \ldots, q_s, \dot q_1, \ldots, \dot q_s; t)
\end{equation}
$$

We will, for simplicity neglect the 1 through $s$ labels
$$
\begin{equation}
 S[q] = \int dt \, L(q, \dot q ; t).
\end{equation}
$$
The general statement is that $S[q] = S[\sigma(q, \alpha)]$ for any $\alpha$ (and neglecting boundary terms -- terms which depend exclusively on $q$ or $\dot q$ at the initial or final times).
The function $\sigma(q,\alpha)$ represents our symmetry transformation (it could be rotations $\alpha = \theta$, time translations, spatial translations, or something even more complicated).
Importantly, we define $\sigma(q, 0) = q$, so that we can expand $\sigma(q, \alpha) = q + \frac{\partial \sigma}{\partial \alpha}\big\rvert_{\alpha = 0} \alpha + \cdots$ allowing us to make _infinitesimal_ symmetry transformations.
Writing out the action explicitly,

$$
\begin{equation}
\int dt \, L(q, \dot q; t) = \int dt \, L\bigg(\sigma(q, \alpha), \frac{d}{dt} \sigma(q, \alpha); t\bigg).
\end{equation}
$$

We define $L_\alpha \equiv L(\sigma(q, \alpha), \frac{d}{dt} \sigma(q, \alpha); t)$ for ease.
In order to be a symmetry, we can expand the right in terms of $\alpha$ 
$$
\begin{equation}
\int dt \, L(q, \dot q; t) = \int dt \, \bigg[L(q, \dot q; t) + \alpha \frac{\partial L_\alpha}{\partial \alpha}\Big\rvert_{\alpha = 0} + \cdots \bigg].
\end{equation}
$$

In the above, they can only differ by a boundary term which implies there is a function $\Lambda(q, \dot q; t)$ such that
$$
\begin{equation}
    \frac{\partial L_\alpha}{\partial \alpha}\Big\rvert_{\alpha = 0} = \bigg[ \frac{\partial L}{\partial q} \frac{\partial \sigma}{\partial \alpha} + \frac{\partial L}{\partial \dot q} \frac{d}{dt}\frac{\partial \sigma}{\partial \alpha} \bigg]_{\alpha=0}= \frac{d \Lambda(q, \dot q; t)}{dt}. \label{eq:dLambda}
\end{equation}
$$
**This is what it means, in general, for a Lagrangian to have a (continuous) symmetry.** For the action to have a symmetry and produce the same equations of motion, the Lagrangian can differ by at most a full derivative.
This is a powerful statement: it is true regardless of path, it is just a property of the action itself.
We will use it for the extremal paths that minimize the action in order to derive Noether's theorem.

To prove Noether's theorem we consider a (small) time dependence of $\alpha = \alpha(t)$.
The logic here is rather simple: We are trying to find equations of motion but instead of just blindly letting $q \mapsto q + \delta q$, we choose $\delta q =\alpha(t) \frac{\partial \sigma}{\partial \alpha}\Big\rvert_{\alpha = 0}$ and let $\alpha(t)$ freely vary (not just be constant).
In this way, we will obtain a term proportional to $\alpha(t)$ and it must be zero _on the paths that minimize the action_.

The main difference from what we showed above comes from the derivative term
$$
\begin{equation}
\begin{aligned}
 \frac{d}{dt} \sigma(q, \alpha(t)) & = \frac{d}{dt} \bigg( q + \alpha(t) \frac{\partial \sigma}{\partial \alpha}\Big\rvert_{\alpha = 0} + \cdots \bigg) \\
 & = \dot q + \alpha(t) \frac{d}{dt } \bigg(\frac{\partial \sigma}{\partial \alpha}\Big\rvert_{\alpha = 0}\bigg)  + \dot \alpha(t)\frac{\partial \sigma}{\partial \alpha}\Big\rvert_{\alpha = 0},
\end{aligned}
\end{equation}
$$
where notice that we have a term proportional to $\dot \alpha(t)$.

Explicitly, we can make the expansion
$$
\begin{equation}
\begin{aligned}
   S[\sigma(q, \alpha(t))] & = \int dt \, L\bigg(\sigma(q, \alpha(t)), \frac{d}{dt} \sigma(q, \alpha(t)); t\bigg) \\
    & = \int dt \, L\bigg(q + \alpha(t)\frac{\partial \sigma}{\partial \alpha}\Big\rvert_{\alpha = 0} + \cdots , \\ & \quad\quad\quad \quad \quad \dot q + \alpha(t) \frac{d}{dt } \bigg(\frac{\partial \sigma}{\partial \alpha}\Big\rvert_{\alpha = 0}\bigg) + \dot \alpha(t)\frac{\partial \sigma}{\partial \alpha}\Big\rvert_{\alpha = 0} ; t\bigg) \\
    & = \int dt \, \bigg(L(q, \dot q) + \alpha(t)\bigg[ \frac{\partial L}{\partial q} \frac{\partial \sigma}{\partial \alpha} + \frac{\partial L}{\partial \dot q} \frac{d}{dt}\frac{\partial \sigma}{\partial \alpha} \bigg]_{\alpha=0} \\ & \hspace{140pt}+ \frac{\partial L}{\partial \dot q} \frac{\partial \sigma}{\partial \alpha} \bigg\rvert_{\alpha=0} \dot \alpha(t) + \cdots \bigg) \\
    & = \int dt \, \bigg(L(q, \dot q) + \bigg[ \frac{d \Lambda}{dt} - \frac{d}{dt}\bigg(\frac{\partial L}{\partial\dot q} \frac{\partial \sigma}{\partial \alpha} \bigg\rvert_{\alpha=0}\bigg) \bigg] \alpha(t) + \cdots \bigg),
\end{aligned}
\end{equation}
$$
where in the last line we have used \eqref{eq:dLambda} and integration by parts on the last term (dropping boundary terms).
To extremize the action, we cannot have a term proportional to $\alpha(t)$ which means the term multiplying it is zero. 
In other words, we have formally found the conserved quantity
$$
\begin{equation}
   Q = \frac{\partial L }{\partial \dot q}  \frac{\partial \sigma}{\partial \alpha} \bigg\rvert_{\alpha=0} - \Lambda, \quad \frac{d Q}{dt} = 0. \label{eq:Qconserve}
\end{equation}
$$

Most of the work will be finding what $\Lambda$ is.

## A symmetry of space and time

Now, we want to make a slightly more specific observation using just one dimension.
The symmetry we care about is going to be one of both space and time and we can write it out with infinitesimals
$$
\begin{equation}
   \begin{aligned}
    x & \mapsto x + \alpha \delta x(x, \dot x, t) + \cdots, \\
    t & \mapsto t + \alpha \delta t(x, \dot x, t) + \cdots.
   \end{aligned} 
\end{equation}
$$
**Caution: $\delta x$ and $\delta t$ are functions and never assumed to be small in this calculation, it is only $\alpha$ that we take to be small.**

For generality, the objects $\delta x$ and $\delta t$ are functions which can depend on the trajectory in potentially complicated ways.
For a trajectory, the time mapping is modified by both of the above and we obtain 
$$
\begin{equation}
   x(t) \mapsto x(t + \alpha \delta t(x, \dot x, t) + \cdots) + \alpha \delta x(x, \dot x, t)  + \cdots,
\end{equation}
$$
which we can expand the argument of $x(t)$ to obtain
$$
\begin{equation}
   x(t) \mapsto x(t) + \alpha ( \delta x + \dot x(t) \delta t) + \cdots,
\end{equation}
$$
where for simplicity we have dropped the arguments of $\delta x$ and $\delta t$. One might wonder why $t$ is not transformed within the arguments of these functions and the reason is simply because that will constitute a higher order correction which is buried in the "$+\cdots$" at the end of the expression.

We have thus found 

$$
\begin{equation}
   \frac{\partial \sigma}{\partial \alpha}\Big\rvert_{\alpha = 0} = \delta x + \dot x(t) \delta t, \label{eq:xtsigma}
\end{equation}
$$
our first ingredient in computing our conserved quantity $Q$.

Next, we need to consider what happens to the action itself. In this case, it is helpful to (1) consider the Lagrangian along with the infinitesimal $dt$ that it comes with as part of the action and (2) define the time transformation $\tau_\alpha =t + \alpha \delta t(x, \dot x, t) + \cdots$. 
With these, our statement of symmetry under this spacetime transformation implies that the Lagrangian transforms as follows 

$$
\begin{equation}
   dt\, L\bigg(\sigma(x, \alpha), \frac{d}{dt} \sigma(x,\alpha)\bigg) = d\tau_\alpha L( x(\tau_\alpha), \dot x(\tau_\alpha))
\end{equation}
$$

Or in otherwords, we reorganize terms to obtain
$$
\begin{equation}
   L\bigg(\sigma(x, \alpha), \frac{d}{dt} \sigma(x,\alpha)\bigg) = \frac{d\tau_\alpha}{dt} L( x(\tau_\alpha), \dot x(\tau_\alpha)).
\end{equation}
$$
This makes sense: If you change variables on the right (integrating over $t$) changing $t$ to $\tau_\alpha$, you would get the normal action that already know and love.

If we expand the right though, (calling it $L_\alpha$), we obtain
$$
\begin{equation}
\begin{aligned}
   L_\alpha & = (1 + \alpha \dot{\delta t} + \cdots)\Big(L + \alpha \frac{dL}{dt} \delta t + \cdots \Big)  \\
   & = L + \alpha \frac{d}{dt} ( L \delta t) + \cdots. 
\end{aligned}\label{eq:xtLambda}
\end{equation}
$$
We have thus found $\Lambda = L \delta t$.
Combining \eqref{eq:xtLambda} and \eqref{eq:xtsigma} into \eqref{eq:Qconserve}, we have
$$
\begin{equation}
   Q = \frac{\partial L}{\partial \dot x} ( \delta x + \dot x \delta t) - L \delta t, 
\end{equation}
$$
or in other words,
$$
\begin{equation}
   Q = \bigg(\dot x \frac{\partial L}{\partial \dot x} - L\bigg) \delta t + \frac{\partial L}{\partial \dot x} \delta x. \label{eq:xtQ}
\end{equation}
$$
This effectively has mixed something that looks energy-like (the term proportional to $\delta t$) to the term which is more momentum-like (the term proportional to $\delta x$).
In fact, one can use this expression to derive both energy and momentum separately (in cases where those are in fact conserved).
Furthermore, the result to higher dimensions and more particles is rather straightforward.

## Rotating system

We end with a simple application of the above: A Lagrangian that experiences an external rotation (at frequency $\omega$). 
In this case the Lagrangian has a functional form in cylindrical coordinates

$$
L(r, \theta - \omega t, \dot r, \dot \theta).
$$

In this case there is no energy or angular momentum conservation, but we do have a transformation law that will leave our Lagrangian invariant
$$
\begin{equation}
   \begin{aligned}
     t & \mapsto t + \alpha, \\
     \theta & \mapsto \theta - \omega \alpha.
   \end{aligned} 
\end{equation}
$$
(The minus signs comes from the following algebra $\theta(t) - \omega t \mapsto \theta(t + \alpha) - \omega (t + \alpha)$, notice that $t$ does not explicitly change but $\theta(t)\mapsto \theta(t + \alpha) - \omega \alpha$.)

Using what we have shown in \eqref{eq:xtQ} (generalized to higher dimensions), we have a conserved quantity
$$
\begin{equation}
   Q = E - \omega \frac{\partial L}{\partial \dot \theta}  = E - \omega L_z,
\end{equation}
$$
a quantity that is a combination of both energy and angular momentum about the $z$-axis (which are separately not conserved but this combination _is_).
