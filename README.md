# MAGEseq

MAGE-seq (Multiplexed Automated Genome Engineering) can be used to generate a saturation mutagenesis library at a genomic locus and quantify fitness of each individual mutant variants through a pooled competition experiment and sequencing. Here, we provide code and materials from the manuscript "Systematic dissection of σ70 sequence diversity and function in bacteria" [Add citation]    

Manuscript can be accessed here: [add link]
Raw data for the manuscript can be accessed here:E-MTAB-9103 [add link]


# Dependencies
- Python 3.X
    - biopython
    - pandas
    - numpy 
    - xlrd 
    - statmodels
- SeqPrep


# 1. Raw file processing and other prerequisites
The raw sequencing files should be provided as merged fastq.gz files in the "merged/" directory. For the demo, download files from samples `RpoD_MAGE_Bin1_T1` through `RpoD_MAGE_Bin1_T9` and `RpoD_MAGE_Bin1_WT` . Raw R1 and R2 files can be merged using SeqPrep as follows. 
```
SeqPrep -m .05 -L 30 -f R1_file.fastq.gz -r R2_file.fastq.gz -1 processed/R1_file.fastq.gz  -2 processed/R2_file.fastq.gz -3 discarded/R1_file.fastq.gz  -4 discarded/R2_file.fastq.gz  -s merged/R1_file.fastq.gz  -E pretty/R1_file.fastq.gz -x 1000
```
Also, file describing the sequence variants generated through MAGE is required. File should be titles `HEAD_MAGE_oligos.txt` where `HEAD` is the experiment/sample ID. For demonstration purposes `HEAD` is `Bin1`.

# 2. Parse sequence variants
- Edit the master_demo.py file with the relevant parameters
- For the demo ("Bin1") samples, no need to change any parameters
- Run the master_demo.py files
    - This generates csv files of fitness, linear regression statistics, fitness landscapes (position x codon matrix), etc.
