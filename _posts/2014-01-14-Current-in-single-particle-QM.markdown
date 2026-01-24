---
layout: post
title: Current in Single Particle Quantum Mechanics
published: true
category: short-calculations
---

For simplicity, I will only use one-dimension in this post, but this can be generalized to higher dimensions rather easily.

Many textbooks on Quantum Mechanics mention current density can be derived from the continuity equation and probability.
The usual method for figuring this out is to assume you have some Hamiltonian $$ H = p^2/2m + V(x)$$ where $$p$$ is the momentum and $$x$$ is the position.
In this way the current density is written in terms of the wave function $$\psi(x,t)$$ as
<!--more-->

\begin{equation}
j(x,t) = \frac1{2m i}\left[ \psi^* \overrightarrow{\partial_x} \psi - \psi^* \overleftarrow{\partial_x} \psi \right].
\end{equation}

This then satisfies the continuity equation

\begin{equation}
\partial_t \rho(x,t) + \partial_x j(x,t) = 0,
\end{equation}

with density $$\rho(x,t)=\psi^*(x,t)\psi(x,t)$$. It should be noted that if you write the wave function as $$\psi(x,t) = \sqrt{\rho(x,t)} e^{i \theta(x,t)}$$, then the current is just proportional to the gradient of the phase $$j(x,t)= \rho(x,t) \partial_x \theta(x,t)/m$$, giving the spatial change in phase a physical significance.

However, there are two lingering questions:

1.  Is this current density related to the Heisenberg operator $$\dot x(t)$$ which tracks the velocity of the system?
2.  If so, does it generalize to more arbitrary Hamiltonians?

To answer these questions, we consider the more arbitrary Hamiltonian

\begin{equation}
H = T(p) + V(x),
\end{equation}

where $$V(x)$$ is some potential and the kinetic energy is some polynomial

\begin{equation}T(p) = \sum_{n=1} a_n \frac{p^n}{n!}.\end{equation}

We are unworried about bounding the energy, so odd-order Kinetic energy terms are allowed (in the higher dimensional case, the Dirac-like Hamiltonians have linear terms in $$p$$).
At this point, we can take our Heisenberg operator $$\dot x(t)$$ and find

$$
\begin{align}
\dot x(t) & = i [H, x(t)] \\
  & = T'(p(t)).
\end{align}
$$

where $$T'$$ is the derivative of $$T$$ with respect to its argument.
Now, we would like to obtain a current density from this quantity.
We can certainly define the total current at a specific time as

$$
\begin{align}
I & = \langle\psi_0\lvert \dot x(t) \rvert \psi_0\rangle = \langle\psi_0\lvert T'(p(t)) \rvert \psi_0\rangle \\
 & = \langle\psi(t)\lvert T'(p) \rvert \psi(t)\rangle,
\end{align}
$$

where in the last line we go from the Heisenberg to Schroedinger picture. Now to get density, we need to use a complete set position states, so that

$$
\begin{align} \label{eq:total-current} 
I & = \int dx \, dy \, \langle\psi(t)\lvert x\rangle \langle x \lvert T'(p) \rvert y \rangle \langle y \lvert \psi(t)\rangle.
\end{align}
$$

Now, $$p$$ acts as a derivative on position kets, so that one can verify that

$$
\begin{equation}
\langle x \lvert T'(p) \rvert y \rangle = T'(-i \partial_x ) \delta(x-y).
\end{equation}
$$

However, there is an ambiguity here since we can write

$$
\begin{align}
T'(-i \partial_x)\delta(x-y) & =  \sum_{n=0} a_{n+1} \frac{(-i\partial_x)^n}{n!} \delta(x-y) \nonumber \\ & = \sum_{n=0} a_{n+1} \frac{(-i\partial_x)^{n-m} (i \partial_y)^m}{n!} \delta(x-y). \label{eq:T-delta} 
\end{align}
$$

This ambiguiuty in how to choose the derivatives leaves us with many way to define the current density.
Fortunately, only one of these combinations satisfies the continuity equation.
To figure out which one that is, let us reverse engineer the continuity equation to obtain a solution.
The density is $$\rho(x,t) = \psi^*(x,t) \psi(x,t)$$, and so using the Schroedinger's equation, we have

$$
\begin{align}
  i \partial_t \rho(x,t) & = i(\psi^*(x,t) \overleftarrow {\partial_t} \psi(x,t) + \psi^*(x,t) \overrightarrow {\partial_t} \psi(x,t) ) \\
   & = - [\psi^*(x,t)( T(i \overleftarrow{\partial_x} ) - T(-i \overrightarrow{\partial_x} ) )\psi(x,t) ].
\end{align}
$$

Thus, the continuity equation must become

\begin{align}
  \partial_t \rho(x,t) - i [\psi^*(x,t)( T(i \overleftarrow{\partial_x} ) - T(-i \overrightarrow{\partial_x} ) )\psi(x,t) ] = 0.
\end{align}

If we now assume that we have a current density that takes the form

\begin{equation} j(x,t) = \psi^*(x,t) \vartheta(\overleftarrow{\partial_x},\overrightarrow{\partial_x}) \psi(x,t), \end{equation}

and satisfies the continuity equation, $$\partial_t \rho + \partial_x j = 0$$, then we can equate operators to obtain

\begin{align} \label{eq:diff-ops-cty} 
\overleftarrow{\partial_x} \vartheta + \vartheta \overrightarrow{\partial_x} = -i [T(i \overleftarrow{\partial_x} ) - T(-i \overrightarrow{\partial_x} ) ].  
\end{align}

Anticipating the answer, we write the general form of $$\vartheta$$ as

\begin{equation}
\vartheta =  \sum_{n=0} \sum_{m=0}^n (-1)^{m} i^n b_{n,m} \overleftarrow{\partial}{}_x^{n-m} \overrightarrow{\partial}{}_x^m.
\end{equation}

Then we can take the left hand side Eq. \\eqref{eq:diff-ops-cty} and write

$$
\begin{multline}
\overleftarrow{\partial_x} \vartheta + \vartheta \overrightarrow{\partial_x} = -i \sum_{n=1} i^n b_{n-1,0} \overleftarrow{\partial}{}_x^{n} - \sum_{n=0} \sum_{m=0}^{n-1} (-1)^m i^n \left[  b_{n,m+1} - b_{n,m} \right] \\ \times \overleftarrow{\partial}{}_x^{n-m} \overrightarrow{\partial}{}_x^{m+1}
+ i \sum_{n=1} (-i)^{n} b_{n-1,n-1} \overrightarrow{\partial}{}_x^{n} .
\end{multline}
$$

On the other hand, we can calculate the right hand side of Eq. \\eqref{eq:diff-ops-cty} to be

$$
\begin{equation}
-i [T(i \overleftarrow{\partial_x} ) - T(-i \overrightarrow{\partial_x} ) ] = -i \sum_{n=1} a_n i^n \frac{\overleftarrow{\partial}{}_x^n}{n!} + i \sum_{n=1} a_n (-i)^n \frac{\overrightarrow{\partial}{}_x^n}{n!}.
\end{equation}
$$

Equating the left and right sides, we can just read off that $$b_{n-1,0} = a_n/n!$$, $$b_{n-1,n-1}= a_n/n!$$ and $$b_{n,m+1} = b_{n,m}$$, so that $$b_{n,m} = a_{n+1}/(n+1)!$$.

Thus, we have

\begin{equation}
\vartheta = - \sum_{n=0} \sum_{m=0}^n (-1)^{m} i^n \frac{a_{n+1}}{(n+1)!} \overleftarrow{\partial}{}_x^{n-m} \overrightarrow{\partial}{}_x^m.
\end{equation}

Returning all the way to when we were considering $$\dot x(t)$$ as an integral over position,
this suggests that in Eq. \\eqref{eq:T-delta}, we want to consider

\begin{equation}
T'(-i \partial_x)\delta(x-y)  \\ = \sum_{n=0} \frac{a_{n+1}}{n!} \frac1{n+1}\sum_{m=0}^n (-i\partial_x)^{n-m} (i \partial_y)^m \delta(x-y).
\end{equation}

Given the expression for total current Eq. \\eqref{eq:total-current} and integrating the delta function by parts numerous times, we can replace $$\partial_x$$ with $$-\overleftarrow \partial_x$$ and $$\partial_y$$ with $$- \overrightarrow\partial_x$$, and then the total current is just

\begin{equation}
I = \int dx \, \psi^*(x,t) \sum_{n=0} \frac{a_{n+1}}{(n+1)!} \sum_{m=0}^n (i \overleftarrow \partial_x)^{n-m} (-i \overrightarrow \partial_x)^m \psi(x,t).
\end{equation}

which actually integrates the current density! Thus, we have shown that

\begin{equation}
j(x,t) = \psi^*(x,t) \sum_{n=0} \frac{a_{n+1}}{(n+1)!} \sum_{m=0}^n (i \overleftarrow \partial_x)^{n-m} (-i \overrightarrow \partial_x)^m \psi(x,t),
\end{equation}

and that

\begin{equation}\langle \dot x(t) \rangle = \int dx \, j(x,t). \end{equation}

Indeed, $$\dot x(t)$$ does track the current of the problem and can even be written as the integral of a current density. Even for the more arbitrary Hamiltonian $$H = T(p) + V(x)$$.
