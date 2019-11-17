import nltk
import string
from rilib import *
from collections import Counter
import eel

testdir = "./dataset_files"
manager = DatasetManager(testdir)

@eel.expose
def describe_token(token):
    return { 'freq': manager.docs_of_token(token) , 'weight': manager.w_docs_of_token(token) }

@eel.expose
def get_all_docs():
    return manager.files
    


eel.init('assets', allowed_extensions=['.js', '.html', '.css', '.png'])
eel.start('index.html', size=(1024,600), position=(150,50))
#eel.start('index.html', mode='default' )
#eel.start('index.html', mode='electron' )



