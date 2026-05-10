# Case 2b: Von Karman Turbulent Vortex Street Simulation 

## Mesh refinement
To fully capture the turbulent boundary layer and vortices, I have refined the meshing merely quadrupling the number of cells (especially in the near wake zone).
* Total cell number : approx. 1.2 million
* Number of boundary layers : 6+
* Max aspect ratio = 4.97956 OK.
* Max skewness = 0.386238 OK.
* Mesh non-orthogonality Max: 38.0647 average: 4.40876

## Parallel Processing
To espect around 2 to 3 times faster calculations, I compensated the addition of cells with parallel processing thanks to my Apple Silicon M1 SoC and used 4 processors with each around 300k cells in their respective subdomains.

## How to Launch
Run this sequence in your OpenFOAM terminal:

```bash
# Mesh generation
blockMesh
surfaceFeatureExtract
snappyHexMesh -overwrite
checkMesh

# Execution
foamListTimes -rm && rm -rf postProcessing # To remove previous runs
decomposePar # parallel processing initiation
mpirun --allow-run-as-root -np 4 pimpleFoam -parallel > log.pimpleFoam & # WARNING : running as root is strongly discouraged if not in a isolated environment like Docker containers
tail -f log.pimpleFoam # To live track the run
reconstructPar # parallel processing ending (do not forget)


# Clean-up to reload (Utility script)
mv log.pimpleFoam final_calculation.log # To register converged results
rm -rf processor* # To remove parallel processing files
./CleanMesh # To restart meshing
