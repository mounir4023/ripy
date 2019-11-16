import nltk
import string
from rilib import *
from collections import Counter
import eel

testdir = "./dataset_files"
testfile = "ripy1000.cacm"
stopwordsfile = "./stopwords_fr.txt"

manager = DatasetManager(testdir)

@eel.expose
def describe_token(token):
    return { 'freq': manager.docs_of_token(token) , 'weight': manager.w_docs_of_token(token) }

############## eel conf ##############

eel.init('assets', allowed_extensions=['.js', '.html', '.css', '.png'])
eel.start('index.html')
#eel.start('index.html', mode='electron' )



