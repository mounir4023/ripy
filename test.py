import nltk
import string
from rilib import *
from collections import Counter
import eel

testdir = "./dataset_files"
#testreq = "(aaa+!bbb+(ccc+!aaa*!ddd+(aaa*ddd))*bbb)"
testreq = "(international + generic)" 
manager = DatasetManager(testdir)

@eel.expose
def describe_token(token):
    description = [ ]
    freqs = manager.docs_of_token(token)
    weights = manager.w_docs_of_token(token)
    for i in range(0,len(freqs)):
        w = round(weights[i][1],2)
        description.append({"document":freqs[i][0],"freq":freqs[i][1],"weight":w})
    return description

@eel.expose
def process_boolean(query):
    print(query)
    booldesc = [ ]
    docs = manager.docs_of_boolean_q(query)
    booldesc[0:1] = docs
    return booldesc

@eel.expose
def open_doc(doc):
    return open(manager.path+"/"+doc,"r").read()

@eel.expose
def get_all_docs():
    return manager.files
    


eel.init('assets', allowed_extensions=['.js', '.html', '.css', '.png'])
eel.start('index.html', size=(1024,600), position=(150,50))

#eel.start('index.html', mode='default' )
#eel.start('index.html', mode='electron' )



