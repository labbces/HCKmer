#!/usr/bin/python

# Importar bibliotecas
import random 
import argparse 
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from Bio import SeqIO

sequences = {}
sequences_mutado = {}

##ler o arquivo

##definir saida .png

if  __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Um programa que calcula as probabilidades de mutações")
    parser.add_argument('-F','--fastqFile', dest = "fastq_file",required = True, help = "Digite o nome do arquivo com as sequências em formato fasta", type = str)
    parser.add_argument('-M','--fastaFile2',dest = "fastq_file2", required = True,help ="Digite o nome do arquivo com as sequencias do genoma mutado em formato fastaq",type =str)
    parser.add_argument('-O','--outputFile',dest = "output_file",required= True,help = "Digite o nome do output em formato fasta", type =str)
    parser.add_argument('-G','--outputGc',dest = "gc_file",required = True,help = "Digite a saide do gc", type =str)
    
    args = parser.parse_args()

    with open(args.fastq_file, 'r') as fastqhandle, open(args.gc_file, 'w') as gchandle:
        for record in SeqIO.parse(fastqhandle, "fastq"):
            sequences[record.id] = GC(record.seq)
            gchandle.write(f'{record.id}\toriginal\t{sequences[record.id]}\n')
    with open(args.fastq_file2,'r') as fastqhandle2, open(args.gc_file, 'a') as gchandle2:
        for record in SeqIO.parse(fastqhandle2, "fastq"):
             sequences_mutado[record.id] = GC(record.seq)
             gchandle2.write(f'{record.id}\tmutado\t{sequences_mutado[record.id]}\n')

    figure, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    ax1.hist(sequences.values(), bins = 1000,label= 'original',color='green',)
    ax1.hist(sequences_mutado.values(), bins = 1000,label= 'mutado', color='red')
    ax1.set_title("com 1000")
    ax2.hist(sequences.values(), bins = 200,label= 'original',color='green',)
    ax2.hist(sequences_mutado.values(), bins = 200,label= 'mutado', color='red')
    ax2.set_title("com 200")
    
    #fig1 = plt.hist(sequences.values(), bins = np.ceil(1+3.3*np.log(len(sequences))).astype(int))
    #fig2 = plt.hist([sequences.values(),sequences_mutado.values()],bins = 200,label = ['original','mutado'])
    
    plt.savefig(args.output_file+'_colors.png', dpi=200, format='png')      

       
