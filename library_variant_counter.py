import os,re,sys

def main(lib_name,Library):
	library_counts_dic = {}
	rel_mut_WT_abundance = {}
	WT_count = 0

	#first create a textfile of all the library variants
	with open(lib_name+"_MAGE_variants.txt", "w+") as Wfile:
		Rfile = open(lib_name+"_MAGE_oligos.txt","r")
		Wfile.write("-"*(len(Rfile.readline())-1) + "\n")
		Rfile.close()
		Rfile = open(lib_name+"_MAGE_oligos.txt","r")
		for line in Rfile.read().splitlines():
			for variant in (variants(line)):
				Wfile.write(mask(variant,Library) + "\n")
		Rfile.close()

	if not os.path.exists('library_counts'):
		os.makedirs('library_counts')
	if not os.path.exists('library_rel_abundance'):
		os.makedirs('library_rel_abundance')
	if not os.path.exists('library_rel_abunance_wt_sub'):
		os.makedirs('library_rel_abunance_wt_sub')

	merged_files = [i for i in os.listdir("merged") if os.path.isfile(os.path.join("merged",i)) and lib_name in i]
	for file in merged_files:
		f = open(lib_name+"_MAGE_variants.txt")
		for line in f.read().splitlines():
			library_counts_dic[line] = 0
		f.close()
		file = file.split(".")[0]
		write_counts(count_variants("library_parsed\\" +file + ".txt",library_counts_dic),"library_counts\\"+ file + ".txt")

	counts_file = [i for i in os.listdir("library_counts") if os.path.isfile(os.path.join("library_counts",i)) and lib_name in i]
	for file in counts_file:
		f = open("library_counts\\" + file)
		WT_count = int(f.readline().split(" ")[1])
		for line in f.readlines():
			seq,count = line.split(",")
			rel_mut_WT_abundance[seq] = int(count)/WT_count
		f.close()
		write_counts(rel_mut_WT_abundance,"library_rel_abundance\\"+ file)	
	wt_file = "library_rel_abundance\\" + lib_name + "-WT.txt"
	wt_rel_abundance = {}
	with open(wt_file) as wt_file:
		for line in wt_file.readlines():
			wt_rel_abundance[line.split(", ")[0]] = line.split(", ")[1]

	rel_abund_files = [i for i in os.listdir("library_rel_abundance") if os.path.isfile(os.path.join("library_rel_abundance",i)) and lib_name in i]
	for file in rel_abund_files:
		if "WT" not in file:
			with open("library_rel_abundance\\" + file) as f:
				file_counts = {}
				for line in f.readlines():
					if float(line.split(", ")[1]) - float(wt_rel_abundance[line.split(", ")[0]]) > 0.0:
						file_counts[line.split(", ")[0]] = float(line.split(", ")[1]) - float(wt_rel_abundance[line.split(", ")[0]]) 
					else:
						file_counts[line.split(", ")[0]] = 0.0
				write_counts(file_counts, "library_rel_abunance_wt_sub\\" + file)


def mask(seq, mask_seq):
	masked = []
	for i in range(len(seq)):
		if seq[i] == mask_seq[i]:
			masked.append('-')
		else:
			masked.append(seq[i])
	return ''.join(masked)

def count_variants(file,library_counts_dic):
	file = open(file)
	for line in file.read().splitlines():
		seq,count = line.split(",")
		if seq in library_counts_dic.keys():
			library_counts_dic[seq] = int(count)
	file.close()
	return library_counts_dic

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