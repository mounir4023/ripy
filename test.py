import nltk
import string
from rilib import *
from collections import Counter

#testdir = "./Documents"
#testfile = "d200.txt"
#stopwordsfile = "./stopwords_fr.txt"

#manager = DatasetManager(testdir, stopwordsfile)

cacmfile = "cacm_i_t_w.all"
extract_from_cacm(cacmfile)

"""
text = open("cacm_i_t_w.all").read()
#search = re.findall(r'(?:\n|^)[.]I \d+\n[.]T\n(?:.|\s)+?\n[.]W\n(?:.|\s)+?(?:[.]I|$)',text)
#search = re.findall(r'(?:\n|^)[.]I \d+\n(?:[.]T\n(?:.|\s)+?)??(?:[.]W\n(?:.|\s)+?)??(?:[.]I|$)',text)

#search = re.findall(r'(?:\n|^)[.]I \d+\n(?:.|\s)*?(?:\n[.]I|$)',text)
search = re.split(r'\n[.]I \d+\n',text)

print(search[0])
print(len(search))
"""

