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