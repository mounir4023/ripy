import nltk
import string
from rilib import *
from collections import Counter
import eel

testdir = "./dataset_files"
#testbool = "international * generic + world" 
#testvect = "world wide web"
testbool = "test"
testvect = "test"
manager = DatasetManager(testdir)

print("\nquery = test\n")
print("\nword\n")
print(len(manager.docs_of_token(testbool)))
print("\nbool\n")
print(len(manager.docs_of_boolean_q(testbool)))
print("\nvect ip\n")
print(len(manager.docs_of_vectorial_q_ip(testvect)))
print("\nvect cd\n")
print(len(manager.docs_of_vectorial_q_cd(testvect)))
print(" ")
"""
"""

@eel.expose
def describe_token(token):
    description = [ ]
    freqs = manager.docs_of_token(token.lower())
    weights = manager.w_docs_of_token(token.lower())
    for i in range(0,len(freqs)):
        w = round(weights[i][1],2)
        description.append({"document":freqs[i][0],"freq":freqs[i][1],"weight":w})
    return description

@eel.expose
def process_boolean(query):
    booldesc = [ ]
    docs = manager.docs_of_boolean_q(query.lower())
    booldesc[0:1] = docs
    return booldesc

@eel.expose
def process_vectorial(query, mode):
    # dont forget query.lower()
    return 

@eel.expose
def open_doc(doc):
    return open(manager.path+"/"+doc,"r").read()

@eel.expose
def get_all_docs():
    return manager.files
    


#eel.init('assets', allowed_extensions=['.js', '.html', '.css', '.png'])
#eel.start('index.html', size=(1024,600), position=(150,50))




