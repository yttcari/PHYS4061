from lab2lib import construct_sim_box, PBC_distance, neighborcsv
from lab1lib import fcc_lattice
import lab3lib
import lab4lib
import csv
import sys

Ar_period = [3, 3, 3]
Ar_a = 5.24
Ar_A, Ar_B = construct_sim_box(Ar_period, Ar_a)
Ar_df = fcc_lattice(Ar_a, Ar_period)
Ar_cutoff = 3 * 3.4

neighbourcsv_dir = "/Users/caritsang/Desktop/Project/PHYS4061/ProjectA/lab3_datafile/FCC_argon.csv"

EPISLON = 0.01
error = 1

neighborcsv(Ar_df, len(Ar_df), Ar_A, Ar_B, Ar_cutoff, name=neighbourcsv_dir)
E0, E0_per_atom = lab4lib.get_LJ(neighbourcsv_dir, len(Ar_df))

print(f"{E0} {E0_per_atom}")

i = 0

# displace 10th atom towards x by 0.1 A
Ar_df[9][1] += 0.1


while error > EPISLON and i < 100:

    neighborcsv(Ar_df, len(Ar_df), Ar_A, Ar_B, Ar_cutoff, name=neighbourcsv_dir)
    E, E_per_atom = lab4lib.get_LJ(neighbourcsv_dir, len(Ar_df))

    for atom in Ar_df:
        vec = atom[1:]
        vec = lab4lib.SteepestDecent(vec)
        #print("" % atom[1:], vec)

        atom[1:] = vec
        
    error = abs(E0_per_atom - E_per_atom)
    i += 1
    print(f"Epoch {i}, Error: {error}, E: {E_per_atom}")

# Delete snapshot folder
#os.remove("temp")