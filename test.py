import nltk
import string
from rilib import *
from collections import Counter

testdir = "./dataset_files"
testfile = "ripy1000.cacm"
stopwordsfile = "./stopwords_fr.txt"

manager = DatasetManager(testdir)

#print(manager.w_inverted_index)

print(manager.tokens_of_doc(testfile))
print(manager.docs_of_token('computer'))




