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
no_perts = [ 34, 35, 41, 46, 47, 50, 51, 52, 53, 54, 55, 56 ]

def get_filtered_docs( query , N , S ):
    
    query = query.lower()
    query = re.sub(r'\W+',' ',query)
    qtokens = nltk.word_tokenize(query)
    stoptokens = Counter(nltk.corpus.stopwords.words('english'))
    qtokens = [ t for t in qtokens if t not in stoptokens ]
    query = ' '.join(qtokens)
    #print(query)
    
    response_docs = manager.docs_of_vectorial_q_mc(query.lower())
    
    final_docs = [ d for d in response_docs if d[1] > S ]
    final_docs = [ d[0] for d in final_docs ]
    
    return final_docs[:N]

def get_metrics( query, num, N, S ):
    
    response_docs = get_filtered_docs(query.lower() , N, S)
    lq = len ( response_docs )
    #print(response_docs)
    #print("lq",lq)
    
    if num<10:
        num = '0'+str(num)
    else:
        num = str(num)
    true_docs = perts[num]
    true_docs = [ d+'.cacm' for d in true_docs ]
    dq = len ( true_docs )
    #print(true_docs)
    #print("dq",dq)
    
    both_docs = [ ]
    for d in true_docs:
        if d in response_docs:
            #print(d)
            both_docs.append(d)
    
    bq = len ( both_docs )  
    #print("bq",bq)
    
    acc = bq / lq
    rec = bq / dq
    
    return acc, rec
        
def mean_metrics(N, S):
    
    test_set = list(perts.keys())
    mean_acc = 0
    mean_rec = 0
    
    for num in test_set:
        num = int(num)
        #print(num)
        q = queries[num-1] 
        #print(q)
        acc , rec = get_metrics(q, num, N, S)
        #print(acc,' ',rec)
        mean_acc += acc
        mean_rec += rec
        
    mean_acc = mean_acc / len(test_set)
    mean_rec = mean_rec / len(test_set)
    
    return mean_acc, mean_rec
        
        
N = [ 20, 40, 60, 80, 100 ]
#S = [ 0.1, 0.25 ]
S = 0.05

accs = { }
recs = { }
accrecs = { }

for n in N:
    acc , rec = mean_metrics( n , S )
    accs[n] = acc
    recs[n] = rec
    accrecs[n] = (acc,rec)

print("")
print(accs)
print("")
print(recs)
print("")
print(accrecs)
print("")

f1 = open('accs.p','wb')
f2 = open('recs.p','wb')
f3 = open('accrecs.p','wb')
pickle.dump(accs,f1)
pickle.dump(recs,f2)
pickle.dump(accrecs,f3)

#save all metrics for each N value
#save mean metrics for each N value























