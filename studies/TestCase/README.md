# Test Case : Lid-Driven Cavity Study

## Project Overview
The Lid-Driven Cavity is a classic benchmark in fluid dynamics, that I used here to validate my simulation setup and my comprehension of CFD basics. The goal was to solve the incompressible Navier-Stokes equations at different Reynolds numbers and compare the results with the established benchmark data from **Ghia et al. Solutions for incompressible flows (1982)**.

## Difficulties and progression

Troughout this study, I first struggled with basic problems in CFD. My results were often physically impossible because of simple details, that I improved by:

1.  **Mesh Grading & Sizing**: Used `simpleGrading` to achieve a fine cell distribution near the walls, because the boundary layer dynamics were not precise enough. At the same time I increased the total cell number that was initially too low. I then remembered that along with this modification it was vital to adapt the time step to avoid "parameters jumps", so I added a command in the controlDict file that adjusts time step automatically in regards of the Courant–Friedrichs–Lewy condition.
2.  **Discretization Schemes**: Shifted from dissipative `upwind` schemes to **`linearUpwind`**, in order to keep the vortex information that I wanted to study.
3.  **Solver Convergence**: Refined the `PISO` loop settings, specifically using `nCorrectors 3` and `nNonOrthogonalCorrectors 1` that limit very high gradients to erase the discontinuities, especially at the corners (that were still present for low Reynolds unfortunately).
4.  **Physical Steady-State**: I also identified that the vortex developpement required a sufficiently long simulation time (`endTime = 30s`) to reach a stable state, instead of my initial very low total time of 1s.

## Visual Validation 

After these improvements, the simulation was successfull and I was able to perfectly visualize these vortices thanks to the Stream Line filter of Paraview. The results are visually the same as the benchmark (p 14 to 16), which confirms accuracy and code validity.

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
