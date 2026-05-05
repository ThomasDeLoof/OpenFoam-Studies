lc = 0.1;

// Domaines
Point(1) = {-2, -1, 0, lc};
Point(2) = {8, -1, 0, lc};
Point(3) = {8, 1, 0, lc};
Point(4) = {-2, 1, 0, lc};

// Lignes du canal
Line(1) = {1, 2}; // Mur bas
Line(2) = {2, 3}; // Outlet
Line(3) = {3, 4}; // Mur haut
Line(4) = {4, 1}; // Inlet

// Cylindre centré en (0,0)
Point(5) = {0, 0, 0, lc/2};
Point(6) = {0.5, 0, 0, lc/2};
Point(7) = {-0.5, 0, 0, lc/2};

Circle(5) = {6, 5, 7};
Circle(6) = {7, 5, 6};

// Surfaces
Curve Loop(1) = {1, 2, 3, 4};
Curve Loop(2) = {5, 6};
Plane Surface(100) = {1, 2};//+
Physical Curve("inlet", 1) = {4};
//+
Physical Curve("outlet", 2) = {2};
//+
Physical Curve("walls", 3) = {3, 1};
//+
Physical Curve("cylinder", 4) = {5, 6};
//+
Physical Surface("fluid", 5) = {100};
