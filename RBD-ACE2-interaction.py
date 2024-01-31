# Import the PyMOL module
from pymol import cmd

# Set the distance threshold (5 Å)
distance_threshold = 5.0

# Select atoms from Chain A
cmd.select("ACE2_atoms", "resi 19-615 in chain A")

# Select atoms from Chain B
cmd.select("RBD_atoms", "resi 319-526 in chain B")

# Iterate through atoms in Chain A and find interacting residues in Chain B
interacting_residues = set()
cmd.iterate("(RBD_atoms)", "interacting_residues.add(resi)", space={'interacting_residues': interacting_residues})

# Create a selection of interacting residues based on the distance threshold
cmd.select("interacting_residues", f"(byres RBD_atoms) within {distance_threshold} of ACE2_atoms")

# Show the selected residues
cmd.color("yellow", "interacting_residues")
#cmd.show('stick', 'interacting_residues')


interacting_residues_list = cmd.get_model("interacting_residues").atom

# Remove duplicates and sort the list
unique_residues = sorted(set((atom.resi, atom.resn) for atom in interacting_residues_list))

# Display the residue names
for residue in unique_residues:
    print(f"Amino Acid: {residue[1]} Residue: {residue[0]}")

# Write the list to a text file
file_path = "interacting_residues.txt"
with open(file_path, "w") as file:
    for residue in unique_residues:
        file.write(f"{residue[1]} {residue[0]}\n")

print(f"List of interacting residues within {distance_threshold} Å written to {file_path}")


