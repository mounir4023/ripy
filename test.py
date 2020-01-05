import nltk
import string
from rilib import *
from collections import Counter
import eel
from datetime import datetime
import pickle
import sys
import os

testdir = "./dataset_files"

def training_time():
    
    t = datetime.now()
    manager = DatasetManager(testdir)
    t = datetime.now() - t
    print("")
    print("temps d'indexation: ", t)
    print("")
    
    
def size_of_index():
    
    manager = DatasetManager(testdir)
    index = manager.inverted_index
    windex = manager.w_inverted_index
    p_index = open("index.p","wb")
    p_windex = open("windex.p","wb")
    pickle.dump(index,p_index)
    pickle.dump(windex,p_windex)
    
    type_index = type(index)
    type_windex = type(windex)
    
    ram_index = sys.getsizeof(index)
    ram_windex = sys.getsizeof(windex)
    
    phy_index = os.path.getsize("index.p")
    phy_windex = os.path.getsize("windex.p")
    
    if len(index.items()) == len(windex.items()):
        print("nombre d'entrées: ", len(index.items()) )
    print("")
    print("                      \tfichié inversé\t      fichié inversé pondéré")
    print(" structure de données:\t",type_index,"\t",type_windex)
    print("   espace mémoire RAM:\t    ",ram_index,"     \t    ",ram_windex)
    print("taille pickle exporté:\t    ",phy_index,"     \t    ",phy_windex)
    print("")
    
    


training_time()
size_of_index()
