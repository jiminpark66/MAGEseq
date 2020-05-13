import pandas as pd
import numpy as np

def main(lib_name,lib,start):
	name = ["T1_raw","T2_raw","T3_raw","T4_raw","T5_raw","T6_raw","T7_raw","T8_raw","T9_raw","WT_raw"]
	df = pd.read_csv(lib_name + "_library_raw_counts.csv",index_col = 0,names = name)

	raw_sum = {}
	for index in df.index:
		raw_sum[index] = sum(df.loc[index,"T1_raw":"T9_raw"])
		sum_s = pd.Series(raw_sum)
	df['sum_T1-T9_raw'] = sum_s

	mutation = {}
	for index in df.index:
		mutation[index] = pos_AA_codon(list(getcodon(index,lib)),lib,start)
		m = pd.Series(mutation)
	df['Mutation'] = m

	name = ["T1_log_mut_freq_WT_sub","T2_log_mut_freq_WT_sub","T3_log_mut_freq_WT_sub","T4_log_mut_freq_WT_sub","T5_log_mut_freq_WT_sub","T6_log_mut_freq_WT_sub","T7_log_mut_freq_WT_sub","T8_log_mut_freq_WT_sub","T9_log_mut_freq_WT_sub"]
	log_rel_cor = pd.read_csv(lib_name + "_library_log_rel_corrected.csv",index_col = 0,names = name)
	df = pd.concat([df,log_rel_cor],axis = 1)

	name = ["T1_WT_freq/mut_freq","T2_WT_freq/mut_freq","T3_WT_freq/mut_freq","T4_WT_freq/mut_freq","T5_WT_freq/mut_freq","T6_WT_freq/mut_freq","T7_WT_freq/mut_freq","T8_WT_freq/mut_freq","T9_WT_freq/mut_freq"]
	rel_abund_ratio = pd.read_csv(lib_name + "_library_rel_abundance_ratio.csv",index_col = 0,names = name)
	df = pd.concat([df,rel_abund_ratio],axis = 1)

	ratio_avg = {}
	for index in df.index:
		ratio_avg[index] = np.mean(df.loc[index,"T1_WT_freq/mut_freq":"T9_WT_freq/mut_freq"])
	avg_r = pd.Series(ratio_avg)
	df['Avg_WT_freq/mut_freq'] = avg_r

	name = ["Fitness"]
	fit = pd.read_csv(lib_name + "_library_fitness.csv",index_col = 0,names = name)
	df = pd.concat([df,fit],axis = 1)
	name = ["SE"]
	SE = pd.read_csv(lib_name + "_library_fitness_SE.csv",index_col = 0,names = name)
	df = pd.concat([df,SE],axis = 1)
	name = ["pval"]
	pval = pd.read_csv(lib_name + "_library_fitness_pval.csv",index_col = 0,names = name)
	df = pd.concat([df,pval],axis = 1)
	name = ["rsq"]
	pval = pd.read_csv(lib_name + "_library_fitness_rsq.csv",index_col = 0,names = name)
	df = pd.concat([df,pval],axis = 1)
	name = ["confint"]
	pval = pd.read_csv(lib_name + "_library_fitness_conf_int.csv",index_col = 0,names = name)
	df = pd.concat([df,pval],axis = 1)
	name = ["rmse"]
	pval = pd.read_csv(lib_name + "_library_fitness_RMSE.csv",index_col = 0,names = name)
	df = pd.concat([df,pval],axis = 1)


	df.to_csv(lib_name + "_summary.csv")


def getcodon(seq,lib):
	index = 0
	seq_slice = seq[index:index+3]
	#print(seq)
	if "A" in seq or "T" in seq or "G" in seq or "C" in seq:
		while "A" not in seq_slice and "T" not in seq_slice and "G" not in seq_slice and "C" not in seq_slice:
			index = index + 3
			if index > len(seq):
				break
			seq_slice = seq[index:index+3]
		codon = seq[index:index+3]
		if index != 0:
			index = int(index/3)
	else:
		return ("WT","WT")
	return (int(index),codon)

def pos_AA_codon(pos_codon, lib,start):
	index = 0
	if pos_codon[0] == "WT":
		pos_codon.append("WT")
		return pos_codon
	for cha in pos_codon[1]:
		if cha == "-":
			pos_codon[1] = pos_codon[1][:index] + lib[pos_codon[0]*3+index] + pos_codon[1][index+1:]
		index = index+1
	pos_codon.append(AA(pos_codon[1]))
	pos_codon[0] = pos_codon[0]+start
	return(pos_codon)


def AA(codon):
	AA_dict = {
		"ATG":"M",
		"GCA":"A",
		"GCC":"A",
		"GCG":"A",
		"GCT":"A",
		"GTA":"V",
		"GTC":"V",
		"GTG":"V",
		"GTT":"V",
		"CTA":"L",
		"CTC":"L",
		"CTG":"L",
		"CTT":"L",
		"TTA":"L",
		"TTG":"L",
		"ATA":"I",
		"ATC":"I",
		"ATT":"I",
		"CCA":"P",
		"CCC":"P",
		"CCG":"P",
		"CCT":"P",
		"TTC":"F",
		"TTT":"F",
		"TGG":"W",
		"GGA":"G",
		"GGC":"G",
		"GGG":"G",
		"GGT":"G",
		"AGC":"S",
		"AGT":"S",
		"TCA":"S",
		"TCC":"S",
		"TCG":"S",
		"TCT":"S",
		"ACA":"T",
		"ACC":"T",
		"ACG":"T",
		"ACT":"T",
		"TGC":"C",
		"TGT":"C",
		"AAC":"N",
		"AAT":"N",
		"CAA":"Q",
		"CAG":"Q",
		"TAC":"Y",
		"TAT":"Y",
		"GAC":"D",
		"GAT":"D",
		"GAA":"E",
		"GAG":"E",
		"AAA":"K",
		"AAG":"K",
		"AGA":"R",
		"AGG":"R",
		"CGA":"R",
		"CGC":"R",
		"CGG":"R",
		"CGT":"R",
		"CAC":"H",
		"CAT":"H",
		"TAG":"*",
		"TAA":"*",
		"TGA":"*"}
	return AA_dict[codon]


if __name__ == "__main__":
	main(sys.argv[1],sys.argv[2],sys.argv[3])
