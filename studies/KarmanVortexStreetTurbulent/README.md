# Case 2b: Von Karman Turbulent Vortex Street Simulation 

## Mesh Quality & Validation
To capture the turbulent boundary layer and the complex wake dynamics, the mesh density was quadrupled compared to the laminar case, focusing specifically on the **near-wake region**.

**Key `checkMesh` Statistics:**
* **Cell Count:** ~1.2 million cells
* **Boundary Layers:** 6+ layers with high-resolution near-wall refinement.
* **Max Aspect Ratio:** 4.98 (Well within stability limits).
* **Max Skewness:** 0.38 (Excellent cell orthogonality).
* **Non-Orthogonality:** Max 38.06° / Average 4.41° (Highly stable for PIMPLE/PISO solvers).

> **Verification:** Post-run analysis confirmed a **$y^+ \approx 1$** across the cylinder surface. This validates the near-wall resolution, ensuring the $k-\omega$ SST model accurately solves the viscous sublayer without relying solely on wall functions.

## High-Performance Computing 
The simulation was optimized for the **Apple Silicon M1 SoC** using parallel processing:
* **Domain Decomposition:** 4 sub-domains (approx. 300k cells per core).
* **Speed-up:** Achieved a $2.5\times$ to $3\times$ reduction in wall-clock time compared to serial execution.
* **Method:** Simple geometric decomposition for balanced CPU load.

## Turbulence Modeling
I implemented the **$k-\omega$ SST (Shear Stress Transport)** model, chosen for its superior performance in predicting flow separation under adverse pressure gradients.

* **Field Initialization:** Configured `k`, `omega`, and `nut` in the `0/` directory.
* **Numerical Schemes:** Used second-order schemes for divergence and gradients to balance stability and accuracy.
* **Philosophy:** While the simulation is 2D, the SST model provides a Reynolds-Averaged (RANS) approximation of the 3D energy cascade through the turbulent viscosity ($\nu_t$).

## Results & Physical Analysis
At $Re = 4 \cdot 10^5$, the flow is in the **high-Reynolds regime**. 

**Observations:** The 2D constraint preserves a coherent vortex street structure. While 3D instabilities (vortex stretching) are not explicitly resolved, the turbulent Viscosity ($\nu_t$) field clearly shows massive production in the wake, accounting for the energy dissipation of the chaotic flow.

<p align="center">
  <b>Turbulent flow across cylinder at Re 4e5</b>
</p>
<table align="center">
  <tr>
    <td align="center">
      <img src="plots/Final_Nut_Re4e5.png" width="500px"/><br/>
      <sub>(a) Turbulent Viscosity ($\nu_t$) Distribution (25 advective times)</sub>
    </td>
    <td align="center">
      <img src="plots/Final_Vorticity.png" width="500px"/><br/>
      <sub>(b) Vorticity Distribution (25 advective times)</sub>
    </td>
  </tr>
</table>

**Quantification:** Beyond visualization, the simulation was validated through :
* The convergence of residuals (see log.pimpleFoam)
* The analysis of the drag coefficient ($C_d$): this Reynold should be the threshold for the theoretical "drag fall" , which was indeed seen here : $C_d \approx 0.3$.
* The Stouhal number that was validated : $S_t \approx 0.5$

## How to Launch


```bash
# Pre-processing (Mesh)
blockMesh
surfaceFeatureExtract
snappyHexMesh -overwrite
checkMesh

# Execution (parallel)
# Clean previous results & decompose
foamListTimes -rm && rm -rf postProcessing
decomposePar 
# Run the solver (Optimized for Docker/M1)
mpirun --allow-run-as-root -np 4 pimpleFoam -parallel > log.pimpleFoam &
# Live-track convergence
tail -f log.pimpleFoam

# Post-Processing
# Reconstruct sub-domains for ParaView
reconstructPar 
# Optional: Clean up to save disk space (Mac SSD safety)
mv log.pimpleFoam final_calculation.log
rm -rf processor*
