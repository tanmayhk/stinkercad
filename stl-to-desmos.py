from stl import mesh
import numpy as np 
import sys
from environment import write

f = open(sys.argv[1] + "_stl.txt", "w")

write(f)

object = mesh.Mesh.from_file("./" + sys.argv[1] + ".stl")
obj_vectors = object.vectors

points = np.around(np.unique(obj_vectors.reshape([int(obj_vectors.size/3), 3]), axis=0),2)

for triangle in obj_vectors:
    coord0 = str([triangle[0][0], triangle[0][1], triangle[0][2]]).replace("]", "").replace("[", "")
    coord1 = str([triangle[1][0], triangle[1][1], triangle[1][2]]).replace("]", "").replace("[", "")
    coord2 = str([triangle[2][0], triangle[2][1], triangle[2][2]]).replace("]", "").replace("[", "")
    f.write("P(" + coord0 + "," + coord1 + "," + coord2 + ")\n")

f.close()