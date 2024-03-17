#!/usr/bin/env python

from PDBTools import pdblib

#This function takes a PDB id and return a pdb file
get_pdb=pdblib.get_pdb(ID="PDB_options")

#This function returns pdb details as per users choice on
#what they want to see, it takes a pdb id and a key to the option of interest
pdb_details=pdblib.pdb_details(ID,key)

#This function returns one letter protein residues from the pdb file
protein_residues=pdblib.protein_residues(ID,chain_id)

#This function writes to a file, chains with their chain ids and the pdb header as definition lines
pdb_chains=pdblib.pdb_chains(ID, output_filename, chain=None)

#This function allows the user to write their lines of choice
# to a file or to print them to the standard output
print_or_write_lines=pdblib.print_or_writelines_to_a_file(ID,chain_id,record_type,option)

#This function allows the user to alter a chain id of choice and save the file
altered_chain_id=pdblib.change_chain_id(ID,record_type,chain_id, new_chain_id)

#This function returns non standardprotein residues found on the pdb file
non_standard_protein_residues=pdblib.non_standard_residues(ID)

#This function returns a plot of the temperature factor of the proteins found on the pdb file
Temperature_factor_plot=pdblib.temperature_factor_plot(ID,chain_id,L,B)
