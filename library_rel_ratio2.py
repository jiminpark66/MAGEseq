import os,re,sys,csv
import pandas as pd
import numpy as np
import math
import xlrd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.tools.eval_measures import rmse
import csv
import math

def main(lib_name,dil_rate):
	ratio = {}
	wt_file = "library_rel_abundance\\" + lib_name + "-WT.txt"
	wt_rel_abund = {}
	with open(wt_file) as wt_file:
		for line in wt_file.readlines():
			wt_rel_abund[line.split(", ")[0]] = line.split(", ")[1]
	if not os.path.exists('library_rel_abundance_ratio'):
		os.makedirs('library_rel_abundance_ratio')
	rel_files = [i for i in os.listdir("library_rel_abundance") if os.path.isfile(os.path.join("library_rel_abundance",i)) and lib_name in i]
	for file in rel_files:
		ratio = {}
		if "WT" not in file:
			with open("library_rel_abundance\\" + file) as f:
				for line in f.readlines():
					if float(line.split(', ')[1]) > 0.0:
						ratio[line.split(", ")[0]] = float(wt_rel_abund[line.split(', ')[0]])/float(line.split(', ')[1])
					else:
						ratio[line.split(", ")[0]] = 0
			write_counts(ratio, "library_rel_abundance_ratio\\" + file)

	ratio_dic = {} #get ratios
	rel_files = [i for i in os.listdir("library_rel_abundance_ratio") if os.path.isfile(os.path.join("library_rel_abundance_ratio",i)) and lib_name in i]
	for file in rel_files:
		with open("library_rel_abundance_ratio\\" + file) as f:
			for line in f.readlines():
				ratio_dic[line.split(',')[0]] = []
	for file in rel_files:
		with open("library_rel_abundance_ratio\\" + file) as f:
			for line in f.readlines():
				ratio_dic[line.split(',')[0]].append(float(line.split(',')[1]))
	with open(lib_name + "_library_rel_abundance_ratio.csv", 'w',newline='') as f:
		for key,value in ratio_dic.items():
			temp_list = [key]
			for item in value:
				temp_list.append(item)
			writer = csv.writer(f,lineterminator = '\n')
			writer.writerow(temp_list)
	log_rel_dic = {} #get log10(rel)
	rel_wt_sub_files = [i for i in os.listdir("library_rel_abunance_wt_sub") if os.path.isfile(os.path.join("library_rel_abunance_wt_sub",i)) and lib_name in i]
	for file in rel_wt_sub_files:
		with open("library_rel_abunance_wt_sub/" + file) as f:
			for line in f.readlines():
				log_rel_dic[line.split(',')[0]] = []
	for file in rel_wt_sub_files:
		with open("library_rel_abunance_wt_sub/" + file) as f:
			for line in f.readlines():
				if float(line.split(',')[1]) >0:
					log_rel_dic[line.split(',')[0]].append(math.log(float(line.split(',')[1]),10))
				else:
					log_rel_dic[line.split(',')[0]].append(0)
	with open(lib_name + "_library_log_rel_corrected.csv", 'w', newline = '') as f:
		for key,value in log_rel_dic.items():
			temp_list = [key]
			for item in value:
				temp_list.append(item)
			writer = csv.writer(f,lineterminator = "\n")
			writer.writerow(temp_list)

	counts_dic = {} #get counts
	counts_sum_dic = {} #get total counts across all time points
	counts_files = [i for i in os.listdir("library_counts") if os.path.isfile(os.path.join("library_counts",i)) and lib_name in i]
	for file in counts_files:
		with open("library_counts/" + file) as f:
			for line in f.readlines():
				counts_dic[line.split(',')[0]] = []
	for file in counts_files:
		if "WT" not in file:
			with open("library_counts/" + file) as f:
				for line in f.readlines():
						counts_dic[line.split(',')[0]].append(int(line.split(',')[1]))
	for key, value in counts_dic.items():
		counts_sum_dic[key] = np.sum(value)
	for file in counts_files:
		if "WT.txt" in file:
			with open("library_counts/" + file) as f:
				for line in f.readlines():
						counts_dic[line.split(',')[0]].append(int(line.split(',')[1]))
	with open(lib_name + "_library_raw_counts.csv", 'w', newline = '') as f:
		for key,value in counts_dic.items():
			temp_list = [key]
			for item in value:
				temp_list.append(item)
			writer = csv.writer(f,lineterminator = "\n")
			writer.writerow(temp_list)
	fit_dict = {}
	SE_dict = {}
	p_dict = {}
	rsq_dict = {}
	conf_dict = {}
	rmse_dict = {}

	for key,value in ratio_dic.items(): #calculate fitness but only if meets requirement, average ratio <0.8 and at least a total of 20 raw counts
		value = list(filter((0.0).__ne__, value))
		value = value[0:3]
		if np.mean(value) > 0.79 or counts_sum_dic[key] <20: #do not calculate fitness
			fit_dict[key] = np.float("nan")
			SE_dict[key] = np.float("nan")
			p_dict[key] = np.float("nan")
			rsq_dict[key] = np.float("nan")
			conf_dict[key] = np.float("nan")
			rmse_dict[key] = np.float("nan")

		else:# calculate fitness
			if 0 not in log_rel_dic[key]:
				time = [0,1,2,3,4,5,6,9,12]
				time = sm.add_constant(time)
				model = smf.OLS(log_rel_dic[key],time)
				results = model.fit()
				fit_dict[key] = results.params[1]/np.log10(1+dil_rate) + 1 #fitness calculation
				SE_dict[key] = results.bse[1]/np.log10(1+dil_rate)
				p_dict[key] = results.pvalues[1]
				rsq_dict[key] = results.rsquared
				conf_dict[key] = results.conf_int()[1]
				rmse_dict[key] = rmse(log_rel_dic[key], results.predict(time))

			elif counts_dic[key][0] > 5 and log_rel_dic[key][1] != 0 and log_rel_dic[key][2] != 0:# has to have first three timepoints and at least 5 counts for the first timepoint
				time = np.array([0,1,2,3,4,5,6,9,12])
				count = np.array(log_rel_dic[key])
				time = time[0:np.where(count==0)[0][0]]
				count = count[0:np.where(count==0)[0][0]]
				count = count.tolist()
				time = time.tolist()
				time = sm.add_constant(time)
				model = smf.OLS(count,time)
				results = model.fit()
				fit_dict[key] = results.params[1]/np.log10(1+dil_rate) + 1
				SE_dict[key] = results.bse[1]/np.log10(1+dil_rate)
				p_dict[key] = results.pvalues[1]
				rsq_dict[key] = results.rsquared
				conf_dict[key] = results.conf_int()[1]
				rmse_dict[key] = rmse(count, results.predict(time))
				
			else:
				fit_dict[key] = "nan"
				SE_dict[key] = "nan"
				p_dict[key] = "nan"
				rsq_dict[key] = "nan"
				conf_dict[key] = "nan"
				rmse_dict[key] = "nan"

	with open(lib_name + "_library_fitness.csv", 'w') as f:
		writer = csv.writer(f,lineterminator = '\n')
		for key, value in fit_dict.items():
			writer.writerow([key, value])
	with open(lib_name + "_library_fitness_SE.csv", 'w') as f:
		writer = csv.writer(f,lineterminator = '\n')
		for key, value in SE_dict.items():
			writer.writerow([key, value])
	with open(lib_name + "_library_fitness_pval.csv", 'w') as f:
		writer = csv.writer(f,lineterminator = '\n')
		for key, value in p_dict.items():
			writer.writerow([key, value])
	with open(lib_name + "_library_fitness_rsq.csv", 'w') as f:
		writer = csv.writer(f,lineterminator = '\n')
		for key, value in rsq_dict.items():
			writer.writerow([key, value])
	with open(lib_name + "_library_fitness_conf_int.csv", 'w') as f:
		writer = csv.writer(f,lineterminator = '\n')
		for key, value in conf_dict.items():
			writer.writerow([key, value])
	with open(lib_name + "_library_fitness_RMSE.csv", 'w') as f:
		writer = csv.writer(f,lineterminator = '\n')
		for key, value in rmse_dict.items():
			writer.writerow([key, value])	

def mask(seq, mask_seq):
	masked = []
	for i in range(len(seq)):
		if seq[i] == mask_seq[i]:
			masked.append('-')
		else:
			masked.append(seq[i])
	return ''.join(masked)

def count_variants(file):
	file = open(file)
	for line in file.read().splitlines():
		seq,count = line.split(",")
		if seq in library_counts.keys():
			library_counts[seq] = int(count)
	file.close()
	return library_counts

def write_counts(dict, outputfile):
	# write sequences and counts to a text file
	print (outputfile)
	file = open(outputfile, 'w+')
	for w in sorted(dict, key=dict.get, reverse=True):
		file.write('{seq}, {num}\n'.format(seq=w, num=dict[w]))
	file.close()

#convert MAGE library sequence from N's to all variants
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

if __name__ == "__main__":
	main(sys.argv[1],sys.argv[2])