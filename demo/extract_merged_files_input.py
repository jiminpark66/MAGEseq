from Bio import SeqIO
from Bio.Seq import Seq
import os, sys, re, gzip
from datetime import datetime

def get_libary_region(seq_string, scores,Adapter,Adapter_spacer,Library_len):
    # first look for exact match
    Adapter_start = seq_string.find(Adapter)
    if Adapter_start == -1:
        return False, '', []
    start = seq_string.find(Adapter)+len(Adapter)+Adapter_spacer
    end = start+Library_len
    library_seq = seq_string[start:end]
    if len(seq_string) < end:
        return False, '', []
    library_seq = seq_string[start:end]
    library_scores = scores[start:end]
    return True, Seq(library_seq), library_scores

def tabulate(key, counts):
    # add 1 to count for this key, or add it to the dictionary    
    if key in counts:
        counts[key] += 1
    else:
        counts[key] = 1
        
def mask(seq, mask_seq):
    masked = []
    for i in range(len(seq)):
        if seq[i] == mask_seq[i]:
            masked.append('-')
        else:
            masked.append(seq[i])
    return ''.join(masked)

def write_counts(dict, outputfile):
    # write sequences and counts to a text file
    print (outputfile)
    file = open(outputfile, 'w+')
    for w in sorted(dict, key=dict.get, reverse=True):
        file.write('{seq}, {num}\n'.format(seq=w, num=dict[w]))
    file.close()

def main(file_name,Library,Adapter,Adapter_spacer):
    Library_len = len(Library)
    Library_list = []
    min_qscore_threshold = 14

    output_path = ""
    if not os.path.exists('library_discarded'):
        os.makedirs('library_discarded')
    if not os.path.exists('library_parsed'):
        os.makedirs('library_parsed')
    if not os.path.exists('library_lowQ'):
        os.makedirs('library_lowQ')
    if not os.path.exists("log_folder"):
        os.makedirs("log_folder")
    discarded_folder = output_path + 'library_discarded'
    parsed_folder = output_path + 'library_parsed'
    lowQ_folder = output_path + 'library_lowQ'
    log_folder = output_path + "log_folder"

    qscores = {}
    sequences = {}
    sequences_lowQ = {}
    sequences_discarded = {}

    reads_processed_counts = 0
    good_read_counts = 0
    bad_read_counts_lowQ = 0
    bad_read_counts_no_primer = 0

    merged_reads_file = '' + file_name 
    name = file_name.split(".")[0]

    if ".gz" in merged_reads_file:
        handle = gzip.open("merged/" + merged_reads_file,"rt")
    else: 
        handle = merged_reads_file
    print("Parsing of " + merged_reads_file + " started at:" + str(datetime.now()))
    for read in SeqIO.parse(handle, 'fastq'): 
            seq = str(read.seq)
            scores = read.letter_annotations["phred_quality"]
            # print seq
            # print scores 
            keep, library_seq, library_scores = get_libary_region(seq, scores,Adapter,Adapter_spacer,Library_len)
            if keep:
                min_qscore = min(library_scores)
                tabulate(min_qscore, qscores)
                m = mask(str(library_seq), Library) # masked
                # m = str(library_seq) # regular seq

                if min_qscore >= min_qscore_threshold:
                    tabulate(m, sequences)
                    good_read_counts += 1
                else:
                    tabulate(m, sequences_lowQ)
                    bad_read_counts_lowQ += 1
            else:
                bad_read_counts_no_primer += 1
                tabulate(str(seq), sequences_discarded)
            reads_processed_counts += 1

    print ('processed {p} reads, good = {g:.2%}, bad = {b:.2%}\n\t {q:.2%} = low Q score < {QC}\n\t {f:.2%}  = no fwd primer or too short'.format(
            p = reads_processed_counts, 
            g = float(good_read_counts)/reads_processed_counts,     
            b = float(bad_read_counts_lowQ+bad_read_counts_no_primer)/reads_processed_counts,
            QC = min_qscore_threshold,
            q = float(bad_read_counts_lowQ)/reads_processed_counts, 
            f = float(bad_read_counts_no_primer)/reads_processed_counts))
    
    print ('Q score distribution')
    for w in sorted(qscores, reverse=True):
            print('\t{key}, {val}'.format(key=w, val=qscores[w]))
            # print '\n'

    write_counts(sequences, '{folder}/{name}.txt'.format(folder=parsed_folder, name=name))
    write_counts(sequences_lowQ, '{folder}/{name}.txt'.format(folder=lowQ_folder, name=name))
    write_counts(sequences_discarded, '{folder}/{name}.txt'.format(folder=discarded_folder, name=name))
    with open('{folder}/{name}.txt'.format(folder = log_folder,name=name),"w+") as logfile:
        logfile.write('processed {p} reads, good = {g:.2%}, bad = {b:.2%}\n\t {q:.2%} = low Q score < {QC}\n\t {f:.2%}  = no fwd primer or too short'.format(
            p = reads_processed_counts, 
            g = float(good_read_counts)/reads_processed_counts,     
            b = float(bad_read_counts_lowQ+bad_read_counts_no_primer)/reads_processed_counts,
            QC = min_qscore_threshold,
            q = float(bad_read_counts_lowQ)/reads_processed_counts, 
            f = float(bad_read_counts_no_primer)/reads_processed_counts))
        logfile.write("Q scores")
        for w in sorted(qscores, reverse=True):
            logfile.write('\t{key}, {val}\n'.format(key=w, val=qscores[w]))
        logfile.write("Parsing of " + merged_reads_file + " finished at:" + str(datetime.now()))
    print("Parsing of " + merged_reads_file + " finished at:" + str(datetime.now()))
    if ".gz" in merged_reads_file:
        handle.close() # need to close the gz file if we were streaming 
if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
