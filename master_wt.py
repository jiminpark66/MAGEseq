import extract_merged_files_input
import library_variant_counter_wt
#Be sure to have "Binname"_MAGE oligos.txt file 
Adapter_spacer = 0 # space between adapter and library start

Bin3_Adapter = "CAACCGTATTTCTCGCCAGATG"
Bin3_Library = "CTGCAAGAGATGGGCCGTGAACCGACGCCGGAAGAACTGGCTGAACGTATGCTGATGCCGGAAGACAAGATCCGCAAAGTGCTGAAGATCGCCAAAGAGCCAATCTCC" 

#extract_merged_files_input.main("Bin3_WT1.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3_WT2.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
library_variant_counter_wt.main("Bin3_WT1",Bin3_Library)
library_variant_counter_wt.main("Bin3_WT2",Bin3_Library)

Bin4_Adapter = "CGCCAAAGAGCCAATCTCC"
Bin4_Library = "ATGGAAACGCCGATCGGTGATGATGAAGATTCGCATCTGGGGGATTTCATCGAGGATACCACCCTCGAGCTGCCGCTGGATTCTGCGACCACCGAAAGCCTGCGTGCG"

#extract_merged_files_input.main("Bin4_WT1.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4_WT2.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
library_variant_counter_wt.main("Bin4_WT1",Bin4_Library)
library_variant_counter_wt.main("Bin4_WT2",Bin4_Library)

Bin5_Adapter = "CGAAAGCCTGCGTGCG"
Bin5_Library = "GCAACGCACGACGTGCTGGCTGGCCTGACCGCGCGTGAAGCAAAAGTTCTGCGTATGCGTTTCGGTATCGATATGAACACCGACTACACGCTGGAAGAAGTGGGTAAA"

#extract_merged_files_input.main("Bin5_WT1.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5_WT2.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
library_variant_counter_wt.main("Bin5_WT1",Bin5_Library)
library_variant_counter_wt.main("Bin5_WT2",Bin5_Library)

Bin6_Adapter = "CACGCTGGAAGAAGTGGGTAAA"
Bin6_Library = "CAGTTCGACGTTACCCGCGAACGTATCCGTCAGATCGAAGCGAAGGCGCTGCGCAAACTGCGTCACCCGAGCCGTTCTGAAGTGCTGCGTAGCTTCCTGGACGATTAA"

#extract_merged_files_input.main("Bin6_WT1.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6_WT2.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
library_variant_counter_wt.main("Bin6_WT1",Bin6_Library)
library_variant_counter_wt.main("Bin6_WT2",Bin6_Library)