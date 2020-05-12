import pandas as pd
import numpy as np
import sys
import csv




def mask(seq, mask_seq):
	masked = []
	for i in range(len(seq)):
		if seq[i] == mask_seq[i]:
			masked.append('-')
		else:
			masked.append(seq[i])
	return ''.join(masked)

def variants(seqN):
	var = []
	for let in range(len(seqN)):
		if seqN[let] == "-" and not var:
			var = ["-"]
		elif seqN[let] == "N" and not var:
			var.append("A")
			var.append("T")
			var.append("C")
			var.append("G")
		elif seqN[let] == "-":
			for variant in range(len(var)):
				var[variant] = var[variant] + ("-")
		elif seqN[let] == "A" or seqN[let] == "T" or seqN[let] == "C" or seqN[let] == "G":
			for variant in range(len(var)):
				var[variant] = var[variant] + seqN[let]
		elif seqN[let] == "N":
			for variant in range(len(var)):
				var.append(var[variant] + "T")
				var.append(var[variant] + "C")
				var.append(var[variant] + "G")
				var[variant] = var[variant] + ("A")

	return(var)

def main(lib_name,Library,AA_start,AA_end):
		#Set 1 and 2 have different ordering
	Rep_1A = [] #mutant sequence
	Rep_1B = [] #masked mutant seq
	Rep_2A = [] #masked mutant seq
	Rep_2B = [] #fitness values
	oligo = []
	oligo_variants = {}
	AA_end = AA_end+1
	WT_mask = "-"*(AA_end - AA_start)*3
	#set up replacement variables for masked and fitnessvalues
	with open(lib_name + "_library_fitness_RMSE.csv","r") as f:
		reader = csv.reader(f,delimiter = ",")
		for line in reader:
			Rep_2A.append(mask(line[0],Library))
			Rep_2B.append(line[1])

	with open(lib_name+"_MAGE_oligos.txt","r") as f:
		for line in f.read().splitlines():
			oligo.append(line)
			
	for var in oligo:
		oligo_variants[var] = variants(var)

	#this needs to be changed when you have different Ns in the oligo library
	ind = variants("N"*int(3))

	DFF = pd.DataFrame.from_dict(oligo_variants,"index")
	print(DFF)
	DFF.columns = ind

	for index, rows in DFF.iterrows():
		for item in rows:
			Rep_1A.append(item)
			Rep_1B.append(mask(item,Library))
			
	DFF = DFF.replace(Rep_1A,Rep_1B)
	DFF = DFF.replace(Rep_2A,Rep_2B)
	DFF = DFF.replace(WT_mask,1)
	
	#This line changes rows and columns
	DFF = DFF.T
	DFF = DFF.reindex_axis(sorted(DFF.columns,reverse = True),axis = 1)
	#change columns to AA number and WT codon

	AA_col = []
	n = 3
	for index in list(range(AA_end - AA_start)):
		AA_col.append(str([Library[i:i+n] for i in range(0, len(Library), n)][index]) + " " + str(list(range(AA_start,AA_end))[index]))
		
	DFF.columns = AA_col

	if n == 3:
		AA_index = [
		"ATG",
		"GCA",
		"GCC",
		"GCG",
		"GCT",
		"GTA",
		"GTC",
		"GTG",
		"GTT",
		"CTA",
		"CTC",
		"CTG",
		"CTT",
		"TTA",
		"TTG",
		"ATA",
		"ATC",
		"ATT",
		"CCA",
		"CCC",
		"CCG",
		"CCT",
		"TTC",
		"TTT",
		"TGG",
		"GGA",
		"GGC",
		"GGG",
		"GGT",
		"AGC",
		"AGT",
		"TCA",
		"TCC",
		"TCG",
		"TCT",
		"ACA",
		"ACC",
		"ACG",
		"ACT",
		"TGC",
		"TGT",
		"AAC",
		"AAT",
		"CAA",
		"CAG",
		"TAC",
		"TAT",
		"GAC",
		"GAT",
		"GAA",
		"GAG",
		"AAA",
		"AAG",
		"AGA",
		"AGG",
		"CGA",
		"CGC",
		"CGG",
		"CGT",
		"CAC",
		"CAT",
		"TAG",
		"TAA",
		"TGA"
			]
		DFF = DFF.reindex(AA_index)
		DFF.to_csv(lib_name + "_fitness_RMSE_matrix_unformat.csv")

		AA_index_AA = [
		"M - ATG",
		"A - GCA",
		"GCC",
		"GCG",
		"GCT",
		"V - GTA",
		"GTC",
		"GTG",
		"GTT",
		"L - CTA",
		"CTC",
		"CTG",
		"CTT",
		"TTA",
		"TTG",
		"I - ATA",
		"ATC",
		"ATT",
		"P - CCA",
		"CCC",
		"CCG",
		"CCT",
		"F - TTC",
		"TTT",
		"W - TGG",
		"G - GGA",
		"GGC",
		"GGG",
		"GGT",
		"S - AGC",
		"AGT",
		"TCA",
		"TCC",
		"TCG",
		"TCT",
		"T - ACA",
		"ACC",
		"ACG",
		"ACT",
		"C - TGC",
		"TGT",
		"N - AAC",
		"AAT",
		"Q - CAA",
		"CAG",
		"Y - TAC",
		"TAT",
		"D - GAC",
		"GAT",
		"E - GAA",
		"GAG",
		"K - AAA",
		"AAG",
		"R - AGA",
		"AGG",
		"CGA",
		"CGC",
		"CGG",
		"CGT",
		"H - CAC",
		"CAT",
		"* - TAG",
		"TAA",
		"TGA"
			]
		DFF.index = AA_index_AA

	DFF.to_csv(lib_name + "_fitness_RMSE_matrix.csv")




if __name__ == "__main__":
	main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])