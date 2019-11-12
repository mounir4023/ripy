import nltk
import string
from rilib import *
from collections import Counter

testdir = "./Documents"
testfile = "d200.txt"
stopwordsfile = "./stopwords_fr.txt"

manager = DatasetManager(testdir, stopwordsfile)


def test_access3():
    l = manager.w_tokens_of_doc("d111.txt")
    print("mots du document : d111.txt")
    for i in l:
        print(i)

def test_access4():
    l = manager.w_docs_of_token("connaissances")
    print("documents du mots : connaissances")
    for i in l:
        print(i)

test_access3()
print(" ")
test_access4()
"""
def test_access1():
    l = manager.tokens_of_doc("d111.txt")
    print("mots du document : d111.txt")
    for i in l:
        print(i)

def test_access2():
    l = manager.docs_of_token("connaissances")
    print("documents du mots : connaissances")
    for i in l:
        print(i)

#test_access1()
#test_access2()

for k in manager.inverted_index.keys():
    print(k)
"""
