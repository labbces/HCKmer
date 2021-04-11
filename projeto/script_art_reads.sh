#!/bin/bash

#$ -cwd
#$ -V
#$ -q all.q

../art_illumina  -ss HS25 -i data/GCF_000146045.2_R64_genomic.fna -p -l 100 -f 100 -m 400  -s 50 -o outputs/outputs_reads/output_read_art_original


