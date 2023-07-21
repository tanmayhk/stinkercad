from stl import mesh
import numpy as np 
import sys
import extrusion

f = open(sys.argv[1] + "_stl.txt", "r")

fin_list = []
for line in f.readlines():
    if line[0] == "P" and "M" not in line:
        x = line.replace("P", "").replace(")", "").replace("(", "").replace("\\right)", "").replace("\left(", "")
        x = [i.replace(" ", "").replace("\n", "") for i in x.split(",")]
        fin_list.append([[x[0], x[1], x[2]], [x[3], x[4], x[5]], [x[6], x[7], x[8]]])
    if line[0:5] == "e_{x}" and "M" not in line:
        x = line.replace("e_{x}", "").replace(")", "").replace("(", "").replace("\\right)", "").replace("\left(", "")
        x = [i.replace("\n", "") for i in x.split(",")]
        x = [float(i) for i in x]
        extrusion_polygons = extrusion.e_x(*x)
        actual_triangles = []
        for poly in extrusion_polygons:
            triangles_per_poly = [[str(poly[i]), str(poly[i + 1]), str(poly[i + 2])] for i in range(0, len(poly), 3)]
            actual_triangles.append(triangles_per_poly)
        fin_list = fin_list + actual_triangles

num_triangles=len(fin_list)
data = np.zeros(num_triangles, dtype=mesh.Mesh.dtype)
for i in range(num_triangles):
    data["vectors"][i] = np.array([fin_list[i][0], fin_list[i][1], fin_list[i][2]])

m=mesh.Mesh(data)
m.save(sys.argv[2] + '.stl')