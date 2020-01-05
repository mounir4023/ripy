import nltk
import string
from rilib import *
from collections import Counter
import eel

testdir = "./dataset_files"
testbool = "international * generic + world"
testvect = "world wide web"
manager = DatasetManager(testdir)

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
    return manager.docs_of_boolean_q(query.lower())

@eel.expose
def process_vectorial(query, mode):
    if mode == "IP":
        return manager.docs_of_vectorial_q_ip(query.lower())
    elif mode == "CD":
        return manager.docs_of_vectorial_q_cd(query.lower())
    elif mode == "MC":
        return manager.docs_of_vectorial_q_mc(query.lower())
    elif mode == "MJ":
        return manager.docs_of_vectorial_q_mj(query.lower())
    else:
        return []

@eel.expose
def open_doc(doc):
    return open(manager.path+"/"+doc,"r").read()

@eel.expose
def get_all_docs():
    return manager.files


eel.init('assets', allowed_extensions=['.js', '.html', '.css', '.png'])
eel.start('index.html', size=(1024,600), position=(150,50))
