# Simple Molecular Dynamics Simulation of Lennard-Jones Fluids

This project presents a simple implementation of a Molecular Dynamics (MD) simulation using the Velocity-Verlet algorithm to generate the trajectories of a system containing 10 argon atoms. The study incorporates a velocity-rescaling thermostat to regulate temperature, performs rigorous energy tracking (kinetic, potential, and total energy), and provides visual trajectories of the atomic system.

## Tools Used

- `SciPy` – constants library for physical values and matrix operations
- `NumPy` / `Matplotlib` – for array manipulation, data storage, and energy profile plotting
- `mdtraj` / `py3Dmol` – for trajectory visualization

## Files Included

- `Simulation.ipynb` - Main Jupyter notebook containing the algorithm setup, execution, and data analysis.
- `Ar10.xyz` - Input file containing the initial Cartesian coordinates for the 10 argon atoms.
- `Ar10.pdb` - Protein Data Bank formatted file used for structural loading and visualization.
- `md.npz` - Compressed NumPy array file storing the raw trajectory and energy data from the baseline simulation.
- `md_thermostat.npz` - Compressed NumPy array file containing the data from the stabilized, thermostated simulation run.
