from math import exp, pi
from lab1lib import fcc_lattice

def LJPotential(r):
    """
    Calculate Lennard-Jones Potential 
    Argument:
    - r: distance between two atoms
    """
    return 4 / (r ** 12) - 4 / (r ** 6)

def BuckinghamPotential(r_ij, A_ij, B_ij, C_ij):
    """
    Calculate Buckingham Potential
    Argument:
    - Arbitrary constant: A_ij, B_ij, C_ij, unit please see README.md
    - r: distance between two ions in A

    return energy in eV
    """
    return (A_ij * exp(- r_ij / B_ij) - C_ij / (r_ij ** 6))

def CoulumbPotential(r_ij, Zi, Zj):
    """
    Calculate Coulumb potential
    Argument:
    - r_ij, distance between two ions in meter
    - Zi, Zj: effective charge of ions in unit of Coulumb

    return energy in eV
    """
    return (Zi * Zj  / (r_ij * (4 * pi * 8.854e-12))) / 1.6e-19

def NaCl_lattice(a, period):
    # As NaCl has alternate FCC lattice, two FCC lattices are generated
    Na_df = fcc_lattice(a, period, 'Na', 'Na')
    Cl_df = fcc_lattice(a, period, 'Cl', 'Cl')

    # Displaces Cl FCC lattice by 0.5a relative to Na FCC lattice
    # In order to obtain NaCl unit cell
    for row in Cl_df:
        row[1] += 0.5 * a

    # Concat the position list of Na ions and Cl ions
    df = Na_df + Cl_df
    return df
