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


#N = [ 10, 20, 30, 40, 50, 60, 80, 90, 100 ]
#S = [ 0.1, 0.25 ]

N = [ 20, 40, 60, 80, 100 ]
S = 0.1


f1 = open('accs.p','rb')
f2 = open('recs.p','rb')
f3 = open('accrecs.p','rb')

accs = pickle.load(f1)
recs = pickle.load(f2)
accrecs = pickle.load(f3)

print("\n   Accuracy and recall for S = 0.1\n")
print("    N   \t acc  \t\t\trec")
for n in N:
    if n < 100:
        print("  ",n,"\t",accs[n],"\t",recs[n])
    else:
        print(" ",n,"\t",accs[n],"\t",recs[n])
print("")






















