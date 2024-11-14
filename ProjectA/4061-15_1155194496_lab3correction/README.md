# Introduction

This folder contain programme from lab1 and lab2 for PHYS4061. 
Each lab is divided into "lib" and "main" program. 
_mathlib.py_ is the matrix operating function that is useful in the labs.
_lab_lib.py_ contains the functions that may be useful in future labs.
_lab_main.py_ contains that is used to fulfill requirement of each lab.
The output of each lab is stored in folder with prefix of lab number 
(e.g. lab1_latticexyz, lab2_neighbourcsv).

This project self-contained and does not require any external library.
# Lab 1 README

To run the program:
```
$ python lab1_main.py
```

The program would ask user to input file type, lattice constant
and periodicity in x, y, z direction. For example:
```
$ Please input the file you want (sc, bcc, fcc): (input)
$ Please input lattice constant: (input)
$ Please input your period in x: (input)
$ Please input your period in y: (input)
$ Please input your period in z: (input)
```

This would then output the xyz file of the selected lattice in 
output folder `lab1_latticexyz`. See the example files in the folder.

# Lab 2 README

To run the program:
```
$ python lab2_main.py
```

The program would as user to input file type, lattice constant,
periodicity in x, y, z, and the desired cutoff distance. For example:
```
$ Please input lattice constant: (input)
$ Please input cutoff distance: (input)
$ Please input your period in x: (input) 
$ Please input your period in y: (input)
$ Please input your period in z: (input) 
```

The volume of unit cell would be output in console
```
$ The volume of unit cell in sc is [volume]
```

The program would output neighbour list of each atom in the lattice.
The output file is stored in `lab2_neighbourcsv`. See example files
in the folder.

# Lab3 3 README

# Q1: Lennard-Jones Potential of FCC solid Argon

This part of the lab follows the approach in https://arxiv.org/pdf/1908.00601.
The cohesive energy of solid argon as FCC lattice is calculated by Lennard-Jones potential.

The unit of this part follows the reference, 
- lattice constant = 5.24 A
- $x^*$ = x / $\sigma$, where $\sigma$ = 3.4 A
- $E^*$ = E / $\epsilon$, where $\epsilon$ = 1.65e-21
- cutoff distance = $3\sigma$. 

Generating a lattice with period 3x3x3, the simulated energy per atom is -85.60985 meV.
Comparing to the energy in the work (-85.51 meV) and experimental data (-88.9 meV),
The simulation result is within an acceptable error range of 5%, which is satisfactory.

# Q2

In Q2, the program calculates the Buckingham potential of ionic solid NaCl.
NaCl is an FCC lattice, with alternate Na FCC lattice and Cl FCC lattice.
It can also be seen as Cl FCC lattice displaces by a/2 comparing to Na lattice.

Buckingham Potential Parameters:
(Reference: P. 16 or Session 2.2 of https://www.sciencedirect.com/science/article/pii/S0013794412000653?fr=RR-2&ref=pdf_download&rr=8d6981a69e47f605)
- Na-Na: A (eV) = 7895.4; B (A) = 0.1709; C (eV A^6) = 29.06
- Na-Cl: A (eV) = 2314.7; B (A) = 0.2903; C (eV A^6) = 0
- Cl-Cl: A (eV) = 1227.2; B (A) = 0.3214; C (ev A^6) = 29.06
- Effective charge of Na = 0.998. * 1.6e-19,
- Effective charge of Cl = -0.998 * 1.6e-19

From https://www.princeton.edu/~maelabs/mae324/glos324/nacl.htm, which is from Chiang, Birnie and Kingery, "Physical Ceramics," Wiley (1997):
- lattice constant: 5.63 A
- Cohesive energy: -7.9 eV

The simulated energy per ion is -7.93 eV. Comparing with the aforementioned literature result,
the simulation result is within an acceptable error range of 5%, which is satisfactory.


Last update: 2024 Oct 22
