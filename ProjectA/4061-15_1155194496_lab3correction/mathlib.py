from math import acos, sqrt

def dot(a,  b):
    """
    Conduct dot product on the two row matrix a and b
    Argument:
    - a: row matrix of shape 3
    - b: row matrix of shape 3
    """
    result = 0
    for i in range(3):
        result += a[i] * b[i]

    return result

def cross(a, b):
    """
    Conduct cross product on two 3x3 matrix
    Argument:
    - a: 3x3 matrix
    - b: 3x3 matrix

    Return: row matrix of shape 3
    """
    # Conduct cross product
    answer = [a[1]*b[2] - a[2]*b[1], 
              a[2]*b[0] - a[0]*b[2], 
              a[0]*b[1] - a[1]*b[0]]

    return answer


def vec_subtraction(vec1, vec2):
    """
    Conduct vector subtraction vec1 - vec2
    Argument:
    - vec1: row matrix with shape 3
    - vec2: row matrix with shape 3
    """
    vec = []
    for i in range(3):
        vec.append(vec1[i] - vec2[i])

    return vec

def get_mag(vec):
    """
    Get magnitude of a vector
    Argument:
    - vec: a row matrix that contains the vector elements
    """
    distance = 0
    for i in range(3):
        # Calculate x^2 + y^2 + z^2
        distance += (vec[i]) ** 2

    return sqrt(distance)

def get_angle(a, b):
    """
    Get angle in between two vector
    Argument:
    - a: cartesian position (x, y, z) of atom a
    - b: cartesian position (x, y, z) of atom b
    """

    mag_a = round(get_mag(a), 10) # magnitude of a, round to 10th digit to prevent floating point error
    mag_b = round(get_mag(b), 10) # magnitude of b, round to 10th digit to prevent floating error

    return acos(dot(a, b) / (mag_a * mag_b))