def write(text_file):
    # Variables
    text_file.write("z_{c}=1\n")
    text_file.write("y_{f}=1\n")
    text_file.write("a = 0\n")
    text_file.write("(0, a) \n")
    text_file.write("C=\left(0,\ 0\\right)\n")

    # Projection function
    text_file.write("D(P_x, P_y, P_z) = (((P_x - C.x) * ((P_z - z_c)/z_c)) + C.x, ((P_y - C.y) * ((P_z - z_c)/z_c)) + C.y)\n")

    # Rotation functions
    text_file.write("R_x(x, y, z) = x\n")
    text_file.write("R_y(x, y, z) = ycos(a) - zsin(a)\n")
    text_file.write("R_z(x, y, z) = ysin(a) + zcos(a)\n")

    # Polygon and combined plotting function
    text_file.write("f(x) = polygon(x)\n")
    text_file.write("P(M_1, M_2, M_3, N_1, N_2, N_3, O_1, O_2, O_3) = f([D(R_x(M_1, M_2, M_3), R_y(M_1, M_2, M_3), R_z(M_1, M_2, M_3)), D(R_x(N_1, N_2, N_3), R_y(N_1, N_2, N_3), R_z(N_1, N_2, N_3)), D(R_x(O_1, O_2, O_3), R_y(O_1, O_2, O_3), R_z(O_1, O_2, O_3))])\n")

    # Extrusion functions
    text_file.write("X_1(M_1, M_2, M_3, N_1, N_2, N_3) = M_2*N_3 - M_3*N_2\n")
    text_file.write("X_2(M_1, M_2, M_3, N_1, N_2, N_3) = M_3*N_1 - M_1*N_3\n")
    text_file.write("X_3(M_1, M_2, M_3, N_1, N_2, N_3) = M_1*N_2 - M_2*N_1\n")

    text_file.write("e_x(M_1, M_2, M_3, N_1, N_2, N_3, O_1, O_2, O_3, d) = [P(M_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)), P(N_1, N_2, N_3, M_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)), P(M_1, M_2, M_3, N_1, N_2, N_3, M_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)), P(O_1, O_2, O_3, N_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)), P(N_1, N_2, N_3, O_1, O_2, O_3, N_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), N_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)), P(M_1, M_2, M_3, O_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), M_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)), P(O_1, O_2, O_3, M_1, M_2, M_3, O_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), O_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3))]\n")