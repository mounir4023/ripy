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


N = [ 10, 20, 30, 40, 50, 60, 80, 90, 100 ]
#S = [ 0.1, 0.25 ]
S = 0.1


f1 = open('accs.p','rb')
f2 = open('recs.p','rb')
f3 = open('accrecs.p','rb')

accs = pickle.load(f1)
recs = pickle.load(f2)
accrecs = pickle.load(f3)

for n in N:
    print("N: ",n,"\tacc: ",accs[n],"\trec",recs[n])






















