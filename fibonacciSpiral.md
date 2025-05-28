# Fibonacci Spiral in $d$ dimensions

The Fibonacci Spiral is one of the best known methods to analytically place $N$ points on a $(d-1)$-dimensional hypersphere, such that the distance between nearest neighbours is the as uniform as possible.

### Probability distribution of the angular components

The generalized spherical coordinates in $d$ dimensions are

$$
x_1 = r \, \sin\theta_1 \, \dots \, \sin\theta_{d-2} \, \sin\theta_{d-1}
\\
x_2 = r \, \sin\theta_1 \, \dots \, \sin\theta_{d-2} \, \cos\theta_{d-1}
\\
x_3 = r \, \sin\theta_1 \, \dots \, \sin\theta_{d-3} \, \cos\theta_{d-2}
\\
\dots
\\
x_d = r \, \cos\theta_1
$$

which can be summarized in just one formula

$$
x_i = r \, \prod_{j=1}^{d-i} \sin\theta_j \, \cos\theta_{d+1-i}
$$

where $\cos\theta_d \equiv 1$ can be defined to account for the first cartesian component. Since the hypersphere has constant radius, the relevant variables are the $d-1$ angular coordinates $\theta_i$.

A uniform probability distribution over the hypersphere of radius $R_0$ in Carthesian coordinates would look like

$$
P(x_1,\dots,x_d) = \frac{\Gamma\left(\frac{d}{2}\right)}{2\pi^{d/2}R_0^d} \, \delta \left( \sum_i^d x_i^2-R_0 \right)
$$

To change this to hyperspherical coordinates, the Jacobian of the coordinate transformation must be computed. According to [Wikipedia](https://en.wikipedia.org/wiki/N-sphere#Spherical_volume_and_area_elements), the Jacobian is $|J| = r^{d-1} \sin^{d-2}\theta_1 \sin^{d-3}\theta_{2} \dots \, \sin\theta_{d-2}$. This leads to the probability distribution in the hyperspherical coordinates

$$
P(r,\theta_1,\dots,\theta_{d-1}) = \frac{\Gamma\left(\frac{d}{2}\right)}{2\pi^{d/2}R_0^d} \, r^{d-1} \, \prod_{i=1}^{d-2 }\sin^{d-1-i}\theta_i \: \delta \left( r - R_0 \right)
$$

Since all the coordinates are independent and the radial one is fixed, the probability distribution can be factorized in its angular components and the radial one can be marginalized out (suppose $R_0 = 1$ for simplicity with the normalization coefficient), so to get

$$
P(\theta_1,\dots,\theta_{d-1}) = \prod_i^{d-1} P(\theta_i)
$$

where each $P(\theta_i) \propto \sin^{d-1-i}\theta_i$. With the normalization factor one can start considering

$$
\frac{\Gamma\left(\frac{d}{2}\right)}{2\pi^{d/2}} = \frac{1}{2\pi} \left(\frac{1}{\sqrt{\pi}}\right)^{d-2} \Gamma\left(\frac{d}{2}\right) \frac{\Gamma\left(\frac{d-1}{2}\right)}{\Gamma\left(\frac{d-1}{2}\right)}\dots\frac{\Gamma\left(1\right)}{\Gamma\left(1\right)}
\\
= \frac{1}{2\pi} \left(\frac{1}{\sqrt{\pi}}\right)^{d-2} \frac{\Gamma\left(\frac{d}{2}\right)}{\Gamma\left(\frac{d-1}{2}\right)} \frac{\Gamma\left(\frac{d-1}{2}\right)}{\Gamma\left(\frac{d-2}{2}\right)}\dots\frac{\Gamma\left(\frac{3}{2}\right)}{\Gamma\left(1\right)} \Gamma\left(1\right)
\\
= \frac{1}{2\pi} \left(\frac{1}{\sqrt{\pi}}\right)^{d-2} \frac{\Gamma\left(\frac{d}{2}\right)}{\Gamma\left(\frac{d-1}{2}\right)} \frac{\Gamma\left(\frac{d-1}{2}\right)}{\Gamma\left(\frac{d-2}{2}\right)}\dots\frac{\Gamma\left(\frac{3}{2}\right)}{\Gamma\left(1\right)}
$$

Doing so, there are $d-2$ factors in the form $\frac{\Gamma\left(\frac{i}{2}\right)}{\Gamma\left(\frac{i-1}{2}\right)}$, so regrouping the factors as

$$
\frac{1}{2\pi} \qquad,\qquad \frac{1}{\sqrt{\pi}}\frac{\Gamma\left(\frac{i}{2}\right)}{\Gamma\left(\frac{i-1}{2}\right)} \quad \mathrm{for} \: i \in \mathbb{N} \cap \left[3, d\right]
$$

we obtain the $1+(d-2)$ normalization coefficients.

Considering $P(\theta_i) \propto \sin^{d-1-i}\theta_i$, for the first angular component we obtain

$$
P(\theta_1) = \frac{1}{\sqrt{\pi}}\frac{\Gamma\left(\frac{d}{2}\right)}{\Gamma\left(\frac{d-1}{2}\right)} \sin^{d-2}\theta_1
$$

which can be verified being a properly normalized probability distribution for any $d$. For all other angular components until the last one, a similar reasoning can be applied, taking all the $d-2$ normalization coefficients expressed as a fraction of Gamma functions.

The last angular component $\theta_{d-1}$ is uniformly distributed over the complete angle, so it has the other normalization coefficient.

To sum up, the probability distributions of the angular components are

$$
P(\theta_{d-1}) = \frac{1}{2\pi}
\\
P(\theta_i) = \frac{1}{\sqrt{\pi}}\frac{\Gamma\left(\frac{d+1-i}{2}\right)}{\Gamma\left(\frac{d-i}{2}\right)} \sin^{d-1-i}\theta_i
$$


### Random sampling

Computing the cumulative probability distribution is useful to apply the inverse-sampling technique for generating random samples.

The general cumulative distribution is

$$
P(\vartheta_i \le \theta_i) = \int_0^{\theta_i} P(\vartheta_i) \: d\vartheta_i
$$

To evaluate the integral in arbitrary dimension, one can resort to the recursive relation

$$
\int \sin^d x \: dx = -\frac{1}{d} \sin^{d-1} x \: \cos x + \frac{d-1}{d} \int \sin^{d-2} x \: dx
$$

valid for $d \ge 2$, where the cases for $d \in \{0,1\}$ are trivial.

The formula above can be proven by integrating by parts

$$
\int \sin^d x \: dx = \int \sin^{d-1} x \: \sin x \: dx
\\
= \sin^{d-1} x \left(-\cos x\right) - (d-1) \int \sin^{d-2} x \: \cos x \left(-\cos x\right) \: dx
\\
= \sin^{d-1} x \left(-\cos x\right) + (d-1) \int \sin^{d-2} x \: \cos^2 x \: dx
\\
= \sin^{d-1} x \left(-\cos x\right) + (d-1) \int \sin^{d-2} x \left(1-\sin^2 x\right) \: dx
$$

Defining $I_i := \int \sin^i x \: dx$, the equation above becomes

$$
I_d = \sin^{d-1} x \left(-\cos x\right) + (d-1) I_{d-2} + (1-d) I_d
\\
d \, I_d = \sin^{d-1} x \left(-\cos x\right) + (d-1) I_{d-2}
$$

which proves the above relation.

In this case, the recursive relation is always evaluated as a definite integral in $[0,\theta_i]$, so 

$$
\int_0^{\theta_i} \sin^d x \: dx = -\frac{1}{d} \sin^{d-1} x \: \cos x + \frac{d-1}{d} \int \sin^{d-2} x \: dx
$$

 we can leverage this recursive relation to write that

$$
P(\vartheta_i \le \theta_i) = \frac{1}{\sqrt{\pi}}\frac{\Gamma\left(\frac{d+1-i}{2}\right)}{\Gamma\left(\frac{d-i}{2}\right)} \int_0^{\theta_i} d\vartheta_i \, \sin^{d-1-i}\vartheta_i
\\
= 
$$

To obtain then a random point with uniform probability over the hypersphere is then possible to generate a random variable with uniform probability distribution over the unit hypercube $\vec{Y} \sim \mathrm{U}^d(0,1)$, and then map it to the angular coordinates through the cumulative distributions above described

$$
Y_i = P(\vartheta_i \le \theta_i)
$$

and solve the implicit equation for all $\theta_i$.


### Fibonacci Spiral

To generate a Fibonacci Spiral, the angular coordinates must be dependent one another: the spiral is a $1$-dimensional surface, so there is only one free parameter that describes it. Thus, instead of sampling random variables, we set a grid of $N$ integers $k \in [1\dots N]$, and we write the dependency of the cumulative variables $Y_i$ from that. The grid is composed by $N$ points indexed by $k$, so for each angular component there will be a collection of cumulative variables $Y_i^k$, one for each of the points in the grid.

It must be ensured that there are no periodic patterns in the unit hypercube, to avoid concentration of points on the hypersphere. To ensure so, we can take $d-1$ irrational numbers $c_i \in \mathbb{I}$ which ratio is always irrational $\frac{c_i}{c_j} \in \mathbb{I}$ for $j \ne i$. A convenient and general way to proceed is to take

$$
c_i = \sqrt{p}
$$

where $p$ is a prime number. With this approach, one can compute the first $d-1$ prime numbers and have all the coefficients $c_i$.

The use of irrational numbers allows $\mathrm{frac}(k \, c_i)$ to asymptotically cover densely the interval $[0,1]$. Thus, we can set one the cumulative variables to be

$$
Y_{d-1}^k = 2\pi \frac{k-0.5}{N} 
\\
Y_i^k = \mathrm{frac}(k\, c_i)
$$

for $i \in \{1,\dots,d-2\}$, and solving implicitly for $\theta_i$ obtain the angular components for the uniform grid.


### Testing the grid

The aim is to have a grid over the hypersphere that covers it as uniformly as possible. Ideally, the distance between nearest neighbours should be the same for all points. In pratice, the Fibonacci Spiral method does not create a perfecly uniform grid.

The distance can be defined in several ways. In this case, we define the similarity (opposite concept of distance)

$$
\rho\left(\vec{x}^i,\vec{x}^j\right) = \vec{x}^i \cdot \vec{x}^j
$$

In this case, $\vec{x}^i$ is a point in the grid on the hypersphere, so their similarity is bounded $\rho \in [-1,1]$.

To quantify the uniformity, we consider the metric

$$
\Delta = \max_i \left(\max_j \left(\rho\left(\vec{x}^i,\vec{x}^j\right)\right)\right) - \min_i \left(\max_j \left(\rho\left(\vec{x}^i,\vec{x}^j\right)\right)\right)
$$
