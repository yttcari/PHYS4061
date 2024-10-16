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

Last update: 2024 Oct 16
