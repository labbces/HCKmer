#!/bin/bash
#$ -q all.q
#$ -cwd
#$ -t 1-10

module load miniconda3
module load gcc/4.9.4
export PATH="/Storage/data1/felipe.peres/src/KAT/bin/:$PATH"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Storage/data1/felipe.peres/src/libtool-2.4.6/bin/:/Storage/data1/felipe.peres/src/KAT/deps/boost/build/lib/:/Storage/progs/miniconda3/lib/

ORIGINAL1=`ls -1 /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/output_read_art_original1.fq` 
ORIGINAL2=`ls -1 /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/output_read_art_original2.fq` 

INFILE1=`ls -1 /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/out_read_art_mutado_${SGE_TASK_ID}1.fq`
INFILE2=${INFILE1/1.fq/2.fq}
 

kat comp -n -m 23 -o /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/kat_kmers/saidas_kmers/kat_art_katkmers_23_${SGE_TASK_ID}.fq   "$ORIGINAL1 $ORIGINAL2" "$INFILE1 $INFILE2" 




