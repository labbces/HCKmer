#!/bin/bash
#$ -q all.q
#$ -cwd 
#$ -t 6-10
module load Python/3.7.2
probabilidade=`echo "$SGE_TASK_ID*0.01"| bc` 

python3 script_probabilidade.py -F data/GCF_000146045.2_R64_genomic.fna  -O saidas/out_mutado_${SGE_TASK_ID} -C saidas/out_concat_${SGE_TASK_ID} -P probabilidade 

