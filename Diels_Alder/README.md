# Computational Analysis of Diels–Alder Reaction

This project explores the reactivity and orbital interactions in Diels–Alder (DA) reactions through quantum chemical calculations using Psi4 and Python. It focuses on the effect of substituents on frontier molecular orbitals (FMOs), rotational conformers, and energy gaps. The study includes geometry optimization, orbital energy calculation, potential energy surface (PES) scans, and 3D visualization of molecular orbitals.

## 🛠 Tools Used

- `Psi4` – quantum chemistry package for electronic structure and energy calculations  
- `NumPy` / `Matplotlib` / `RDKit` / `py3Dmol` – for data analysis and visualization 

## 🧪 Project Structure

**Part 1: Effect of Dienophile Electron Deficiency on Diels–Alder Reaction Rates**  
- Performed geometry optimizations of various substituted ethene dienophiles and calculated LUMO energies.
- Plotted LUMO energies against reaction rates to reveal the correlation between electron-withdrawing substituents and DA reactivity.

**Part 2: Potential Energy Surface Scan of Diene Rotation Around Central Bond**  
- Conducted a PES scan by varying the dihedral angle around the central C–C bond of different 1,3-butadiene derivatives
- Performed transition state and minimum geometry optimizations to determine the rotational activation barrier.

**Part 3: Normal vs. Inverse Electron Demand in the DA Reaction**  
- Analyzed HOMO/LUMO energy levels of dienes and dienophiles to predict whether normal or inverse electron demand dominates based on substituent effects.

**Part 4: Visualization of the Frontier Molecular Orbitals**
- Visualized HOMO/LUMO orbitals to assess phase symmetry and orbital overlap compatibility.

## 📁 Folder Contents

- `Diels_Alder_Reaction.ipynb` - Main notebook with all analysis and plots  
- `molecule/` - Input geometries in Z-matrix for calculations  
- `orbital/` - Cube and xyz files for orbital visualization
- `media/` - Figures used in the notebook
