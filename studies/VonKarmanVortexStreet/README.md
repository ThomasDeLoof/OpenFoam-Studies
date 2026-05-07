# Case 2 : Von Karman Vortex Street Simulation

The calculation of the stream behind a cylinder is a well known CFD benchmark and has made me capture the open, unstationary cases of CFD in Openfoam.

## Progression & Study Outline

### 2. Advanced Meshing Strategy (The "Snappy" Challenge)
*   **Background Mesh:** I started by rescaling my cylinder STL file in meters (0.2m diameter, 0.05m height) using 'surfaceCheck' and 'surfaceTransformPoints' and creating a fluid domain respecting usual mimimum size to avoid edge effects (5xD in front and on the sides, 15xD behind, same height for 2D). I especially focused on the cubic aspect of the cells (50mm sides), providing a stable foundation for the snappyHexMesh refinement.
* **octree refinement conflicts** I forced the refinement to stay in 2D by balancing cell levels to prevent the "10-point cell" error (common when snapping a single-layer mesh). 

### 3. Mesh Quality Validation (`checkMesh`)
The resulting mesh was validated against common standards:
*   **Non-Orthogonality:** Max $25.2^\circ$ (Well below the $65^\circ$ critical threshold), ensuring high numerical stability.
*   **Aspect Ratio:** $1.22$ (Optimal for resolving gradients).
*   **Skewness:** Successfully maintained within safe bounds for the PISO/PIMPLE algorithms.



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