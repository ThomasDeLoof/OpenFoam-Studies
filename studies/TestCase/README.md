# Test Case : Lid-Driven Cavity Flow

## Objective
The purpose of this simulation is to validate the setup of the `icoFoam` solver by modeling the classic 2D lid-driven cavity flow. 

## Methodology
* **Solver:** `icoFoam` (Transient solver for incompressible, laminar flow of Newtonian fluids).
* **Mesh:** Structured hexahedral mesh generated with `blockMesh`.
* **Boundary Conditions:**
    * **Top wall:** Moving wall (velocity = 1.0 m/s).
    * **Other walls:** No-slip condition (velocity = 0 m/s).
    * **Pressure:** Zero-gradient at all walls.

## Results
The simulation successfully reached a steady-state velocity field. The primary vortex is clearly visible at the center of the cavity.

## Observations
![Velocity Field](plots/ArrowGlyph.png) 
*Figure 1: Velocity magnitude contours showing the primary vortex formation for Re=1000.*

- **Vortex Characterization:** The primary vortex center location seems to fit the standard literature results for each Reynolds number (I compared with the Ghia et al. 1982 article)
- **Boundary Layer:** A clear boundary layer is observed along the moving top wall, as expected in viscous flow regimes.

## How to run
1. Navigate to the case directory.
2. Run `blockMesh`.
3. Run `icoFoam`.
4. Post-process using `paraFoam` or open TestCase.foam in paraview
