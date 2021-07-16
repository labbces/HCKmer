#!/bin/bash
#$ -q all.q
#$ -cwd
#$ -t 1-10
#$ -pe smp 4 
module load miniconda3
export PATH="/Storage/data1/felipe.peres/src/KAT/bin/:$PATH"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Storage/data1/felipe.peres/src/libtool-2.4.6/bin/:/Storage/data1/felipe.peres/src/KAT/deps/boost/build/lib/:/Storage/progs/miniconda3/lib/

mut_input_r1=`ls -1 /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/out_mutado_pass_teste_${SGE_TASK_ID}/out_read_pass_mutado${SGE_TASK_ID}.fq`
data=/Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/saidas/saidas_reads/out_original_pass/out_read_pass_original.fq 
kat comp -n -m 37  -o /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/kat_kmers/saidas_kmers/kat_comp_pass_37_${SGE_TASK_ID}.fq  -t 4   $data $mut_input_r1




