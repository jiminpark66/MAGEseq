# MAGE-seq

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
Also, file describing the sequence variants generated through MAGE is required. File should be titled `HEAD_MAGE_oligos.txt` where `HEAD` is the experiment/sample ID. For demonstration purposes `HEAD` is `Bin1`. Each line in the oligo file identifies individual oligo sequence using either `-` to denote positions that are not targeted for mutagenesis or `N` to denote positions that are targeted for mutagenesis. See the `Bin1_MAGE_oligos.txt` file provided for reference.

# 2. Parse sequence variants
Edit the main parameters in the initial section of the `master_demo.py`
Parameter descriptions:  
- Adapter: 5' upstream sequence of mutant loci to identify in each read 
- Adapter_spacer: number of basepairs between adapter and library start
- Library: Wildtype/Reference sequence of the loci
- Start/End: First and last amino acid position of the library
- dil_rate: Dilution rate of the turbidostat used to transform the log-linear regression slope
- header: library/sample name
- file_list: List of timepoint sample files found in the 'merged' directory. WT is required to compute a baseline sequencing miscall threshold.  

For the demo, the file can be ran as provided.  
Run `master_demo.py`.

# 3. Output
`master_demo.py` generates the `HEAD_summary.csv` that contains the following columns for each mutant/sequence variant (rows) generated from MAGE  
- Sequence, `-` denoting positions that remain unchanged from the reference sequence
- Raw counts of the each timepoint and WT reference sample
- Mutant Position, codon sequence and amino acid
- Relative abundance and log-transformed abundance at each time point
- fitness of mutant variant
- OLS statistics including SE, r-squared, etc. 

Additionally, each statistic is written in also writted separately, in list and matrix format.
