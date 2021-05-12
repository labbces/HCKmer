#!/bin/bash
#$ -q all.q
#$ -cwd 
#$ -t 1-5
module load Python/3.7.2
mut_input_r1=`ls -1 saidas/saidas_reads/out_mutado_pass_teste_${SGE_TASK_ID}/out_read_pass_mutado${SGE_TASK_ID}.fq`
python3 histograma_color.py -F  saidas/saidas_reads/out_original_pass/out_read_pass_original.fq  -M $mut_input_r1 -O saidas/histograma/histograma_diploide_color_pass_${SGE_TASK_ID} -G saidas/histograma/histograma_diploide_color_gc_pass${SGE_TASK_ID}

