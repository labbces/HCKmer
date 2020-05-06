# Importando Bibliotecas necessárias

from Bio import SeqIO
# Criando uma função que calcula os kmers com base na sequencia quer quer e os kmers que quer
def build_kmers(sequence, ksize):
    # Cria uma lista para armazenas os kmers 
    kmers = []
    n_kmers = len(sequence) - ksize + 1
    # loop para pegar os kmers em cada sequência
    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers, n_kmers
# Abre o arquivo em fasta e faz uma lista com o nome ID e a respectiva sequência
seq_records = list(SeqIO.parse("sequence.fasta", 'fasta'))

# Itera para cada sequência e chama a função criada 
for x in seq_records:
    re = build_kmers(x.seq, ksize)
    print(x.seq)
    print(re[1])
    