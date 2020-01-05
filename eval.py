import nltk
import string
from rilib import *
from collections import Counter
import eel
from datetime import datetime
import pickle
import sys
import os

testdir = "./dataset_files"
manager = DatasetManager(testdir)

p_queries = open("queries.p","rb")
queries = pickle.load(p_queries)
p_perts = open("perts.p","rb")
perts = pickle.load(p_perts)

def get_filtered_docs( query , N , S ):
    
    response_docs = manager.docs_of_vectorial_q_mc(query.lower())
    print(len(response_docs))
    final_docs = [ d for d in response_docs if d[1] > S ]
    print(len(final_docs))
    
    return final_docs
    
N = 10
S = 0
q = queries[0]

get_filtered_docs(q, N, S)
    
    
