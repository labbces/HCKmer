# Importando módulos para lidar com o terminal
import argparse as args
import sys

# Criar um objeto que irá lidar com argumentos
parser = args.ArgumentParser(description = " Programa para contar k-mers")
# Adicionar os argumentos
parser.add_argument('-A',  default = "v.fasta", required = False, help = "Arquivo que contém as sequências", type = str)
parser.add_argument('--K',required = True, help = "O valor que quer para os kmers", type = int)
parser.add_argument( '--W',required= True, help = "O Tamanho da jenala", type = int)
parser.add_argument( '--J', required= True, help = "O pulo de uma janela para a seguinte", type = int)
#  Soliciar ao parser para verificar os argumentos
parsed_args = parser.parse_args()