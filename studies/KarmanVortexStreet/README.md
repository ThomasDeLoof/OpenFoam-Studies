# Case 2 : Von Karman Vortex Street Simulation

The calculation of the stream behind a cylinder is a well known CFD benchmark and has made me capture the open, unstationary cases of CFD in Openfoam.

## Progression & Study Outline
I first struggled with the fact that the cylinder needed to be larger (at least same height) as the fluid domain. I started by rescaling my cylinder STL file in meters (0.2m diameter, 0.05m height) using 'surfaceCheck' and 'surfaceTransformPoints' and creating a fluid domain respecting usual mimimum size to avoid edge effects (5xD in front and on the sides, 15xD behind, same height for 2D). 
Then the meshing crashed because I forced the refinement to stay in 2D by balancing cell levels, and snappyhexmesh crashed with the "10-point cell" error (common when snapping a single-layer mesh). I especially focused on keeping the cubic aspect of the cells (50mm sides), i.e. minimizing their aspect ratio, providing a stable foundation for the snappyHexMesh refinement. 

### Mesh Quality Validation
The command 'checkMesh' provided me a complete overview of the mesh created, allowing me to validate it against common standards:
*   **Non-Orthogonality:** Max $25.2^\circ$ (Well below the $65^\circ$ critical threshold), ensuring high numerical stability.
*   **Aspect Ratio:** $1.22$ (Optimal for resolving gradients).
*   **Skewness:** Successfully maintained within safe bounds for the PISO/PIMPLE algorithms.

### Result interpretation & validation
The first results at Re around 100 showcased total laminar and symmetric streams; I was able to then preserve the vortex structure by improving the meshing refinement especially near the cylinder;


I tried to match my results with those proposed in the article on **Vortices for rigid circular cylinders by Jonh H. Lienhard (1966)**, that provides an explanation for 6 different vortices regime depending on the Reynolds Number (in respect of the cylinder Diameter).

![Fig 1 : Regime of fluid flow across cylinders](plot/KarmanVortexRegimes.png)


---

## How to launch
Run this sequence in the openFoam terminal :
'''bash
blockMesh
surfaceFeatureExtract
snappyHexMesh -overwrite
checkMesh
icoFoam

./Allclean //to clean case and reload
