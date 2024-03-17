#!/usr/bin/env python

from PDBTools import pdblib

#This function returns a pdb file when given a pdb id
PDB_file=pdblib.get_pdb(ID="PDB_options")

#This function returns details of the pdb file
#by taking as positional inputs a pdb_id and a key to an option in the dictionary
PDB_details=pdblib.pdb_details(ID,key)

#This function gives one-letter protein residues
protein_residues=pdblib.protein_residues(ID,chain_id)

#This function returns a fasta file of chains with a header
#and chain id as a definition line
chains=pdblib.pdb_chains(ID, output_filename, chain=None)

#This function gives the user an option to print lines of their choice
#to the standard output or to write them to a file
print_or_writelines=pdblib.print_or_writelines_to_a_file(ID,chain_id,record_type,option)

#This function returns a file with chain ids of the pdb_file altered as per user's choice
altered_chain_id=change_chain_id(ID,record_type,chain_id, new_chain_id)

#This function takes a pdb id and returns non standard protein residues from the pdb file
nonstandard_residues=pdblib.non_standard_residues(ID)

#This function returns a plot of the temperature factor of the proteins in the pdb file
Temperature_factor_plot=pdblib.temperature_factor_plot(ID, chain_id)
