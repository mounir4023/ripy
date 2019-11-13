import nltk
import string
from rilib import *
from collections import Counter

#testdir = "./Documents"
#testfile = "d200.txt"
#stopwordsfile = "./stopwords_fr.txt"

#manager = DatasetManager(testdir, stopwordsfile)

text = open("cacm_i_t_w.all").read()

#search = re.findall(r'(?:\n|^)[.]I \d+\n[.]T\n[.\n]*?\n[.]W\n[.\n]*?\n(?:[.]I|$)',text)
search = re.findall(r'(?:\n|^)[.]I \d+\n[.]T\n(?:.|\s)+?\n[.]W\n(?:.|\s)+?(?:[.]I|$)',text)

print(search)
print(len(search))

