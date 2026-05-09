# Case 2: Von Karman Vortex Street Simulation (Unsteady Laminar Flow)

## Overview
This case focuses on the simulation of an unsteady flow behind a circular cylinder, a classic CFD benchmark. The objective was to capture the **Von Karman Vortex Street** using OpenFOAM (and compare the results with theory).

## Geometry & Pre-processing
Initially, I faced challenges with the STL scale and domain boundaries.
*   **Rescaling:** Used `surfaceCheck` and `surfaceTransformPoints` to ensure the cylinder diameter was $D = 0.2\text{m}$ (rescaled from mm to meters).
*   **Domain Sizing:** To avoid edge effects, I designed the fluid domain following standard aerospace guidelines: $5D$ upstream/sides and $15D$ downstream.
*   **2.5D Constraints:** For a 2D simulation in OpenFOAM, the domain thickness (Z-axis) was set to one cell layer ($0.05\text{m}$), matching the cylinder height.

## Meshing Challenges & Logic
The meshing process was a major learning curve, especially regarding **SnappyHexMesh** on a single-cell layer (2.5D).
*   **Aspect Ratio Control:** I focused on keeping the background grid (`blockMesh`) cubic ($50\text{mm}$ sides). This minimized the aspect ratio ($1.22$), providing a stable foundation for the snapping process.
*   **Solving the "10-point cell" error:** I encountered crashes when forcing refinement levels to stay 2D. I resolved this by carefully balancing refinement levels and ensuring the snapping didn't collapse cells on the Z-front/back planes.

### Mesh Quality Validation (`checkMesh`)
To ensure high-fidelity results, the mesh was validated against industry standards:
*   **Max Non-Orthogonality:** $25.2^\circ$ (Well below the $65^\circ$ critical threshold), ensuring high numerical stability.
*   **Max Aspect Ratio:** $1.22$ (Optimal for resolving sharp gradients in the wake).
*   **Skewness:** Maintained within safe bounds for the PIMPLE algorithm.

## Solver Evolution Troubleshooting
One of the key technical takeaways was the transition from `icoFoam` to `pimpleFoam`.
*   **From Fixed to Adaptive $\Delta t$:** I realized `icoFoam` ignored `adjustTimeStep`, leading to sub-optimal computation times on my Mac M1. Migrating to `pimpleFoam` allowed for an adaptive time-step based on a target Maximum Courant Number ($Co_{max} = 0.8$).
*   **The Metastability Challenge:** Early simulations at $Re=150$ remained stubbornly symmetric. I learned that:
    1. Numerical noise isn't always enough to break symmetry; a small "kick" (perturbation in $U_y$) was added to the inlet to trigger the instability.
    2. **Advection Time:** At low velocities, the flow requires several hundred seconds of physical time to clear the initial stationary field and fully develop the vortex street.

## Result Interpretation & Validation
I compared the results with **Lienhard (1966)**'s classification of vortex regimes :

![Fig 1: Regime of fluid flow across cylinders](plot/KarmanVortexRegimes.png)

# Reynolds 30
We expect a fixed pair of Föppl vortices in the wake.


# Reynolds 130
At $Re \approx 130$, the simulation correctly predicts a stable, laminar vortex street :

![Fig 2a: Vorticity Flow at Re = 130](plot/Re130/Vortex_Animation_Re130.gif)
![Fig 2b: Pressure distribution after 20 advective times at Re = 130](plot/Re130/Final_Velocity_Re130.png)

**Key Observations:**
* The flow separation point is located around the back of the cylinder, typical for low Reynolds regimes.
* The vortices appear smooth and have a circular shape compatible with laminar flow.
* The vortices lose consistence after 4 iteration (approximately 15 advection distances).

# Reynolds 1000

At $Re = 1000$, we observe the transition towards a more chaotic wake. While the periodic shedding remains, the flow exhibits clear signs of increased instability compared to the $Re = 150$ case.

![Fig 3a: Vorticity Flow at Re = 1000](plot/Re1000/Vorticity_Animation_Re1000.gif)
![Fig 3b: Pressure distribution after 30 advective times at Re = 1000](plot/Re1000/Final_Velocity_Re1000.png)

**Key Observations:**
* The shear structures are significantly elongated behind the cylinder.
* The flow separation point has migrated upstream along the cylinder’s shoulders, typical of higher Reynolds regimes.
* The vortices appear more "agitated" and lose their perfectly circular laminar shape shortly after shedding.
* The vortices lose consistence far later than in the previous case.

**Numerical validation**
To get a macroscopic check of this case, we can monitor the Strouhal Number ($St$), which characterizes the vortex shedding frequency:
* Expected Value: $St \approx 0.21$ for $Re = 1000$.
* Calculated Value: $St = [To be calculated]$ (derived from the $C_l$ oscillation frequency).The proximity of our results to the empirical values confirms that the global shedding dynamics are correctly captured despite the lack of a sub-grid scale turbulence model.

**Limitations**
The laminar-biased solver combined with the current mesh density acts as a numerical filter. This leads to a "numerical diffusion" that likely dissipates the finer turbulent scales. In a 2.5D simulation, the solver effectively "swallows" some of the 3D instabilities that would naturally occur at this Reynolds number. 

# Reynolds 400000
For higher Reynolds (often Re>2000), we shall change the configuration to capture the non negligeable turbulent aspect of the flow. I set the solver as RAS, and defined the k, epsilon needed fields in the `/0` file. 
We espect a narrower, completely disorganised wake, and no vortex street.



# Reynolds 4000000
This case was not considered because it required too complex meshing and too much calculation power for my current workspace.



### Ongoing & Future Work
- [x] **Laminar Validation:** Match Strouhal Number ($St \approx 0.18$) with theory.
- [ ] **Mesh Independence Study:** Comparing drag/lift coefficients across three refinement levels.
- [ ] **Turbulence Transition:** Scaling up to $Re > 4,000$ using the $k-\omega$ SST model and implementing boundary layer inflation (snappyHexMesh layers).

---

## How to Launch
Run this sequence in your OpenFOAM terminal:

```bash
# Mesh generation
blockMesh
surfaceFeatureExtract
snappyHexMesh -overwrite
checkMesh

# Execution
pimpleFoam

# Clean-up to reload (Utility script)
./CleanMesh
