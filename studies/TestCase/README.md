# Test Case : Lid-Driven Cavity Study

## Project Overview
The Lid-Driven Cavity is a classic benchmark in fluid dynamics, that I used here to validate my simulation setup and my comprehension of CFD basics. The goal was to solve the incompressible Navier-Stokes equations at different Reynolds numbers and compare the results with the established benchmark data from **Ghia et al. Solutions for incompressible flows (1982)**.

## Difficulties and progression

Throughout this study, I first encountered with common CFD challenges and the results were often physically inconsistent. However I managed to improve them by:

1.  **Mesh Grading & Sizing**: Used simpleGrading to achieve a fine cell distribution near the walls, because the boundary layer dynamics were not precise enough. At the same time I increased the total cell number that was initially too low. I then remembered that along with this modification it was vital to adapt the time step to avoid "parameters jumps", so I added a command in the controlDict file that adjusts time step automatically in regards of the CFL condition.
2.  **Discretization Schemes**: Shifted from dissipative upwind schemes to linearUpwind, which preserves better the flow structures (vortices).
3.  **Solver Convergence**: Refined the PISO loop settings (nCorrectors 3, nNonOrthogonalCorrectors 1) and gradient limiters in order to stabilize the solution and reduce numerical oscillations caused by the lid-corner velocity singularity (that was still a bit present for low Reynolds unfortunately).
4.  **Physical Steady-State**: I realized that the vortex development required a sufficiently long simulation time (endTime = 30s) to reach a stable state, instead of my initial very low total time of 1s.

## Visual Validation 

After these improvements, the simulation was successful and I was able to capture the primary vortex migration and the secondary Moffatt vortices in the corners thanks to the Stream Line filter of Paraview. The results show strong agreement with the benchmark, which confirms accuracy and code validity.

<p align="center">
  <b>Fig. 1: CFD results visualisation using Paraview</b>
</p>
<table align="center">
  <tr>
    <td align="center">
      <img src="plots/Result_Re_100.png" width="350px"/><br/>
        <sub>(a) Stream Lines at Re = 100</sub>
    </td>
    <td align="center">
      <img src="plots/Result_Re_1000.png" width="350px"/><br/>
        <sub>(b) Stream Lines at Re = 1000</sub>
    </td>
    <td align="center">
      <img src="plots/Result_Re_10000.png" width="350px"/><br/>
        <sub>(c) Stream Lines at Re = 10000</sub>
    </td>
  </tr>
</table>

<p align="center">
  <b>Fig. 2: Benchmark theoretical solutions</b>
</p>
<table align="center">
  <tr>
    <td align="center">
      <img src="plots/Gia&al_Re_100" width="350px"/><br/>
        <sub>(a) Stream Lines at Re = 100</sub>
    </td>
    <td align="center">
      <img src="plots/Gia&al_Re_1000" width="350px"/><br/>
        <sub>(b) Stream Lines at Re = 1000</sub>
    </td>
    <td align="center">
      <img src="plots/Gia&al_Re_10000" width="350px"/><br/>
        <sub>(c) Stream Lines at Re = 10000</sub>
    </td>
  </tr>
</table>

## How to use
The configuration files are organized in the `/system` and `/constant` directories.
Run the simulation using:
```bash
blockMesh
icoFoam
parafoam (to view in paraview)
(or touch TestCase.foam and open it with the software)
