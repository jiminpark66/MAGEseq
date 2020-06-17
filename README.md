# MAGEseq

MAGE-seq (Multiplexed Automated Genome Engineering) can be used to generate a saturation mutagenesis library at a genomic locus and quantify fitness of each individual mutant variants through a pooled competition experiment and sequencing. Here, we provide code and materials from the manuscript "Systematic dissection of σ70 sequence diversity and function in bacteria" [Add citation]    

Manuscript can be accessed here: [add link]
Raw data for the manuscript can be accessed here:E-MTAB-9103 [add link]


# Dependencies
Python 3.X
- biopython\
- pandas\
- numpy\
- xlrd\
- statmodels\
SeqPrep


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
