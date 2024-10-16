# Local library
import lab1lib
import lab2lib

# Parameter input session
"""
mode: 'fcc', 'bcc', 'sc', 'tetra'

a: arbitrary lattice constant
period: row matrix with periodicity in x, y, z axis
"""
mode = input("Please input the file you want (sc, bcc, fcc): ")

a = float(input("Please input lattice constant: "))

cutoff = float(input("Please input cutoff distance: "))

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

volume = lab2lib.get_volume(A)
print(f"The volume of unit cell in {mode} is {volume}")


# Set Up Simulation Box
"""
Following example in lab2.pptx
Generate a simulation box with lattice in size of period[0] x period[1] x period[2]
"""
A = [[period[0]*a, 0, 0],
     [0, period[1]*a, 0],
     [0, 0, period[2]*a]]

B = lab2lib.get_reciprocal(A)

# Write the neighbor file
lab2lib.neighborcsv(df, len(df), A, B, cutoff, name=f"lab2_neighbourcsv/{mode}.csv")