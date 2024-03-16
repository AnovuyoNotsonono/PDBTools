
import os
import requests
def get_pdb(ID='PDB_options'):
    """get_pdb takes pdb_ID as a default argument, downloads and reads a PDB file and queries its data
       it also gives options to the user on what to do when no argument is given"""
  #Giving the user options when no input is inserted  
    if ID=='PDB_options':
        print("[1.HEADER, 2.TITLE, 3.SOURCE, 4.KEYWDS, 5.AUTHOR, 6.RESOLUTION, 7.JRNL TITL]")
  
  #Checking whether a file exists before downloading, this line ONLY executes
  #if the argument "ID" is given during a fuction call.
    
    if (os.path.exists(ID+".pdb")==False) and (ID!="PDB_options"):
           print("The file is being downloaded")
  #Downloading a PDB file if it does not exist locally using the "requests" module 
           response=requests.get("https://files.rcsb.org/download/"+ID+".pdb")
           pdb_file=response.text
           return pdb_file
      
  #Allowing the user to open and read the file on condition that the file already exists locally,
  #this line also executes ONLY if the argument "ID" is given in the function call
    elif (os.path.exists(ID+".pdb")==True) and (ID!="PDB_options"):
        print("file exists locally")
        
   #On condition that the file exists locally, it is opened for reading using the "with" keyword.
  #Error handling: this is to avoid the "FileNotFound error" that occurs when trying to read a file without 
                   #providing an ID for that file, this error handling enables the user to choose what they want
                   #to do from the pdb_options given
    try:
        with open(ID+".pdb", "r") as fobject:
                pdf_file=fobject.readlines()
                return pdf_file
    except FileNotFoundError:
        print("Please choose from these PDB_options by calling 'pdb_details' function")
        

def pdb_details(ID, key):
    """pdb_details takes as keyword arguments a pdb ID and a key/option number, it 
       return the details corresponding to the selected key/option """
    # Calling and assigning get_pdb() function into a variable to use it on the "pdb_details" function
    output1=get_pdb(ID).split("\n")
    
    for line in output1:
       #Creating a dictionary containing details of the PDB file with option numbers as keys and details as values 
        PDB_options={"1":"HEADER", "2":"TITLE", "3":"SOURCE", "4":"KEYWDS", 
                     "5":"AUTHOR", "6":"RESOLUTION", "7":"JRNL"}
        #Allowing the user to isolate the lines they want from the optiones given.
        if line.startswith(PDB_options[key]):
            print(line)
    
    

def protein_residues(ID,chain_id):
    """Protein_residues takes a PDB ID and a chain ID as positional inputs to give
       one-letter protein residues found on the pdb_file"""
    #Calling the "get_pdb" function to use its output pdb file to get protein residues
    output1=get_pdb(ID).split("\n")
    
    #Creating an empty string for three-letter protein residues found on the pdb file
    three_letter_residues=""
    
    #Iterating though lines of the pdb file to isolate them as a string
    for line in output1:
    #Isolating protein atoms to get three-letter protein residues
        if (line.startswith("ATOM")) and (line[21]==chain_id) and (line[13:15]=="CA"):
            three_letter_residues +=line[17:21]
            
    #Creating a dictionary for standard-amino acids with three-letter residues as keys and one letter-residues as values   
    standard_amino_acids={"PRO":"P","ALA":"A","ASX":"B","CYS":"C","ASP":"D","GLU":"E","PHE":"F","GLY":"G",
                         "HIS":"H","ILE":"I","LYS":"K","LEU":"L","MET":"M","ASN":"N","GLN":"Q","ARG":"R",
                          "SER":"S","THR":"T","SEC":"U*","VAL":"V","TRP":"W","TYR":"Y","GLX":"Z"}
    
    #Iterating through the "standard_amino_acids" dictionary to access those keys existing on the "three-letter_residues"
    #found on the pdb file protein residues
    for k,v in standard_amino_acids.items():
        #Isolating those protein residues existing in both standard_amino_acids and the pdb file, printing them on a single line
        if k in three_letter_residues:
            print(v, end=" ")


def pdb_chains(ID, output_filename, chain=None):
    """pdb_chains takes pdb_ID, ouput filename as positional arguments and chain_id of none as a default argument,
       this function saves each chain from a pdb_file in a single fasta file provided a chain is not given """
    
    #Calling the "get_pdb" function and giving it a variable "output1" to use its output pdb_file
    output1=get_pdb(ID).split("\n")
    
    #Creating an empty string to isolate chains from the pdb file
    chains=""
    #Creating an empty string to isolate chain_ids corresponding to the chains
    chain_ids=""
    pdb_HEADER=output1[0]
    
    #Isolating lines that satisfy the following conditions 
    for line in output1:
        if line.startswith("SEQRES") and chain==None:
            chains +=line[19:70]
            #Isolating chain ids corresponding to the chains and storing them in a separate empty string
            chain_ids+=line[11]   
    #Creating and saving the new fasta file that stores the pdb_header and chain_ids as definition lines and 
    #the isolated chains
    with open(output_filename+".fasta", "w") as fobject:
        fobject.write(pdb_HEADER+chain_ids + chains)
    
    
        
def print_or_writelines_to_a_file(ID,chain_id,record_type,option):
    """print_or_writelines_to_a_file takes PDB ID, chain ID, record_type(to specify wheter HETATM/ATOM)
       and an option for the user to either print the results or write them to a file, it returns protein
       or non_protein lines either stored in a file or printed out for reading"""
    
    #Calling the "get_pdb() function to use its pdb output file"
    output1=get_pdb(ID).split("\n")
    #Creating an empty string to store the "results" relevant to the conditions set by the user
    results=""
    #Isolating lines according to the criteria chosen by the user
    for line in output1:
        #Giving the user an option to write the lines to a file
        if (line.startswith(record_type)) and (line[21]==chain_id) and (option=="write"):
            with open("Proteins_or_nonproteins.fasta", "w") as fobject:
                results += line
                fobject.writelines(results)
                
        #Giving the user another option to print and read the results    
        elif (line.startswith(record_type)) and (line[21]==chain_id) and (option=="print"):
            results += line
            print(results)
            
#Alter a chain ID from a structure and save the file.
def change_chain_id(ID,record_type,chain_id, new_chain_id):
    """change_chain_id takes as positional inputs PDB ID,record_type(ATOM/HETATM), chain_id to be changed
       and a new chain_id, this function alters chain id as chosen by the user and
       returns a file written to it the PDB contents with the altered chain ids"""
    
    #Calling the get_pdb function to use its output file and change its chain id
    output1=get_pdb(ID).split("\n")
    
    #Creating an empty string to store the file with altered chain id
    new_file=""
    
    #Isolating lines of the pdb file
    for line in output1:
        #Creating an empty string to store lines with the altered chain ids
        altered_chain_id=""
        
        #Selecting the relevant lines according to the criteria chosen by the user
        if (line.startswith(record_type)) and (line[21]==chain_id):
        #Replacing the chain_id chosen by the user with a new chain_id also chosen by the user
            altered_chain_id +=line[21].replace(chain_id, new_chain_id)
            new_file+=line[:21]+altered_chain_id+line[22:]
            
        #Saving the lines with the altered chain ids to a new fasta file
            with open("altered_chain_id.fasta", "w") as fobject:
                    fobject.write(new_file)
                    

  #Print any non-standard protein residue names (on a single line; i.e. one entry per residue), if such are present
def non_standard_residues(ID):
    """non_standard_residues takes as positional argument a pdb ID and returns non-standard residues
       from the pdb file if they exist"""
    #Calling the "get_pdb" function to use its outputfile to get its residues
    output1=get_pdb(ID).split(\n)
    #Creating an empty list to store all the protein residues from the pdb file
    non_standard_residues=set()
    #Isolating lines from the pdb file which is the output of the "get_pdb()" function
    for line in output1:
    #Setting a condition to focus only on the lines starting with "HETATM" since non-standard residues are contained in those lines
        if (line.startswith("HETATM")):
            non_standard_residues.add((line[17:21]))
    print(non_standard_residues)
    
    
#Plot the temperature factor of the protein, given a chain ID, the plot dimensions and an output file name.
from matplotlib import pyplot as plt
def temperature_factor_plot(ID, chain_id):
    output1=get_pdb(ID)
    #Creating an empty list to store all the temperature factor values
    Temperature_factor=[]
    for line in output1:
        if (line.startswith("ATOM")) and (line[21]==chain_id):
            Temperature_factor.append(float(line[61:65]))
            plt.title("Temperature_factor plot")
            plt.plot(Temperature_factor)

 
