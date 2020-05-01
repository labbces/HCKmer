# Abrir o arquivo de sequências
## Importando a Biblioteca SeqIO
from Bio import SeqIO
import argparse as args
import sys

parser = args.ArgumentParser(description = " Programa para contar k-mers")
arser = args.ArgumentParser(description = " Programa para contar k-mers")
# Adicionar os argumentos
parser.add_argument('-file',  default = "file.fasta", required = False, dest = "fasta", help = "Arquivo que contém as sequências", type = open)
parser.add_argument( '--W',required= True, help = "O Tamanho da jenala", type = int)
args = parser.parse_args()
FASTA = args.fasta
print(FASTA)
print (args.file.readlines())
# Lendo o arquivo fasta em uma lista
seq_records = list(SeqIO.parse("file.fasta", 'fasta'))


# Fazendo uma lista
variavel = []

# Criando um loop que itera uma sequência cada vez deslizando por janelas "W" que o usuário escolhe
from Bio import SeqIO
seq_records = list(SeqIO.parse("file.fasta", 'fasta'))
# Fazendo uma lista
variavel = []

# Criando um loop que itera uma sequência cada vez deslizando por janelas "W" que o usuário escolhe
for record in SeqIO.parse("file.fasta", "fasta"):
    pos=0
    if pos<len(record)+1:
      seqstr = str(record[pos:pos+W].seq)
      variavel.append("\n"+">"+record.id+"_"+str(pos)+"\n"+seqstr)
      pos=pos+W

print(variavel)

