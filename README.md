# ISSP/PEQS Classifier

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18625596.svg)](https://doi.org/10.5281/zenodo.18625596)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Python implementation of the **Information Self-Sufficiency Principle (ISSP)** with the **PEQS environmental filter** (v4.3.1).

Classifies galaxies into three dynamical states based on gravitational density:

**K = σ² / R_eff**  [km²/s²/kpc]

| Class | K Range | Description |
|-------|---------|-------------|
| **I_Pure_Relic** | K > 30 000, N_n = 0 | Isolated, DM-deficient (NGC 1277 type) |
| **I_Exogenous_Quasi-PI** | K > 30 000, N_n ≥ 1 | High-K induced by environment |
| **II_Balanced** | 1 000 < K ≤ 30 000 | Normal elliptics, moderate DM |
| **III_DM-Dependent** | K ≤ 1 000 | UDG-type, DM-dominated (Dragonfly 44) |

## Installation

```bash
pip install https://zenodo.org/record/18625596/files/issp_classifier_v0.2.0.zip

Quick start
python

from issp_classifier import classify_peqs

result = classify_peqs(sigma=250, R_eff_kpc=1.5, N_n=0)
print(f"K = {result['K']:.0f}")
print(f"Class: {result['class']}")

Live web tool

👉 ISSP & PEQS Quick Check
Interactive calculator — no Python required.

Reference

Murdasov, A. S. (2026). ISSP Classifier v4.3.1 with PEQS.
Zenodo. doi:10.5281/zenodo.18625596

License

Code: MIT
Data & methodology: CC BY 4.0
text