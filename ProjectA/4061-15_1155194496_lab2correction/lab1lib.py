def sc_lattice(a, period, atom='atom'):
    # Generate simple lattice
    lst = []
    for i in range(period[0]):
        for j in range(period[1]):
            for k in range(period[2]):
                lst.append([atom, i*a, j*a, k*a])
    return lst

def fcc_lattice(a, period, corner='atom', fcc='atom'):
    # Generate Face-centered lattice
    lst = []
    for i in range(period[0]):
        for j in range(period[1]):
            for k in range(period[2]):
                lst.append([corner, i*a, j*a, k*a])
                # face center atoms
                lst.append([corner, i*a, (j+0.5)*a, (k+0.5)*a])
                lst.append([fcc, (i+0.5)*a, j*a, (k+0.5)*a])
                lst.append([fcc, (i+0.5)*a, (j+0.5)*a, k*a])
    return lst

def bcc_lattice(a, period, corner='atom', bcc='atom'):
    # Generate Body-centered lattice 
    lst = []
    for i in range(period[0]):
        for j in range(period[1]):
            for k in range(period[2]):
                lst.append([corner, i*a, j*a, k*a])
                lst.append([bcc, (i+0.5)*a, (j+0.5)*a, (k+0.5)*a])

    return lst

def tetra_lattice(a, period):
    # Generate tetrahedral structure of cells
    lst = []
    for i in range(period[0]):
        for j in range(period[1]):
            for k in range(period[2]):
                lst.append([i*a, j*a, k*a]) 

                lst.append([i*a, (j+0.5)*a, (k+0.5)*a])
                lst.append([(i+0.5)*a, j*a, (k+0.5)*a])
                lst.append([(i+0.5)*a, (j+0.5)*a, k*a])

                lst.append([(i+0.25)*a, (j+0.25)*a, (k+0.25)*a]) 
                lst.append([(i+0.75)*a, (j+0.75)*a, (k+0.25)*a]) 
                lst.append([(i+0.75)*a, (j+0.25)*a, (k+0.75)*a]) 
                lst.append([(i+0.25)*a, (j+0.75)*a, (k+0.75)*a]) 

    return lst

def write_xyz(df, output_dir='lattice.xyz'):
    """
    Write xyz file from the given coordinate vector
    Argument:
    - df: matrix that contains coordinate vector of each atom
    """
    with open(output_dir, "w") as f:
        # Write first line of xyz file (total no of atom)
        f.write(f"{len(df)}\n")

        # Write second line of xyz file
        f.write("Lab 1\n")

        for i in range(len(df)):
            # Write coordinate of atom
            f.write("{}\t{:.5}\t{:.5}\t{:.5}\n".format(df[i][0], df[i][1], df[i][2], df[i][3]))

    return len(df)