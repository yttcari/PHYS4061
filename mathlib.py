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
    Conduct vector subtraction
    Argument:
    - vec1: row matrix with shape 3
    - vec2: row matrix with shape 3
    """
    vec = []
    for i in range(3):
        vec.append(vec1[i] - vec2[i])

    return vec