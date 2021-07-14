#!/bin/bash
#$ -q all.q
#$ -cwd 
#$ -t 1-10
module load Python/3.7.2
mut_input_r1=`ls -1  /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/out_mutado_pass_teste_${SGE_TASK_ID}/out_read_pass_mutado${SGE_TASK_ID}.fq`
python3 histograma_color_kmer.py  -F   /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/out_original_pass/out_read_pass_original.fq  -M $mut_input_r1 -O saidas_histogramas/histograma_diploide_color_pass_katkmer_${SGE_TASK_ID} -G saidas_histogramas/histograma_diploide_color_gc_pass_katkmer${SGE_TASK_ID}

