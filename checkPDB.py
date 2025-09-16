#!/usr/bin/env python

import pdblib

def main():
    """
    Demonstrates the usage of PDBTools library functions on a sample PDB file.

    This function performs the following steps:
    1. Displays available PDBTools functions if no argument is given to the 'get_pdb' function.
    2. Retrieves PDB details for a selected option (e.g., TITLE, HEADER).
    3. Extracts one-letter amino acid residues for a given chain.
    4. Saves chains from the PDB file to a FASTA file.
    5. Prints or writes ATOM/HETATM lines for a specific chain.
    6. Alters a chain ID and saves the modified PDB content to a new file.
    7. Displays non-standard residues found in the PDB file.
    8. Plots the temperature factor (B-factor) of atoms in the specified chain.

    Parameters (set as example values within the function):
        ID (str): PDB identifier (e.g., "1HHP").
        chain_id (str): Chain to analyze (e.g., "A").
        output_filename (str): Name for the FASTA output file for chains.
        record_type (str): Record type to filter ("ATOM" or "HETATM").
        option (str): Whether to print or write lines ("print" or "write").
        key (str): Option number for selecting PDB details (e.g., "2" for TITLE).
        new_chain_id (str): New chain ID for the change_chain_id function.
        L (int): Plot length for temperature factor plot.
        B (int): Plot breadth for temperature factor plot.

    Usage:
        Run the script directly. This function uses example PDB ID "1HHP"
        and demonstrates all main functionalities of the pdblib module.
    """

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
    pdb_options = pdblib.get_pdb()

    # 2. Get PDB details (like TITLE)
    print("\nPDB Details (TITLE):")
    pdblib.pdb_details(ID, key)

    # 3. Get one-letter protein residues
    print("\nProtein residues:")
    pdblib.protein_residues(ID, chain_id)

    # 4. Save chains to a FASTA file
    pdblib.pdb_chains(ID, output_filename)

    # 5. Print or write selected lines
    pdblib.print_or_write_file(ID, chain_id, record_type, option)

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
