#!/bin/bash
#$ -q all.q
#$ -cwd 
#$ -t 1-10
module load Python/3.7.2
mut_input_r1=`ls -1 /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/bbmap_high/out_mutado_reads_bbmap_/bbmap_high_${SGE_TASK_ID}`
python3 histograma_color_bbmapp.py   -F /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/bbmap_high/out_original_bbmap  -M $mut_input_r1 -O /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas_histogramas_bbmap_high${SGE_TASK_ID} -G /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas_histogramas_bbmap_high${SGE_TASK_ID}





