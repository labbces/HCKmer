#!/bin/bash
#$ -q all.q
#$ -cwd 
#$ -t 1-5

module load EMBOSS/6.6.0
org_genoma=data/GCF_000146045.2_R64_genomic.fna
mut_genoma=outputs/out_mutado_${SGE_TASK_ID}
geecee $org_genoma outputs/org_genoma.gc
geecee $mut_genoma outputs/mut_genoma_${SGE_TASK_ID}.gc

