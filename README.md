# OpenFOAM Learning Project

Welcome to my workspace dedicated to **Computational Fluid Dynamics (CFD)** with OpenFOAM. This repository documents my progress in fundamentals for aeronautical engineering.

## 🎯 Objective
The goal of this project is to master the complete CFD pipeline:

- **Pre-processing**: Mesh generation (blockMesh, Gmsh).

- **Solving**: Simulation using OpenFOAM solvers (icoFOAM, simpleFOAM).

- **Post-processing**: Analysis and visualization using ParaView.

## 🚀 Methodology
I work in an isolated **Docker** environment to ensure reproducibility, while versioning my configuration files with **Git**. I follow a bottom-up, iterative approach: understanding the mesh physics before adding complexity to the geometries.

## 🧪 Small Studies (Roadmap)
Here are the studies I'm conducting to validate my skills:

1. **Lid-Driven Cavity**: Validation of the OpenFOAM folder structure (`0/`, `constant/`, `system/`) and understanding the vortex center.

2. **Canal Obstacle**: Importing a cylinder via STL and using `snappyHexMesh` to observe the Von Kármán wake.

3. **Airfoil Analysis**: Studying the behavior of a 2D airfoil with Gmsh.

## 🛠️ Tech Stack
- **OS**: macOS M1 (Workstation)
- **Container**: Docker (OpenFOAM-v2512)
- **Post-processing**: ParaView
- **Versioning**: Git / GitHub

## 📊 Visualization
*(Add a screenshot of your cavity vortex here)*

---
*Project completed as part of my independent CFD learning.*
