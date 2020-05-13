# MAGEseq

Here is the code used to parse and quantify fitness of mutants generated from a MAGE-seq experiment for the manuscript X. Currently it's just a barebones demo but will be updated to be more broadly applicable. 

Raw data avaiable here:\
Manuscript available here:

To do: a few of the codes appear outdates
- OLS from statmodels (import statsmodels.formula.api as smf to import statsmodels.api as smf)
- reindex_axis to reindex for pandas

# Dependencies
biopython\
pandas\
numpy\
xlrd  
statmodels


# 1. Prep raw sequencing files
- For the demo, download all raw files from "Bin1" from the data repository. 
    - Should consist of R1/R2 files from 9 timepoints and a WT samples. 
    - Just download L1 samples, or alternatively download all L1-L4 samples and merge into a single fastq.
- Pair-end merge R1/R2 files
- create a new directory, name it "merged", and move all merged files to the new directory

# 2. Parse sequence variants
- Edit the master_demo.py file with the relevant parameters
- For the demo ("Bin1") samples, no need to change any parameters
- Run the master_demo.py files
    - This generates csv files of fitness, linear regression statistics, fitness landscapes (position x codon matrix), etc.
