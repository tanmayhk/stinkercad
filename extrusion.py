def X_1(M_1, M_2, M_3, N_1, N_2, N_3):
    return M_2*N_3 - M_3*N_2

def X_2(M_1, M_2, M_3, N_1, N_2, N_3):
    return M_3*N_1 - M_1*N_3

def X_3(M_1, M_2, M_3, N_1, N_2, N_3):
    return M_1*N_2 - M_2*N_1

def e_x(M_1, M_2, M_3, N_1, N_2, N_3, O_1, O_2, O_3, d):
    return [[M_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              M_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              M_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              N_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              N_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              N_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              O_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              O_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              O_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)], 
            [N_1, N_2, N_3, M_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              M_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              M_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              N_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              N_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              N_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)], 
            [M_1, M_2, M_3, N_1, N_2, N_3, 
              M_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              M_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              M_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)], 
            [O_1, O_2, O_3, N_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              N_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              N_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              O_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              O_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              O_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)], 
            [N_1, N_2, N_3, O_1, O_2, O_3, 
             N_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
             N_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
             N_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)],
            [M_1, M_2, M_3, O_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
             O_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
             O_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
             M_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
             M_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
             M_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)], 
            [O_1, O_2, O_3, M_1, M_2, M_3,
              O_1 + d*X_1(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              O_2 + d*X_2(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3), 
              O_3 + d*X_3(O_1 - M_1, O_2 - M_2, O_3 - M_3, N_1 - M_1, N_2 - M_2, N_3 - M_3)]]