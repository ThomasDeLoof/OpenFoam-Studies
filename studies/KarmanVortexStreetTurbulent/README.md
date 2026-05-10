# Case 2b: Von Karman Turbulent Vortex Street

# Reynolds 4000
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
decomposePar # parallel processing
mpirun -np 4 pimpleFoam -parallel
tail -f log.pimpleFoam # live tracking of the calculations (optional)
reconstructPar

# Clean-up to reload (Utility script)
./CleanMesh
