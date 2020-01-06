import nltk
import string
from rilib import *
from collections import Counter
import eel
from datetime import datetime
import pickle
import sys
import os
import random
import math
import numpy as np

testdir = "./dataset_files"
manager = DatasetManager(testdir)

p_queries = open("queries.p","rb")
queries = pickle.load(p_queries)
p_perts = open("perts.p","rb")
perts = pickle.load(p_perts)

def get_filtered_docs( query , N , S ):
    
    query = query.lower()
    query = re.sub(r'\W+',' ',query)
    qtokens = nltk.word_tokenize(query)
    stoptokens = Counter(nltk.corpus.stopwords.words('english'))
    qtokens = [ t for t in qtokens if t not in stoptokens ]
    query = ' '.join(qtokens)
    
    print(query)
    
    response_docs = manager.docs_of_vectorial_q_mc(query.lower())
    
    final_docs = [ d for d in response_docs if d[1] > S ]
    final_docs = [ d[0] for d in final_docs ]
    
    return final_docs[-N:]

def get_metrics( query, num, N, S ):
    
    response_docs = get_filtered_docs(query.lower() , N, S)
    lq = len ( response_docs )
    print(response_docs)
    print("lq",lq)
    
    if num<10:
        num = '0'+str(num)
    else:
        num = str(num)
    true_docs = perts[num]
    true_docs = [ d+'.cacm' for d in true_docs ]
    dq = len ( true_docs )
    print(true_docs)
    print("dq",dq)
    
    #both_docs = [ d for d in response_docs if d in true_docs ]
    both_docs = [ ]
    for d in true_docs:
        if d in response_docs:
            print(d)
            both_docs.append(d)
    
    bq = len ( both_docs )  
    print("bq",bq)
    
    acc = bq / lq
    rec = bq / dq
    
    return acc, rec
        

N = 10
S = 0.1
num = math.floor ( random.uniform(1,64.99) )
num = 8
q = queries[num-1]

print(num)
print( get_metrics(q,num,N,S) )
    
