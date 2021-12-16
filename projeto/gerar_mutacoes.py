#importar bibliotecas
import random 
import argparse 
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from os import system

# Código para probabilidades de mutação


def gerar_mutacao(base_nitrogenada,prob_mutar):
    if random.random() <= prob_mutar and (base_nitrogenada != 'G' and base_nitrogenada != 'C'):
            if random.random()<= 0.5:
                base_nitrogenada = "G"
            else:
                base_nitrogenada = "C"
    else:
        base_nitrogenada = base_nitrogenada

    return base_nitrogenada


def substituicao(seq_dna,prob_mutar):
    
    lista_final = []

    for base_nitrogenada in seq_dna:
         resultado = gerar_mutacao(base_nitrogenada,prob_mutar)

         lista_final.append(resultado)
    
    return "".join(lista_final)
  


if  __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Um programa que calcula as probabilidades de mutações")
    parser.add_argument('-F','--fastaFile', dest = "fasta_file",required = True, help = "Digite o nome do arquivo com as sequências em formato fasta", type = str)
    parser.add_argument('-O','--outputFile',dest = "output_mutado",required= True,help = "Digite o nome do output em formato fasta", type =str)
    parser.add_argument('-C','--outputFileconcat',dest = "output_concat",required= True,help = "Digite o nome do output em formato fasta", type =str)
    parser.add_argument('-P','--probabilidade', dest = "prob_mutar",required = True, help = "Digite a probabilidade de ocorrência de mutação", type = float)

    args = parser.parse_args()

    prob_mutar = args.prob_mutar
   

    with open(args.fasta_file, 'r') as fastahandle, open (args.output_mutado, 'w') as output_handle, open (args.output_concat, 'w') as output_concat:
      for seq_record in SeqIO.parse(fastahandle, 'fasta'):
       print(seq_record.id)
       mutatedSequence = substituicao(seq_record.seq,prob_mutar)
       myID = seq_record.id + '_mut'
       print(myID)
       if len(mutatedSequence) == len(seq_record.seq):
           seqObj=SeqRecord(
                   Seq(mutatedSequence),
                   id=myID,
                   name=myID,
                   description='mutated sequence based on: '+myID
                   )
                         
          
           SeqIO.write(seqObj,output_handle,'fasta')
           SeqIO.write(seq_record,output_concat,'fasta')
           SeqIO.write(seqObj,output_concat,'fasta')
       else:
           print("Não está correto, o comprimento da sequencia original nao é o mesmo da sequencia mutada")
           
       
