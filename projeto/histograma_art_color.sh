#!/bin/bash
#$ -q all.q
#$ -cwd 
#$ -t 1-5
module load Python/3.7.2
mut_input_r1=`ls -1 saidas/saidas_reads/out_read_art_mutado_${SGE_TASK_ID}1.fq`
mut_input_r2=`ls -1 saidas/saidas_reads/out_read_art_mutado_${SGE_TASK_ID}2.fq`
org_input_r1=`ls -1 saidas/saidas_reads/output_read_art_original1.fq`
org_input_r2=`ls -1 saidas/saidas_reads/output_read_art_original2.fq`
cat $org_input_r1 $org_input_r2 >saidas/saidas_reads/output_read_art_original_4histo_color${SGE_TASK_ID}.fq
cat $mut_input_r1 $mut_input_r2 > saidas/saidas_reads/output_read_art_mutado_4histo_color${SGE_TASK_ID}.fq
python3 histograma_color.py -F saidas/saidas_reads/output_read_art_original_4histo_color${SGE_TASK_ID}.fq -M saidas/saidas_reads/output_read_art_mutado_4histo_color${SGE_TASK_ID}.fq  -O saidas/histograma/histograma_diploide_art_color${SGE_TASK_ID} -G saidas/histograma/histograma_diploide_gc_art_color${SGE_TASK_ID}

