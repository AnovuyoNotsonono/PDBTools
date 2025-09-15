#!/usr/bin/env python

from PDBTools import pdblib

def main():
    # Example PDB ID and parameters
    ID = "1HHP"          # Replace with any valid PDB ID
    chain_id = "A"       # Chain to analyze
    output_filename = "example_chains"  # Output file for chains
    record_type = "ATOM" # Options: "ATOM" or "HETATM"
    option = "print"     # Options: "print" or "write"
    key = "2"            # Example option for pdb_details (e.g., TITLE)
    new_chain_id = "B"   # For change_chain_id
    L, B = 10, 5         # Plot dimensions (length, breadth)

    # 1. Show available functions
    print("Available PDBTools functions:")
    pdb_options = pdblib.get_pdb(ID="PDB_options")
    print(pdb_options)

    # 2. Get PDB details (like TITLE)
    print("\nPDB Details (TITLE):")
    pdblib.pdb_details(ID, key)

    # 3. Get one-letter protein residues
    print("\nProtein residues:")
    pdblib.protein_residues(ID, chain_id)

    # 4. Save chains to a FASTA file
    pdblib.pdb_chains(ID, output_filename)

    # 5. Print or write selected lines
    pdblib.print_or_writelines_to_a_file(ID, chain_id, record_type, option)

    # 6. Alter chain ID and save to a file
    pdblib.change_chain_id(ID, record_type, chain_id, new_chain_id)

    # 7. Get non-standard residues
    print("\nNon-standard residues:")
    pdblib.non_standard_residues(ID)

    # 8. Plot temperature factors
    print("\nPlotting temperature factor...")
    pdblib.temperature_factor_plot(ID, chain_id, L, B)


if __name__ == "__main__":
    main()
