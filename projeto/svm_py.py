# -*- coding: utf-8 -*-
"""svm_py.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iydWZxakw1JuPXhxQR0w6aK4KdLGxSvh
"""

import collections
import pandas as pd
import itertools
import numpy as np
from Bio import SeqIO
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import argparse
from sklearn.model_selection import train_test_split
from scipy.sparse import csr_matrix

if  __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("original_file", help ="originalFile")
    parser.add_argument("mutado_file", help = "mutado file")
    parser.add_argument("kco", help = "kco", type=int)
    parser.add_argument("saida", help = "saida")
    parser.add_argument("saida2",help="saida2")

args = parser.parse_args()

# Opening files safely
try:
    original_file = open(args.original_file, 'r')
except:
    print('File', args.original_file,  'cannot be open')
    exit()

try:
    mutado_file = open(args.mutado_file, 'r')
except:
    print('File', args.mutado_file, 'cannot be open')
    exit()

k = args.kco
saida = args.saida

def kmers_freq(DNA, id, k,label):
    sequence = [DNA[i:i+k] for i in range(len(DNA) - k + 1)]
    return {**{'id': id,'label':label}, **dict(collections.Counter(sequence))}

def kmers_df(original_file,mutado_file, k):
  count_original = 0
  count_mutado =0
  df= pd.DataFrame()
  for record in SeqIO.parse(original_file, "fasta"):
    kmers_fasta = kmers_freq(str(record.seq), record.id, k,'original')
    df= df.append(kmers_fasta,ignore_index=True)

    count_original+=1
  print(f' o arquivo original tem {count_original} sequências')

  for record in SeqIO.parse(mutado_file, "fasta"):
    kmers_fasta = kmers_freq(str(record.seq), record.id, k,'mutado')
    df= df.append(kmers_fasta,ignore_index=True)
    count_mutado+=1


  print(f' o arquivo mutado tem {count_mutado} sequências')


  return df.fillna(0)

df=kmers_df(original_file,mutado_file,k)


# Transformação da variável resposta


X = csr_matrix(df.drop(['id','label'], axis=1).values)
y = df['label'].replace({'original':0,'mutado':1})



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = make_pipeline(StandardScaler(with_mean=False), SVC(gamma='auto', kernel='rbf'))
clf.fit(X_train, y_train)

y_predicted = clf.predict(X_test)

r=classification_report(y_test, y_predicted, target_names=['original','mutado'],output_dict=True)

with open(saida, 'w') as f:
       f.write(str(r))
       f.close()

with open(saida2, 'w') as f:
       f.write(str(X))
       f.close()