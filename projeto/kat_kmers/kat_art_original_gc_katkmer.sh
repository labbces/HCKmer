#!/bin/bash
#$ -q all.q
#$ -cwd


module load miniconda3
export PATH="/Storage/data1/felipe.peres/src/KAT/bin/:$PATH"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Storage/data1/felipe.peres/src/libtool-2.4.6/bin/:/Storage/data1/felipe.peres/src/KAT/deps/boost/build/lib/:/Storage/progs/miniconda3/lib/

ORIGINAL1=`ls -1 /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/output_read_art_original1.fq` 
ORIGINAL2=`ls -1 /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/output_read_art_original2.fq` 


 

kat gcp -m 37 -o /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/kat_kmers/saidas_gc/kat_art_gc_original_37  -t 1 "$ORIGINAL1" "$ORIGINAL2"




