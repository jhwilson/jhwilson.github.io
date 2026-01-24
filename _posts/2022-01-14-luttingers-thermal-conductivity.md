---
title: Thermal conductivity via gravity
layout: post
published: false 
category: short-calculations
---

In 1964, Luttinger made an astute observation
> Just as the space- and time-varying external electric potential produced electric currents and density variations, so a varying gravitational field will produce, in principle, energy flows and temperature fluctuations.

He would go on to calculate heat transport using this method of gravity. Here, we repeat his calculation.

First, in our system we say we have a Hamiltonian 

$$
\begin{equation}
 H = \int d^d r \, \psi^\dagger(\mathbf r) h(\mathbf r) \psi(\mathbf r)
\end{equation}
$$

Within the integral, this is the _hamiltonian density_. It is important to note that $$h(\mathbf r)$$ is in general a differential operator. In fact, for a usual particle in a potential we will have $$h(\mathbf r) = \frac{\overleftarrow{\nabla}_{\mathbf r}\cdot  \overrightarrow{\nabla}_{\mathbf r}}{2m} + V(\mathbf r)$$. We will perturb this with a gravitation field $$\phi(\mathbf r, t)$$. The equation will take the form

$$
\begin{equation}
 H_\phi = \int d^d r \, (1 + \phi(\mathbf r, t)) \psi^\dagger(\mathbf r) h(\mathbf r) \psi(\mathbf r)
\end{equation}
$$

The operator for hamiltonian density $$\hat h(\mathbf r) = \psi^\dagger(\mathbf r) h(\mathbf r) \psi(\mathbf r)$$, and without the gravitational field, it has an evolution given by

$$
\begin{equation}
\begin{aligned}
i \frac{d \hat h(\mathbf r, t)}{dt} & = [ \hat h(\mathbf r, t), H] \\
 & = \int d^d r' [\hat h(\mathbf r, t), \hat h(\mathbf r', t) ].
\end{aligned}
\end{equation}
$$

How does the Hamiltonian operator commute with itself at different times? Well being careful to keep it in the right place (as an operator), we have

$$
\begin{equation}
\begin{aligned}[]
  [\hat h(\mathbf r, t), \hat h(\mathbf r', t) ] & = \psi^\dagger(\mathbf r,t) h(\mathbf r) \delta(\mathbf r - \mathbf r') h(\mathbf r')\psi(\mathbf r', t) - (\mathbf r \leftrightarrow \mathbf r')
\end{aligned}
\end{equation}
$$

When we integrate over $$\mathbf r'$$ there will be integration by parts that will be important in this expression, so to be explicit, we write

$$
\begin{equation}
h(\mathbf r) = \sum_{n=0}^\infty \sum_{m = 0}^n  ( i \overleftarrow{\partial_{\mathbf r}})^m h_{nm}(\mathbf r) (-i \overrightarrow{\partial_{\mathbf r}})^{n-m}.
\end{equation}
$$
In order to ensure that the energy density is hermitian, we can evaluate $$h^\dagger(\mathbf r)$$ and matching terms, we find

$$
h_{nm}(\mathbf r) = h_{n,n-m}^\dagger(\mathbf r).
$$

When we have derivatives acting on the Dirac delta function we will use $$\partial_x^a \partial_y^b \delta(x-y) = (-1)^b \partial_x^{a+b} \delta(x-y)$$, and we can write using the shorthand $$\psi = \psi(\mathbf r, t)$$ and $$\psi' = \psi(\mathbf r', t)$$

$$
\begin{equation}
 \psi^\dagger h(\mathbf r) \delta(\mathbf r - \mathbf r') h(\mathbf r')\psi'  =  
 \sum_{nm,n'm'} (-1)^{n-m} \partial_{\mathbf r}^m\psi^{\dagger} h_{nm} \partial_{\mathbf r'}^{n-m+m'} \delta(\mathbf r - \mathbf r') h_{n'm'} \partial_{\mathbf r'}^{n' - m'} \psi' 
\end{equation}
$$

Integrating over $$\mathbf r'$$ gives us

$$
\begin{equation}
\begin{aligned}
  \int_{\mathbf r'} \psi^\dagger h(\mathbf r) \delta(\mathbf r - \mathbf r') h(\mathbf r')\psi' = 
 \sum_{nm,n'm'} (-1)^{m'} \partial_{\mathbf r}^m\psi^{\dagger} h_{nm} \partial_{\mathbf r}^{n-m+m'}[ h_{n'm'} \partial_{\mathbf r}^{n' - m'} \psi ]
\end{aligned}
\end{equation}
$$