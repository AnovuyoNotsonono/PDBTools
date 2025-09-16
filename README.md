# PDBTools

## Overview
**PDBTools** is a Python library for working with Protein Data Bank (PDB) files.  
It provides **8 main functions** that allow users to:

1. Download PDB files from the RCSB PDB database.
2. Query PDB details such as HEADER, TITLE, SOURCE, and more.
3. Extract one-letter amino acid sequences for a specific chain.
4. Save chains to FASTA files.
5. Print or write selected ATOM/HETATM lines for specific chains.
6. Change chain IDs in a PDB file and save the modified file.
7. Identify non-standard residues.
8. Plot temperature factors (B-factors) for atoms in a chain.

The library works **without external frameworks**, though plotting requires `matplotlib`.

---

## Features

- **Download PDB files** automatically if not present locally.
- **Query specific PDB information** by user-defined options.
- **Extract protein sequences** in one-letter format.
- **Write selected data to files** for downstream analysis.
- **Visualize structural data** using temperature factor plots.
- **Interactive function list:** If no PDB ID is provided to `get_pdb()`, the function will **print a list of available functions/options**.

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/AnovuyoNotsonono/PDBTools.git
cd PDBTools
```
2. **Create a Python environment (example with Python 3.11):**
```bash
conda create -n py311 python=3.11
conda activate py311
```
3. **Install required packages**:
```bash
   pip install matplotlib requests
```
## Usage

1. **Ensure the main script (checkPDB.py) is in the same directory as pdblib.py**.

2. **Import the library in your Python script**:
   
```python
import pdblib # If (checkPDB.py) is in the same directory as pdblib.py.
```
 **Otherwise**
```python
from PDBTools import pdblib #If (checkPDB.py) is not the same directory as pdblib.py.
```
## Call library functions:

 **The steps below show an example of how to use the program**
```python

# Show available functions (no PDB ID provided)
pdblib.get_pdb()  

# Download a PDB file
pdb_lines = pdblib.get_pdb("1HHP")  # Returns file content as a list of lines

# Get PDB details (e.g., TITLE)
pdblib.pdb_details("1HHP", "2")

# Extract one-letter protein residues
pdblib.protein_residues("1HHP", "A")

# Save chains to a FASTA file
pdblib.pdb_chains("1HHP", "example_chains")

# Print or write ATOM/HETATM lines
pdblib.print_or_write_file("1HHP", "A", record_type="ATOM", option="print")

# Change chain ID
pdblib.change_chain_id("1HHP", "ATOM", "A", "B")

# Get non-standard residues
pdblib.non_standard_residues("1HHP")

# Plot temperature factors
pdblib.temperature_factor_plot("1HHP", "A", 10, 5)
```
## Example Script

The provided checkPDB.py script demonstrates all functions interactively.

Note: checkPDB.py must be in the same directory as pdblib.py to work correctly.


