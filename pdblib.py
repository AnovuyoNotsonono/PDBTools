#!/usr/bin/env python
"""
pdbtools.py

A Python toolkit for downloading, querying, and analyzing PDB files.
Includes functions for:
- Downloading PDB files
- Extracting metadata
- Retrieving protein residues and chains
- Modifying chain IDs
- Identifying non-standard residues
- Plotting temperature factors
"""

import os
import requests
from matplotlib import pyplot as plt

# -----------------------------
# Core Function: Get PDB file
# -----------------------------
def get_pdb(pdb_id=None):
    """
    Download or read a PDB file and return its content as a list of lines.
    
    Parameters:
        pdb_id (str): The PDB ID of the structure.
                       If None, prints available options.
    
    Returns:
        list[str]: Lines of the PDB file.
    """
    try:
        if pdb_id is None:
            print("Available functions:\n"
                  "1. get_pdb()\n"
                  "2. pdb_details()\n"
                  "3. protein_residues()\n"
                  "4. pdb_chains()\n"
                  "5. print_or_write_file()\n"
                  "6. change_chain_id()\n"
                  "7. non_standard_residues()\n"
                  "8. temperature_factor_plot()")
            return
        
        filename = f"{pdb_id}.pdb"
        if not os.path.exists(filename):
            print(f"{filename} not found locally. Downloading...")
            response = requests.get(f"https://files.rcsb.org/download/{pdb_id}.pdb")
            pdb_lines = response.text.splitlines()
            with open(filename, "w") as f:
                f.write("\n".join(pdb_lines))
            return pdb_lines
        else:
            print(f"{filename} exists locally. Reading...")
            with open(filename, "r") as f:
                return f.readlines()
    except Exception as e:
        print(f"Error in get_pdb: {e}")


# -----------------------------
# Metadata Extraction
# -----------------------------
def pdb_details(pdb_id, key):
    """
    Print specific metadata lines from a PDB file.
    
    Parameters:
        pdb_id (str): PDB ID
        key (str): Metadata key (1-7)
    """
    try:
        pdb_lines = get_pdb(pdb_id)
        keys = {
            "1": "HEADER",
            "2": "TITLE",
            "3": "SOURCE",
            "4": "KEYWDS",
            "5": "AUTHOR",
            "6": "RESOLUTION",
            "7": "JRNL"
        }
        target = keys.get(key)
        if not target:
            print("Invalid key. Choose 1-7.")
            return
        for line in pdb_lines:
            if line.startswith(target):
                print(line.strip())
    except Exception as e:
        print(f"Error in pdb_details: {e}")


# -----------------------------
# Protein Residues
# -----------------------------
def protein_residues(pdb_id, chain_id):
    """
    Print one-letter amino acid sequence for a specific chain.
    
    Parameters:
        pdb_id (str): PDB ID
        chain_id (str): Chain identifier
    """
    try:
        pdb_lines = get_pdb(pdb_id)
        three_letter_seq = ""
        for line in pdb_lines:
            if line.startswith("ATOM") and line[21] == chain_id and line[13:15] == "CA":
                three_letter_seq += line[17:20].strip()

        aa_map = {
            "ALA":"A","ARG":"R","ASN":"N","ASP":"D","CYS":"C","GLU":"E",
            "GLN":"Q","GLY":"G","HIS":"H","ILE":"I","LEU":"L","LYS":"K",
            "MET":"M","PHE":"F","PRO":"P","SER":"S","THR":"T","TRP":"W",
            "TYR":"Y","VAL":"V","ASX":"B","GLX":"Z","SEC":"U*"
        }
        seq = [aa_map.get(res, "X") for res in [three_letter_seq[i:i+3] 
                                                for i in range(0, len(three_letter_seq), 3)]]
        print("".join(seq))
    except Exception as e:
        print(f"Error in protein_residues: {e}")


# -----------------------------
# Extract Chains
# -----------------------------
def pdb_chains(pdb_id, output_filename, chain=None):
    """
    Save sequences of chains from a PDB file into a FASTA file.
    
    Parameters:
        pdb_id (str): PDB ID
        output_filename (str): Output FASTA filename
        chain (str): Optional chain to extract (default None for all)
    """
    try:
        pdb_lines = get_pdb(pdb_id)
        sequences = ""
        chain_ids = ""
        header = pdb_lines[0].strip()
        for line in pdb_lines:
            if line.startswith("SEQRES") and chain is None:
                sequences += line[19:70].strip()
                chain_ids += line[11].strip()
        with open(f"{output_filename}.fasta", "w") as f:
            f.write(f">{header}_{chain_ids}\n{sequences}\n")
    except Exception as e:
        print(f"Error in pdb_chains: {e}")


# -----------------------------
# Print or write lines
# -----------------------------
def print_or_write_file(pdb_id, chain_id, record_type="ATOM", option="print"):
    """
    Print or write ATOM/HETATM lines for a chain.
    
    Parameters:
        pdb_id (str)
        chain_id (str)
        record_type (str): "ATOM" or "HETATM"
        option (str): "print" or "write"
    """
    try:
        pdb_lines = get_pdb(pdb_id)
        results = [line for line in pdb_lines if line.startswith(record_type) and line[21] == chain_id]
        if option == "print":
            for line in results:
                print(line.strip())
        elif option == "write":
            with open("Proteins_or_nonproteins.fasta", "w") as f:
                f.writelines(results)
        else:
            print("Option must be 'print' or 'write'.")
    except Exception as e:
        print(f"Error in print_or_write_file: {e}")


# -----------------------------
# Change Chain ID
# -----------------------------
def change_chain_id(pdb_id, record_type, old_chain_id, new_chain_id, output_filename="altered_chain.fasta"):
    """
    Replace a chain ID in a PDB file and save to new file.
    """
    try:
        pdb_lines = get_pdb(pdb_id)
        new_file = []
        for line in pdb_lines:
            if line.startswith(record_type) and line[21] == old_chain_id:
                line = line[:21] + new_chain_id + line[22:]
            new_file.append(line)
        with open(output_filename, "w") as f:
            f.writelines(new_file)
    except Exception as e:
        print(f"Error in change_chain_id: {e}")


# -----------------------------
# Non-standard residues
# -----------------------------
def non_standard_residues(pdb_id):
    """
    Print non-standard residues (from HETATM records) in a PDB file.
    """
    try:
        pdb_lines = get_pdb(pdb_id)
        residues = {line[17:20].strip() for line in pdb_lines if line.startswith("HETATM")}
        print(residues)
    except Exception as e:
        print(f"Error in non_standard_residues: {e}")


# -----------------------------
# Temperature Factor Plot
# -----------------------------
def temperature_factor_plot(pdb_id, chain_id, L=10, B=5):
    """
    Plot B-factors (temperature factors) for a given chain.
    """
    try:
        pdb_lines = get_pdb(pdb_id)
        b_factors = [float(line[60:66]) for line in pdb_lines if line.startswith("ATOM") and line[21] == chain_id]
        plt.figure(figsize=(L, B))
        plt.plot(b_factors)
        plt.title(f"Temperature Factors for {pdb_id} Chain {chain_id}")
        plt.xlabel("Residue Index")
        plt.ylabel("B-factor")
        plt.show()
    except Exception as e:
        print(f"Error in temperature_factor_plot: {e}")
