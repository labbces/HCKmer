# -*- coding: utf-8 -*-
"""kat-bbmpap-gc-mutado-gc.sh  .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K491TApgZ3PL9ryUJp6rQWbpXrPbVhON
"""

#!/bin/bash
#$ -q all.q
#$ -cwd
#$ -t 1-10
#$ -pe smp 4
module load miniconda3
export PATH="/Storage/data1/felipe.peres/src/KAT/bin/:$PATH"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Storage/data1/felipe.peres/src/libtool-2.4.6/bin/:/Storage/data1/felipe.peres/src/KAT/deps/boost/build/lib/:/Storage/progs/miniconda3/lib/

mut_input_r1=`ls -1 /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/bbmap_high/out_mutado_reads_bbmap_/bbmap_high_${SGE_TASK_ID}/bbmap_high_${SGE_TASK_ID}.fq  `

kat gcp -m 7 -o /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/kat_kmers/saidas_gc/kat_bbmap_mutado_gc_7_${SGE_TASK_ID}.fq  -t 4   $mut_input_r1