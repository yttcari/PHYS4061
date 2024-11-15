# Local library that contains code for generating lattice structure
import lab1lib

# User input section
"""
mode: 'fcc', 'bcc', 'sc', 'tetra'

a: arbitrary lattice constant
period: row matrix with periodicity in x, y, z axis
"""
mode = input("Please input the file you want (sc, bcc, fcc): ")

a = float(input("Please input lattice constant: "))

period = [0, 0, 0]
period[0] = int(input("Please input your period in x: "))
period[1] = int(input("Please input your period in y: "))
period[2] = int(input("Please input your period in z: "))

# generate lattice atom coordinate
"""
- df: matrix that stores the coordinate vectors of each atom
"""
if mode == 'sc':
    corner = input("What is the type of your corner atom? ")
    df = lab1lib.sc_lattice(a, period, corner)
elif mode == 'fcc':
    corner = input("What is the type of your corner atom? ")
    fcc = input("What is the type of your fcc atom? ")
    df = lab1lib.fcc_lattice(a, period, corner, fcc)
elif mode == 'bcc':
    corner = input("What is the type of your corner atom? ")
    bcc = input("What is the type of your bcc atom? ")
    df = lab1lib.bcc_lattice(a, period, corner, bcc)

lab1lib.write_xyz(df, f'lab3_datafile/{mode}.xyz')