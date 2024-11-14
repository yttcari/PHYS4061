import mathlib

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

def neighborcsv(df, N, A, B, cutoff, name='neighbor.csv', write=False):
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
    if write:
        with open(name, "w", newline='') as f:
            f.write("Atom_Index, Neighbour_Index, distance\n")
            for row in lst:
                f.write(f"{row[0]},{row[1]},{row[2]}\n")
    else:
        return lst

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