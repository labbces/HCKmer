#!/bin/bash

#$ -cwd
#$ -V
#$ -q all.q


module load bbmap/38.91
caminho=/Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/bbmap_high/out_original_bbmap

mkdir -p  $caminho 
cd $caminho 
input=/Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/data/GCF_000146045.2_R64_genomic.fna ./





randomreads.sh ref=$input out=bbmap_high_original.fq pacbio=t pbmin=0.001 pbmax=0.01 coverage=50 minlength=1500 maxlength=30000 midlength=15000
