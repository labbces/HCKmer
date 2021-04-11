#!/bin/bash

#$ -cwd
#$ -V
#$ -q all.q
#$ -t 1-5

caminho=/Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/outputs/outputs_reads/out_mutado_pass_teste_${SGE_TASK_ID}
mkdir -p  $caminho 
cd $caminho 
cp  /Storage/data1/nina.pinheiro/iniciacao/HCKmer/projeto/outputs/out_mutado_${SGE_TASK_ID} ./
perl /Storage/data1/nina.pinheiro/iniciacao/software/PaSS/pacbio_mkindex.pl  out_mutado_${SGE_TASK_ID} ./




/Storage/data1/nina.pinheiro/iniciacao/software/PaSS/PaSS -list percentage.txt -index index -m pacbio_sequel -c  /Storage/data1/nina.pinheiro/iniciacao/software/PaSS/C.elegan/elegan.config -r 100000 -t 1 -o ./out_read_pass_mutado${SGE_TASK_ID}
