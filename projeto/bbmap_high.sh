#!/bin/bash

#$ -cwd
#$ -V
#$ -q all.q
#$ -t 1-10

module load bbmap/38.91
caminho=/Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/bbmap_high/out_mutado_reads_bbmap_/bbmap_high_${SGE_TASK_ID}
mkdir -p  $caminho 
cd $caminho 
input=/Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/out_mutado_${SGE_TASK_ID}




randomreads.sh ref=$input out=bbmap_high_${SGE_TASK_ID}.fq pacbio=t pbmin=0.001 pbmax=0.01 coverage=50 minlength=1500 maxlength=30000 midlength=15000
