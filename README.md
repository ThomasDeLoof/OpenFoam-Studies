# OpenFOAM Learning Project

Welcome to my workspace dedicated to Computational Fluid Dynamics (CFD) with OpenFOAM. This repository documents my progress in fundamentals for aeronautical engineering.

<p align="center">
  <b>Turbulent viscosity distribution around a cylinder at Supercritical flow (Re=4.10^5)</b>
  <i>Validation: Cd ≈ 1.27 | St ≈ 0.26 | Residuals converged at 10⁻⁴</i>
</p>
<table align="center">
  <tr>
    <td align="center">
      <img src="studies/KarmanVortexStreetTurbulent/plots/Final_Nut_Re4e5.png" width="800px"/><br/>
    </td>
  </tr>
</table>

## Objective
The goal of this project is to master the complete CFD pipeline:

- **Pre-processing**: Mesh generation (essentially blockMesh & snappyHexMesh).

- **Solving**: Simulation using OpenFOAM solvers (icoFOAM, pimpleFOAM).

- **Post-processing**: Analysis and visualization using ParaView.

## Roadmap of Small Studies 
Here are the studies I'm conducting to validate my skills:

1. **Lid-Driven Cavity**: Validation of the OpenFOAM folder structure and understanding the vortex center with a typical case.

2. **2D Von Karman Vortices**: Importing a cylinder via STL and using `snappyHexMesh` to observe their influence on simple 2D streams (first laminar then turbulent).

3. **3D Wing Analysis**: Studying the behavior of a 3D stream around an airplane's wing and calculating aerodynamic responses.

## Tech Stack
- **OS**: macOS M1 (Workstation)
- **Container**: Docker (OpenFOAM-v2512)
- **Post-processing**: ParaView
- **Versioning**: Git / GitHub

---
*Project completed as part of my independent CFD learning.*
* **Linkedin:** https://www.linkedin.com/in/thomas-de-loof-319897328/
* **Contact:** Thomas.DE-LOOF@student.isae-supaero.fr

