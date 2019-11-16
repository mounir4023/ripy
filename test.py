import nltk
import string
from rilib import *
from collections import Counter

testdir = "./dataset_files"
testfile = "1000.cacm"
stopwordsfile = "./stopwords_fr.txt"

manager = DatasetManager(testdir)

#print(manager.w_inverted_index)
print(manager.stoptokens)
print(len(manager.stoptokens))



