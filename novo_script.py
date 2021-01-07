# -*- coding: UTF-8 -*-
# Importar bibliotecas
import random 
import argparse 
from Bio import SeqIO
# Código para probabilidades de mutação


def gerar_mutacao(base_nitrogenada,prob_mutar,prob_gc):
    if random.random() <= prob_mutar:
         if random.random() <= prob_gc:
            if random.random() <= 0.5:
                base_nitrogenada = "G"
            else:
                base_nitrogenada = "C"
         else:
            if random.random()<= 0.5:
                base_nitrogenada = "A"
            else:
                base_nitrogenada = "T"
    else:
        base_nitrogenada = base_nitrogenada

    return base_nitrogenada


def substituicao(seq_dna,prob_mutar,prob_gc):
    
    lista_final = []

    for base_nitrogenada in seq_dna:
         resultado = gerar_mutacao(base_nitrogenada,prob_mutar,prob_gc)

         lista_final.append(resultado)
    
    return "".join(lista_final)
  




if  __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Um programa que calcula as probabilidades de mutações")
    parser.add_argument('-F','--fastaFile', dest = "fasta_file",required = True, help = "Digite o nome do arquivo com as sequências em formato fasta", type = str)
    parser.add_argument('-P','--probabilidade', dest = "prob_mutar",required = True, help = "Digite a probabilidade de ocorrência de mutação", type = float)
    parser.add_argument('-G', '--prob', dest = "prob_gc", required = True, help = "Digite a probabilidade de ocorrência de GC", type = float)
    args = parser.parse_args()

    prob_mutar = args.prob_mutar
    prob_gc = args.prob_gc

  
   with open('output.fasta', 'w') as output_handle:
     SeqIO.write(seq_dna,output_handle, 'fasta')


    with open(args.fasta_file, 'rU') as fastahandle:
      for seq_record in SeqIO.parse(fastahandle, 'fasta'):
       print(seq_record.id)
       verificacao = substituicao(seq_record.seq,prob_mutar,prob_gc)
       if len(verificacao) == len(seq_record.seq):
         print("Está correto")
       else:
         print("Não está correto")


       print(verificacao)
    
        








