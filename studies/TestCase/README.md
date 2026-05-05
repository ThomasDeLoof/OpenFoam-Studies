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

### Velocity Magnitude Field
![Velocity Field](path/to/your/image.png) 
*Figure 1: Velocity magnitude contours showing the primary vortex formation.*

### Convergence Analysis
The residuals dropped below the $10^{-5}$ threshold, indicating numerical convergence.

## Observations
- **Vortex Characterization:** The primary vortex center is located at approximately (0.5, 0.75) within the cavity, which is consistent with standard literature results for $Re=100$.
- **Boundary Layer:** A clear boundary layer is observed along the moving top wall, as expected in viscous flow regimes.

## How to run
1. Navigate to the case directory.
2. Run `blockMesh`.
3. Run `icoFoam`.
4. Post-process using `paraFoam` or extract data with `postProcess -func sample`.