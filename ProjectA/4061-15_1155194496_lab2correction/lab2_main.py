# Local library
import lab1lib
import mathlib
import lab2lib
import math

# function definition

def get_volume(a):
    """
    Get volume of the unit cell from lattice vector
    Argument:
    - a: 3x3 matrix, which is lattice vector in x, y, z direction
    """
    volume = mathlib.dot(a[0], mathlib.cross(a[1], a[2]))

    return volume

def PBC(n):
    """
    Apply periodic boundary condition to n
    Argument: 
    - n: row matrix of fractional coordinate with x, y, z elements
    """

    # Take mod of 1
    n = n % 1
    
    if n > 0.5:
        n -= 1
    elif n <= -0.5:
        n += 1
    return n

def frac2cart(n, A):
    """
    Transform fractional coordinate to cartesian coordinate
    Argument:
    - n: a row matrix of fractional coordinate with x, y, z elements
    - A: a 3x3 matrix that contains a1, a2, a3 in x, y, z direction
    """

    vec = []
    for i in range(3):
        # Calculate n dot A
        vec.append(n[0] * A[0][i] + n[1] * A[1][i] + n[2] * A[2][i])

    return vec

# Please use this function to test the PBC condition
def PBC_displacement(s, A, B):
    """
    Calculate cartesian displacement of vector after appling PBC
    Argument:
    - A: a 3x3 matrix that contains a1, a2, a3 in x, y, z direction
    - B: a 3x3 matrix that contains reciprocal lattice vector of A
    - s: a row matrix of vector difference
    """
    n = []
    for i in range(3):
        # Apply periodic condition on dot product of s and B
        n.append(PBC(mathlib.dot(s, B[i])))
    vec = frac2cart(n, A)

    return vec

def PBC_distance(vec1, vec2, A, B):
    distance = mathlib.get_mag(PBC_displacement(mathlib.vec_subtraction(vec1, vec2), A, B))

    return distance

def neighborcsv(df, N, A, B, cutoff, name='neighbor.csv'):
    """
    Generate "neighbor.csv" that recorded all neighbor of each atom
    Argument:
    - df: pandas dataframe that contains all the atom position in cartesian coordinate
    - N: total number of atoms
    - A: a 3x3 matrix that contains a1, a2, a3 in x, y, z direction
    - B: a 3x3 matrix that contains reciprocal lattice vector of A
    - cutoff: a scalar that set the cutoff distance for neighbor
    """
    lst = []
    for i in range(N):
        vec1 = df[i]
        vec1 = vec1[1:]

        for j in range(N):
            # Skip if two atoms are the same
            if i == j:
                continue

            # get values from i and j
            vec2 = df[j]
            vec2 = vec2[1:]

            # After getting displacement from PBC condition, get the magnitude of that displacement vector
            # round off to prevent overflow error
            distance = round(PBC_distance(vec1, vec2, A, B), 5)

            if distance <= cutoff and distance > 0:
                lst.append([i, j, distance])

    # Write file
    with open(name, "w", newline='') as f:
        f.write("Atom_Index, Neighbour_Index, distance\n")
        for row in lst:
            f.write(f"{row[0]},{row[1]},{row[2]}\n")

def get_reciprocal(a):
    """
    Get reciprocal vector from matrix a
    Argument:
    - a: a 3x3 matrix that contains a1, a2, a3 in x, y, z direction
    """
    for i in range(3):
        b = []

        # Get volume of the given a
        volume = get_volume(a)

        for i in range(3):
            lst = []
            # Calcuate a2xa3, a3xa1, a1xa2
            vec = mathlib.cross(a[(i+1) % 3], a[(i+2) % 3])

            # Divide each element by volume
            for j in range(3):
                lst.append(vec[j] / volume)

            b.append(lst) 
        return b
    
def construct_sim_box(period, a):
    """
    Following example in lab2.pptx
    Generate a simulation box with lattice in size of period[0] x period[1] x period[2]
    Argument:
    - period: a row matrix that contains the periodicity in x, y, z direction
    - a: lattice constant
    """

    A = [[period[0]*a, 0, 0],
     [0, period[1]*a, 0],
     [0, 0, period[2]*a]]

    B = get_reciprocal(A)

    return A, B

# Parameter input session
"""
mode: 'fcc', 'bcc', 'sc', 'tetra'

a: arbitrary lattice constant
period: row matrix with periodicity in x, y, z axis
"""
# Test for BCC and FCC
print("Testing for BCC and FCC reciprocal vector, assuming a = 1")
a = 1
FCC_A = [[0, a/2, a/2], [a/2, 0, a/2], [a/2, a/2, 0]]
FCC_B = get_reciprocal(FCC_A)
BCC_A = [[-a/2, a/2, a/2], [a/2, -a/2, a/2], [a/2, a/2, -a/2]]
BCC_B = get_reciprocal(BCC_A)

print(f"The FCC lattice vector is {FCC_A}, the reciprocal vector is {FCC_B}")
print(f"The BCC lattice vector is {BCC_A}, the reciprocal vector is {BCC_B}\n")

# User input
mode = input("Please input the file you want (sc, bcc, fcc): ")

a = float(input("Please input lattice constant: "))

# Cutoff for first nearest neighbour distance
cutoff = {'sc': a, 'fcc': a / math.sqrt(2), 'bcc': math.sqrt(3) * a / 2}

period = [0, 0, 0]
period[0] = int(input("Please input your period in x: "))
period[1] = int(input("Please input your period in y: "))
period[2] = int(input("Please input your period in z: "))

# Lattice Generation
"""
- df: matrix that stores the coordinate vector of each atom
- A: lattice vector of the selected mode
"""
if mode == 'fcc':
    df = lab1lib.fcc_lattice(a, period)
    A = [[0, a/2, a/2], [a/2, 0, a/2], [a/2, a/2, 0]]
elif mode == 'bcc':
    df = lab1lib.bcc_lattice(a, period)   
    A = [[-a/2, a/2, a/2], [a/2, -a/2, a/2], [a/2, a/2, -a/2]]
elif mode == 'sc':
    df = lab1lib.sc_lattice(a, period)
    A = [[a, 0, 0], [0, a, 0], [0, 0, a]]
elif mode == 'tetra':
    df = lab1lib.tetra_lattice(a, period)

print(f"The lattice vector is [{A[0]} {A[1]} {A[2]}]")
volume = get_volume(A)

B = get_reciprocal(A)
print(f"The reciprocal lattice vector is [{B[0]} {B[1]} {B[2]}]")

print(f"The volume of unit cell in {mode} is {volume}")

# Set Up Simulation Box
A, B = construct_sim_box(period, a)
# Write the neighbor file
# Round the cutoff to prevent overflow error
neighborcsv(df, len(df), A, B, round(cutoff[mode], 5), name=f"/Users/caritsang/Desktop/Project/PHYS4061/ProjectA/lab2_neighbourcsv/{mode}.csv")