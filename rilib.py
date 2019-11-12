import os 
import re
import nltk
from collections import Counter
import numpy as np

class DatasetManager:

    def __init__(self, path, stopwords_path):
        self.path = path 
        self.files = os.listdir(path) 
        self.size = len(self.files)
        self.stoptokens = self.make_stoptokens(stopwords_path)
        self.descriptors = self.parse_all() 
        self.inverted_index = self.generate_index()
        self.w_inverted_index = self.generate_w_index()

    def make_stoptokens(self,path):
        f = open(path,"r")
        t = f.read()
        return Counter(nltk.word_tokenize(t))

    def parse_all(self):
        ds = []
        for f in self.files:
            ds.append(DatafileDescriptor(f,self))
        return ds

    def generate_index(self):
        index = { }
        for desc in self.descriptors:
            for term,freq in desc.descriptor.items():
                index[(term,desc.name)] = freq
        return index

    def docs_of_token(self, token):
        return [ (item[0][1],item[1]) for item in self.inverted_index.items() if item[0][0] == token ]

    def tokens_of_doc(self, word):
        return [ (item[0][0],item[1]) for item in self.inverted_index.items() if item[0][1] == word ]

    def generate_w_index(self):

        index = { }
        dmf   = { }
        dot   = { }

        for descriptor in self.descriptors:
            dmf[descriptor.name] = descriptor.max_freq
        
        for item in self.inverted_index.items():
            try:
                dot[item[0][0]] += 1
            except KeyError:
                dot[item[0][0]] = 1

        for item in self.inverted_index.items():
            index[item[0]] = ( item[1] / dmf[item[0][1]] ) * ( np.log10( self.size / dot[item[0][0]]) + 1 )

        return index

    def w_docs_of_token(self, token):
        return [ (item[0][1],item[1]) for item in self.w_inverted_index.items() if item[0][0] == token ]

    def w_tokens_of_doc(self, word):
        return [ (item[0][0],item[1]) for item in self.w_inverted_index.items() if item[0][1] == word ]

class DatafileDescriptor:

    def __init__(self, name, manager):
        self.manager = manager
        self.name = name
        self.path = manager.path+'/'+self.name  
        self.io_ref = open(self.path,"r")
        self.text =  self.io_ref.read()
        self.build_descriptor()
        self.max_freq = max(dict(self.descriptor).values())

    def make_tokens(self):
        self.tokens = nltk.word_tokenize(self.remove_punctuation())
        self.tokens = self.remove_stopwords(self.tokens)

    def remove_punctuation(self):
        regex = r'\W+'
        return re.sub(regex,' ',self.text)

    def remove_stopwords(self, tokens):
        return [ t for t in tokens if not self.manager.stoptokens[t.lower()] ]

    def build_descriptor(self):
        self.make_tokens()
        self.descriptor = Counter(self.tokens)
    

        """
        todo:
        - Aujourd'hui is a stopword with punct
        """
        """
        c = self.text
        c = c.replace(","," ")
        c = c.replace(";"," ")
        c = c.replace("."," ")
        c = c.replace(":"," ")
        c = c.replace("?"," ")
        c = c.replace("!"," ")
        c = c.replace("$"," ")
        c = c.replace("#"," ")
        c = c.replace("@"," ")
        c = c.replace("\""," ")
        c = c.replace("/"," ")
        c = c.replace("|"," ")
        c = c.replace("*"," ")
        c = c.replace("+"," ")
        c = c.replace("-"," ")
        c = c.replace("’"," ")
        c = c.replace("`"," ")
        c = c.replace("'"," ")
        return c
        #regex = r"['’,;.:!?_-]+?"
	#return re.sub(regex," ",self.text)
        """
