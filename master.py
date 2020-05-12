import extract_merged_files_input
import library_variant_counter
import library_rel_ratio2
import library_fitness_matrix
import compile_data_sheet
import library_fitnesspval_matrix,library_fitnessse_matrix, library_fitnessrsq_matrix, library_fitnessconfint_matrix, library_fitnessrmse_matrix

Bin1_Adapter = "GCCGTGCGAAGAAAGAG"
Adapter_spacer = 0 # space between adapter and library start
Bin1_Library = "ATGGTTGAAGCGAACTTACGTCTGGTTATTTCTATCGCTAAGAAATACACCAACCGTGGCTTGCAGTTCCTTGACCTGATTCAGGAAGGCAACATCGGTCTGATGAAAGCGGTTGATAAATTCGAATACCGC" 
Bin1_start = 379
Bin1_end = 422
Bin1_dil_rate = 1.3167 

#extract_merged_files_input.main("Bin1-1.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-2.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-3.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-4.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-5.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-6.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-7.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-8.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-9.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin1-WT.fastq.gz",Bin1_Library,Bin1_Adapter,Adapter_spacer)

#library_variant_counter.main("Bin1",Bin1_Library)
library_rel_ratio2.main("Bin1",Bin1_dil_rate)
library_fitness_matrix.main("Bin1",Bin1_Library,Bin1_start, Bin1_end)
library_fitnesspval_matrix.main("Bin1",Bin1_Library,Bin1_start, Bin1_end)
library_fitnessse_matrix.main("Bin1",Bin1_Library,Bin1_start, Bin1_end)
library_fitnessrsq_matrix.main("Bin1",Bin1_Library,Bin1_start, Bin1_end)
library_fitnessconfint_matrix.main("Bin1",Bin1_Library,Bin1_start, Bin1_end)
library_fitnessrmse_matrix.main("Bin1",Bin1_Library,Bin1_start, Bin1_end)
compile_data_sheet.main("Bin1",Bin1_Library,Bin1_start)

Bin2_Adapter = "GGTTGATAAATTCGAATACCGC"
Adapter_spacer = 0 # space between adapter and library start
Bin2_Library = "CGTGGTTACAAGTTCTCCACCTACGCAACCTGGTGGATCCGTCAGGCGATCACCCGCTCTATCGCGGATCAGGCGCGCACCATCCGTATTCCGGTGCATATGATTGAGACCATCAACAAGCTCAACCGTATTTCTCGCCAGATG" 
Bin2_start = 423
Bin2_end = 470
Bin2_dil_rate = 1.2804

#extract_merged_files_input.main("Bin2-1.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-2.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-3.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-4.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-5.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-6.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-7.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-8.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-9.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin2-WT.fastq.gz",Bin2_Library,Bin2_Adapter,Adapter_spacer)

#library_variant_counter.main("Bin2",Bin2_Library)
library_rel_ratio2.main("Bin2",Bin2_dil_rate)
library_fitness_matrix.main("Bin2",Bin2_Library,Bin2_start, Bin2_end)
library_fitnesspval_matrix.main("Bin2",Bin2_Library,Bin2_start, Bin2_end)
library_fitnessse_matrix.main("Bin2",Bin2_Library,Bin2_start, Bin2_end)
library_fitnessrsq_matrix.main("Bin2",Bin2_Library,Bin2_start, Bin2_end)
library_fitnessconfint_matrix.main("Bin2",Bin2_Library,Bin2_start, Bin2_end)
library_fitnessrmse_matrix.main("Bin2",Bin2_Library,Bin2_start, Bin2_end)
compile_data_sheet.main("Bin2",Bin2_Library,Bin2_start)

Bin3_Adapter = "CAACCGTATTTCTCGCCAGATG"
Adapter_spacer = 0 # space between adapter and library start
Bin3_Library = "CTGCAAGAGATGGGCCGTGAACCGACGCCGGAAGAACTGGCTGAACGTATGCTGATGCCGGAAGACAAGATCCGCAAAGTGCTGAAGATCGCCAAAGAGCCAATCTCC" 
Bin3_start = 471
Bin3_end = 506
Bin3_dil_rate = 1.3417

#extract_merged_files_input.main("Bin3-1.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-2.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-3.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-4.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-5.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-6.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-7.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-8.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-9.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin3-WT.fastq.gz",Bin3_Library,Bin3_Adapter,Adapter_spacer)

#library_variant_counter.main("Bin3",Bin3_Library)
library_rel_ratio2.main("Bin3",Bin3_dil_rate)
library_fitness_matrix.main("Bin3",Bin3_Library,Bin3_start, Bin3_end)
library_fitnesspval_matrix.main("Bin3",Bin3_Library,Bin3_start, Bin3_end)
library_fitnessse_matrix.main("Bin3",Bin3_Library,Bin3_start, Bin3_end)
library_fitnessrsq_matrix.main("Bin3",Bin3_Library,Bin3_start, Bin3_end)
library_fitnessconfint_matrix.main("Bin3",Bin3_Library,Bin3_start, Bin3_end)
library_fitnessrmse_matrix.main("Bin3",Bin3_Library,Bin3_start, Bin3_end)
compile_data_sheet.main("Bin3",Bin3_Library,Bin3_start)

Bin4_Adapter = "CGCCAAAGAGCCAATCTCC"
Adapter_spacer = 0 # space between adapter and library start
Bin4_Library = "ATGGAAACGCCGATCGGTGATGATGAAGATTCGCATCTGGGGGATTTCATCGAGGATACCACCCTCGAGCTGCCGCTGGATTCTGCGACCACCGAAAGCCTGCGTGCG"
Bin4_start = 507
Bin4_end = 542
Bin4_dil_rate = 1.416

#extract_merged_files_input.main("Bin4-1.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-2.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-3.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-4.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-5.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-6.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-7.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-8.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-9.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin4-WT.fastq.gz",Bin4_Library,Bin4_Adapter,Adapter_spacer)

#library_variant_counter.main("Bin4",Bin4_Library)
library_rel_ratio2.main("Bin4",Bin4_dil_rate)
library_fitness_matrix.main("Bin4",Bin4_Library,Bin4_start, Bin4_end)
library_fitnesspval_matrix.main("Bin4",Bin4_Library,Bin4_start, Bin4_end)
library_fitnessse_matrix.main("Bin4",Bin4_Library,Bin4_start, Bin4_end)
library_fitnessrsq_matrix.main("Bin4",Bin4_Library,Bin4_start, Bin4_end)
library_fitnessconfint_matrix.main("Bin4",Bin4_Library,Bin4_start, Bin4_end)
library_fitnessrmse_matrix.main("Bin4",Bin4_Library,Bin4_start, Bin4_end)
compile_data_sheet.main("Bin4",Bin4_Library,Bin4_start)

Bin5_Adapter = "CGAAAGCCTGCGTGCG"
Adapter_spacer = 0 # space between adapter and library start
Bin5_Library = "GCAACGCACGACGTGCTGGCTGGCCTGACCGCGCGTGAAGCAAAAGTTCTGCGTATGCGTTTCGGTATCGATATGAACACCGACTACACGCTGGAAGAAGTGGGTAAA"
Bin5_start = 543
Bin5_end = 578
Bin5_dil_rate = 1.524 

#extract_merged_files_input.main("Bin5-1.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-2.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-3.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-4.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-5.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-6.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-7.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-8.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-9.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin5-WT.fastq.gz",Bin5_Library,Bin5_Adapter,Adapter_spacer)

#library_variant_counter.main("Bin5",Bin5_Library)
library_rel_ratio2.main("Bin5",Bin5_dil_rate)
library_fitness_matrix.main("Bin5",Bin5_Library,Bin5_start, Bin5_end)
library_fitnesspval_matrix.main("Bin5",Bin5_Library,Bin5_start, Bin5_end)
library_fitnessse_matrix.main("Bin5",Bin5_Library,Bin5_start, Bin5_end)
library_fitnessrsq_matrix.main("Bin5",Bin5_Library,Bin5_start, Bin5_end)
library_fitnessconfint_matrix.main("Bin5",Bin5_Library,Bin5_start, Bin5_end)
library_fitnessrmse_matrix.main("Bin5",Bin5_Library,Bin5_start, Bin5_end)
compile_data_sheet.main("Bin5",Bin5_Library,Bin5_start)

Bin6_Adapter = "CACGCTGGAAGAAGTGGGTAAA"
Adapter_spacer = 0 # space between adapter and library start
Bin6_Library = "CAGTTCGACGTTACCCGCGAACGTATCCGTCAGATCGAAGCGAAGGCGCTGCGCAAACTGCGTCACCCGAGCCGTTCTGAAGTGCTGCGTAGCTTCCTGGACGATTAA"
Bin6_start = 579
Bin6_end = 614
Bin6_dil_rate = 1.4817

#extract_merged_files_input.main("Bin6-1.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-2.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-3.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-4.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-5.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-6.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-7.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-8.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-9.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)
#extract_merged_files_input.main("Bin6-WT.fastq.gz",Bin6_Library,Bin6_Adapter,Adapter_spacer)

#library_variant_counter.main("Bin6",Bin6_Library)
library_rel_ratio2.main("Bin6",Bin6_dil_rate)
library_fitness_matrix.main("Bin6",Bin6_Library,Bin6_start, Bin6_end)
library_fitnesspval_matrix.main("Bin6",Bin6_Library,Bin6_start, Bin6_end)
library_fitnessse_matrix.main("Bin6",Bin6_Library,Bin6_start, Bin6_end)
library_fitnessrsq_matrix.main("Bin6",Bin6_Library,Bin6_start, Bin6_end)
library_fitnessconfint_matrix.main("Bin6",Bin6_Library,Bin6_start, Bin6_end)
library_fitnessrmse_matrix.main("Bin6",Bin6_Library,Bin6_start, Bin6_end)
compile_data_sheet.main("Bin6",Bin6_Library,Bin6_start) 