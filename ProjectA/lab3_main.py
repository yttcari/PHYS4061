from lab2lib import construct_sim_box, PBC_distance, neighborcsv
from lab1lib import fcc_lattice
import lab3lib
import csv

# Q1
"""
lab3_datafile/FCC_argon.csv is generated by using lab2 code.
The csv file stores the distance between 
Argon atom and its neighbour within the cutoff distance 3 * 3.4 A
LJ units follow the definition in the reference (See README.md)
"""
Ar_period = [3, 3, 3]
Ar_a = 5.24
Ar_A, Ar_B = construct_sim_box(Ar_period, Ar_a)
Ar_df = fcc_lattice(Ar_a, Ar_period)
Ar_cutoff = 3 * 3.4

df = neighborcsv(Ar_df, len(Ar_df), Ar_A, Ar_B, Ar_cutoff)
energy = 0

for row in df:
    # Only consider when neighbour index > atom index to prvent double count
    if int(row[1]) > int(row[0]):
            
        # distance (LJ unit) = distance (A) / 3.4
        energy += lab3lib.LJPotential(float(row[2])/3.4)

# Energy (eV) = Energy (LJ unit) * 1.65e-21 / 1.6e-19 (Charge of electron)
energy = energy * 1.65e-21 / 1.6e-19

# Transform energy from eV to meV per atom
energy_per_atom = energy * 1e3 / len(Ar_df)

print("Q1: \nTotal PE for FCC Argon: %.5f eV, PE per atom: %.5f meV\n" % (energy, energy_per_atom))

# Q2

# Generate NaCl lattice 
NaCl_period = [3, 3, 3]
NaCl_a = 5.63
NaCl_A, NaCl_B = construct_sim_box(NaCl_period, NaCl_a)

NaCl_df = lab3lib.NaCl_lattice(NaCl_a, NaCl_period)

# Initialize energy
NaCl_energy = 0

charge = {'Na': 0.988 * 1.6e-19, 'Cl': -0.988 * 1.6e-19}

for i, atom_i in enumerate(NaCl_df):
    for j, atom_j in enumerate(NaCl_df):

        # Calculate distance of two atoms under PBC
        r_ij = PBC_distance(atom_i[1:4], atom_j[1:4], NaCl_A, NaCl_B)

        # Skip same atom
        if i != j:
            # Calculate Coulumb potential of two atoms
            NaCl_energy += lab3lib.CoulumbPotential(r_ij * 1e-10, charge[atom_i[0]], charge[atom_j[0]])
            
            # Calculate Buckingham potential according to their charge
            if atom_i[0] == 'Na' and atom_j[0] == 'Na':
                NaCl_energy += lab3lib.BuckinghamPotential(r_ij, 7895.4, 0.1709, 29.06) 
            elif atom_i[0] == 'Cl' and atom_j[0] == 'Cl':
                NaCl_energy += lab3lib.BuckinghamPotential(r_ij, 1227.2, 0.3214, 29.06)
            else:
                NaCl_energy += lab3lib.BuckinghamPotential(r_ij, 2314.7, 0.2903, 0) 

print("Q2:\nEnergy per ion in NaCl lattice: %.5lf eV" % (NaCl_energy / len(NaCl_df)))