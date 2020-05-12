# MAGEseq

Here is the code used to parse and quantify fitness of mutants generated from a MAGE-seq experiment for the manuscript X. Currently pretty barebones but will be updated to be more broadly applicable. 

Raw data avaiable here:\
Manuscript available here:

# Dependencies
biopython\
pandas


# 1. Raw sequencing files prep
Only required for pair-end sequenced samples


# 2. Parse sequence variants
Edit the master.py file with the relevant parameters:  
    Adapter sequence: sequenced used to identify and align against the reference sequence  
    Library sequence: sequence used as the reference sequence  
    Start: amino acid start position  
    End: amino acid end position  
    Dilution rate: dilution rate of the turbidostat used to transform log-linear regression slope to fitness between 0-1  
