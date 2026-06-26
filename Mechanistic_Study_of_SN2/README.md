# Computational Mechanistic Study of S<sub>N</sub>2 Reaction

This project presents a computational investigation of the S<sub>N</sub>2 reaction mechanism between methyl chloride (CH₃Cl) and fluoride anion (F⁻), leading to the substitution product methyl fluoride (CH₃F). The study includes transition state (TS) search, intrinsic reaction coordinate (IRC) calculations, energy profile generation, and geometry analysis using Psi4 and Python.

## Reaction Overview

**CH₃Cl + F⁻ → CH₃F + Cl⁻**

This is a classic bimolecular nucleophilic substitution (S<sub>N</sub>2) reaction. The goal of this study is to calculate the potential energy surface (PES) and understand the changes in molecule geometry throughout the reaction path.

## Tools Used

- `Psi4` – quantum chemistry package for electronic structure and energy calculations
- `NumPy` / `Pandas` / `Matplotlib` / `py3Dmol` – for data analysis and visualization

## Workflow Summary

1. **Geometry Optimizations** at HF/6-31+G(d) for reactants, products, intermediates, and TS
2. **Frequency Calculations** to confirm Minima and TS (imaginary frequency)
3. **IRC Calculations** (forward and backward) to confirm connection between minima and TS
4. **Single Point Energy Calculations** at MP2/6-31++G(d,p) level
5. **Zero-Point Energy (ZPE) Corrections**
6. **Potential Energy Surface (PES) Plot** of reaction path

## Files Included

- `SN2_Reaction.ipynb` - Main notebook with all code and analysis
- `TS_animation.gif` - GIF file of TS vibration animation
- `output.dat` - Output file from Psi4 calculations 
- `*.molden_normal_modes` - Output file from frequency calculation for visualization of vibrational modes   
