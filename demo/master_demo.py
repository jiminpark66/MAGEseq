import extract_merged_files_input
import library_variant_counter
import library_rel_ratio2
import library_fitness_matrix
import compile_data_sheet
import library_fitnesspval_matrix,library_fitnessse_matrix, library_fitnessrsq_matrix, library_fitnessconfint_matrix, library_fitnessrmse_matrix


############################################################
#Initialize these variables

#5' upstream sequence of mutant loci to identify in each read
Adapter = "GCCGTGCGAAGAAAGAG" 

# space between adapter and library start
Adapter_spacer = 0 

#Wildtype reference sequence of the mutant loci
Library = "ATGGTTGAAGCGAACTTACGTCTGGTTATTTCTATCGCTAAGAAATACACCAACCGTGGCTTGCAGTTCCTTGACCTGATTCAGGAAGGCAACATCGGTCTGATGAAAGCGGTTGATAAATTCGAATACCGC" 

#First and last amino acid position mutagenized in the sequencing library, simply here as a reference
Start = 379 
End = 422 

#Dilution rate of the turbidostat used to transform the log-linear regression
dil_rate = 1.3167 

#timepoint samples
#currently these files should refer to samples harvested at corresponding timepoints [0,1,2,3,4,5,6,9,12,WT]. WT is required to compute a baseline sequencing miscall threshold
file_list = ["Bin1-1.fastq.gz","Bin1-2.fastq.gz","Bin1-3.fastq.gz","Bin1-4.fastq.gz","Bin1-5.fastq.gz","Bin1-6.fastq.gz","Bin1-7.fastq.gz","Bin1-8.fastq.gz","Bin1-9.fastq.gz","Bin1-WT.fastq.gz"]

#library name
header = "Bin1"
###########################################################




for file in file_list:
	extract_merged_files_input.main(file,Library,Adapter,Adapter_spacer)

#library_variant_counter.main(header,Library)
library_rel_ratio2.main(header,dil_rate)
library_fitness_matrix.main(header,Library,Start, End)
library_fitnesspval_matrix.main(header,Library,Start, End)
library_fitnessse_matrix.main(header,Library,Start, End)
library_fitnessrsq_matrix.main(header,Library,Start, End)
library_fitnessconfint_matrix.main(header,Library,Start, End)
library_fitnessrmse_matrix.main(header,Library,Start, End)
compile_data_sheet.main(header,Library,Start)