#!/bin/bash
#$ -q all.q
#$ -cwd 
#$ -t 1-5
module load Python/3.7.2
mut_input_r1=`ls -1 outputs/outputs_reads/output_read_art_${SGE_TASK_ID}1.fq`
mut_input_r2=`ls -1 outputs/outputs_reads/output_read_art_${SGE_TASK_ID}2.fq`
org_input_r1=`ls -1 outputs/outputs_reads/output_read_art_original1.fq`
org_input_r2=`ls -1 outputs/outputs_reads/output_read_art_original2.fq`
cat $mut_input_r1 $mut_input_r2 $org_input_r1 $org_input_r2 >outputs/outputs_reads/output_read_art_diploide_${SGE_TASK_ID}.fq
python3 histograma.py -F outputs/outputs_reads/output_read_art_diploide_${SGE_TASK_ID}.fq -O outputs/histograma/histograma_diploide_art_${SGE_TASK_ID} -G outputs/histograma/histograma_diploide_gc_art${SGE_TASK_ID}

