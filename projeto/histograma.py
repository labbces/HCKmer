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

##ler o arquivo

##definir saida .png

if  __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Um programa que calcula as probabilidades de mutações")
    parser.add_argument('-F','--fastaFile', dest = "fasta_file",required = True, help = "Digite o nome do arquivo com as sequências em formato fasta", type = str)
    parser.add_argument('-O','--outputFile',dest = "output_file",required= True,help = "Digite o nome do output em formato fasta", type =str)
    parser.add_argument('-G','--outputGc',dest = "gc_file",required = True,help = "Digite a saide do gc", type =str)
    
    args = parser.parse_args()

    with open(args.fasta_file, 'r') as fastahandle, open(args.gc_file, 'w') as gchandle:
        for record in SeqIO.parse(fastahandle, "fastq"):
            sequences[record.id] = GC(record.seq)
            gchandle.write(f'{record.id}\t{sequences[record.id]}\n')
             
    fig = plt.hist(sequences.values(), bins = np.ceil(1+3.3*np.log(len(sequences))).astype(int))
    #fig2 = plt.hist(sequences.values(), bins = 200)
    plt.savefig(args.output_file+'.png', dpi=200, format='png')      

       
