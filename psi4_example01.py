import psi4

# Allocate memory and set the output file
psi4.set_memory('500 MB')
psi4.core.set_output_file('psi4_output.dat', False)

# Define the water molecule geometry
h2o = psi4.geometry("""
O
H 1 0.96
H 1 0.96 2 104.5
""")

# Compute the Hartree-Fock energy using the STO-3G basis set
energy = psi4.energy('scf/sto-3g', molecule=h2o)
print("Computed energy (in Hartree):", energy)
