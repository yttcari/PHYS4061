from mathlib import get_mag, dot, vec_subtraction, vec_addition, vec_scale
import csv
import lab3lib

def d_LJ(vec, mode):
    # As the form of dx, dy, dz LJ are the same
    # coor can be input as x (or y or z) coordinate
    # depending on which axis is derivating wrt.
    if mode == 0:
        coor = vec[0]
    elif mode == 1:
        coor = vec[1]
    elif mode == 2:
        coor = vec[2]
    
    length = get_mag(vec)
    if length == 0:
        return 0
    else:
        dx = -(- 48 * coor / length ** 14 + 24 * coor / length ** 8)
        return dx

def grad_LJ(vec):
    return [d_LJ(vec, 0), d_LJ(vec, 1), d_LJ(vec, 2)]

def get_alpha(vec, mode, sigma=0.0001):
    h = vec_scale(-1, grad_LJ(vec))
    numerator = grad_LJ(vec)[mode] ** 2
    d_vec = vec
    vec[mode] += sigma * h[mode]
    print(vec, d_vec)
    denominator = grad_LJ(vec)[mode] - grad_LJ(d_vec)[mode]

    if denominator == 0:
        return 0
    else:
        return -sigma * numerator / denominator

def get_LJ(name, N):
    # name: path for neighbour csv
    with open(name, newline='') as f:
        df = csv.reader(f, delimiter=',')

        # Skip first line (i.e. header) of flie
        header = next(df, None)

        energy = 0

        for row in df:
            # Only consider when neighbour index > atom index to prvent double count
            if int(row[1]) > int(row[0]):
                
                # distance (LJ unit) = distance (A) / 3.4
                energy += lab3lib.LJPotential(float(row[2])/3.4)

        # Energy (eV) = Energy (LJ unit) * 1.65e-21 / 1.6e-19 (Charge of electron)
        energy = energy * 1.65e-21 / 1.6e-19

        # Transform energy from eV to meV per atom
        energy_per_atom = energy * 1e3 / N

    return energy, energy_per_atom

def SteepestDecent(vec):
    for i in range(3):
        alpha = get_alpha(vec=vec, mode=i)
        print(alpha)
        vec[i] += alpha * grad_LJ(vec)[i]

    return vec
