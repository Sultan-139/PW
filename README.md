# CSPC — Computer Science for Physics and Chemistry

My coursework repository for the course.
Each practical lives under `PW<1/Lab <A>/`.

## Setup

Create and activate the environment for a given lab:

```bash
conda env create -f "PW<n>/Lab <X>/environment.yml"
conda activate cspc

cd "PW<1>/Lab <A>"
pytest -v


## PW1 — Lab A: Reproducible Foundations

**What I built:**
- <one or two lines: the CSPC repo, the environment, the decay simulation, the tests>

**Speed comparison (loop vs NumPy):**

| version | time (s) |
|---------|----------|
| pure-Python loop | 2.7443 seconds |
| NumPy (vectorised) | 0.0003 seconds |

- Speed-up: 8958.80xfaster**

**Tests:** all passing? (yes)

**Conclusion:**
- NumPy made the decay simulation much faster than standard Python loops, while unit tests confirmed our results matched the physical law. I fixed a test failure by using the final array index `[-1]` and solved GitHub push issues using a Personal Access Token.
---
PW1 Lab B:
- Data: `decay_observed.csv` shows particle  decreasing over time.
- Comparison: The observed data matches the analytical decay law well.
- Automation: The Snakemake pipeline automatically rebuilds `figure.png` whenever the source data or script changes.

--PW2 Lab A - Motion from Tracking Data

- Mean Acceleration: (-8.58)
- Standard Deviation of Acceleration: (28.72)
- Max position recovery difference: (0.7846)

Differentiation magnifies high-frequency noise because comparing nearby noisy data points creates sharp, exaggerated changes, whereas integration acts as a cumulative sum where random errors cancel each other out, thereby suppressing the noise.

### Part 2: Convex and Harder Landscapes
* **Convex Landscape (2A):** All three methods (Gradient Descent, Newton's, and SLSQP) agreed perfectly on the minimum at **x = 3.0000**.
* **Harder Landscape (2B):** From an initial guess of \(x_0 = 2.0\), Gradient Descent and Newton's method converged to a local minimum at **1.1389**, while the SLSQP bounded optimizer successfully reached the stable valley baseline. 

### Part 3: Kinetics Curve Fitting
* **Fitted Rate Constant (k):** 0.2618
* **Plot Output:** Successfully generated `kinetics.png` fitting the experimental exponential decay data cleanly.

### Part 4: Chemical Equilibrium
* **Newton Root Solution:** 0.6638 mol
* **SLSQP Minimization Solution:** 0.6638 mol
* **Equilibrium Yields:** \(H_2 = 0.3362\) mol, \(I_2 = 0.3362\) mol, \(HI = 1.3277\) mol. Both numeric root-finding and square-error optimization methods yield matching equilibrium bounds.

### Part 5: Acid-Base Titration (Bonus)
* **Equivalence Volume Point:** 50.0000 mL
* **Maximum Sloped Gradient:** 4.6000

PW3 - Data, Distributions, Testing, and Causation
Session 1 — Characterise the data
Normality Verdicts
age: Approximately normal ($p = 6.87 \times 10^{-3}$). While the Shapiro-Wilk test rejects strict theoretical normality, visual inspection reveals a fairly symmetric, bell-shaped distribution.
chol: Strongly non-normal ($p = 5.91 \times 10^{-9}$). Right-skewed distribution with severe high-value outliers.
trestbps: Strongly non-normal ($p = 1.80 \times 10^{-6}$). Marked right-skew with a physical lower limit and trailing upper values.
thalach: Approximately normal ($p = 7.00 \times 10^{-5}$). Displays a light left-skew but generally tracks close to an idealized normal curve.
Session 2 — Draw conclusions
Heart Disease Analysis
Max Heart Rate Comparison: A non-parametric Mann-Whitney U test confirmed a highly significant difference ($p = 1.8010 \times 10^{-13}$). Healthy patients reached a noticeably higher maximum heart rate ($158.38 \pm 1.50$ SEM bpm) than heart-disease patients ($139.26 \pm 1.92$ SEM bpm).
Age vs. Heart Rate: Spearman rank correlation analysis yields a significant negative correlation ($r_s = -0.3916$, $p = 1.5189 \times 10^{-12}$). Maximum heart rate declines progressively as patient age increases.
Chemical-Exposure Mystery
Naive Finding: Initially, Cadmium appears strongly associated with tumor malignancy due to environmental grouping.
Controlled Finding: Once restricted to a controlled baseline group (Pollution index between 20 and 40), the Cadmium correlation collapses to $0.2434$, while the true driver, Benzene, shows a powerful correlation of $0.7662$.
Verdict: Benzene is the true causal driver of tumor malignancy. Cadmium's naive association was entirely spurious, driven by area pollution acting as a prominent confounding variable.