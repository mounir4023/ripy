import os 
import re
import nltk
from collections import Counter
import numpy as np
from pyparsing import nestedExpr


def clean_cacm(path,cleanname):
    original = open(path).read()
    clean = re.sub(r'(?:^|\n)[.]B(?:.|\s)*?(?:[.]I|$)',r'\n.I',original)
    clean = re.sub(r'[.]I$','',clean)
    final = open(cleanname,'w')
    final.write(clean)
    final.close()
    
def extract_from_cacm(path ,dirname):
    text = open(path).read()
    docs = re.split(r'\n[.]I \d+\n',text)
    docs[0] = re.sub(r'[.]I \d+\n','',docs[0])
    for i in range(len(docs)):
        docs[i] = re.sub(r'[.]T\n','',docs[i])
        docs[i] = re.sub(r'[.]W\n','',docs[i])
    if not os.path.exists('./'+dirname):
        os.makedirs(dirname)
        for i in range(len(docs)):
            f = open(dirname+"/"+str(i+1)+".cacm","w")
            f.write(docs[i])
            f.close()
    else:
        print("Dataset already exists !")

class DatasetManager:

    def __init__(self, path):
        self.path = path 
        self.files = os.listdir(path) 
        self.size = len(self.files)
        self.stoptokens = self.make_stoptokens()
        self.descriptors = self.parse_all() 
        self.inverted_index = self.generate_index()
        self.w_inverted_index = self.generate_w_index()

    def make_stoptokens(self):
        return Counter(nltk.corpus.stopwords.words('english'))

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
            index[item[0]] = ( item[1] / dmf[item[0][1]] ) *  np.log10( (self.size / dot[item[0][0]]) + 1 )

        return index

    def w_docs_of_token(self, token):
        return [ (item[0][1],item[1]) for item in self.w_inverted_index.items() if item[0][0] == token ]

    def w_tokens_of_doc(self, word):
        return [ (item[0][0],item[1]) for item in self.w_inverted_index.items() if item[0][1] == word ]

    def docs_of_boolean_q(self, query):
        docs = [ ]
        tokens = sorted(list(set(re.findall(r'\w+', query))),key = len)
        for doc in self.files:
            q = query
            for token in tokens:
                try:
                    q = q.replace(token,str(self.inverted_index[(token,doc)]))
                except KeyError:
                    q = q.replace(token,'0')
            for freq in re.findall(r'\d+', query):
                if freq != 0 :
                    q = q.replace(freq, 'True')
            q = q.replace('0', 'False')
            q = q.replace('!',' not ')
            q = q.replace('*',' and ')
            q = q.replace('+',' or ')
            if (eval(q)):
                docs.append(doc)
        return docs

    def docs_of_vectorial_q_ip(self, query):
        docs = [ ]
        tokens = nltk.word_tokenize(query)
        for doc in self.files:
            score = 0
            for token in tokens:
                try:
                    score = score + self.inverted_index[(token,doc)]
                except:
                    pass
            if score > 0:
                docs.append((doc,score))
        return sorted(docs, key = lambda doc: doc[1], reverse = True)

    def docs_of_vectorial_q_cd(self, query):
        docs = [ ]
        tokens = Counter(nltk.word_tokenize(query))
        for doc in self.files:
            try:
                score, ps, qfs, dfs = 0, 0, 0, 0
                for item in tokens.items():
                    qf = item[1]
                    df = self.inverted_index[(item[0],doc)]
                    ps = ps + qf * df
                    qfs = qfs + qf * qf
                    dfs = dfs + df * df
                score = 2 * ps / (qfs + dfs)
                if score > 0 :
                    docs.append((doc,score))
            except:
                pass
        return sorted(docs, key = lambda doc: doc[1], reverse = True)

    def docs_of_vectorial_q_mc(self, query):
        return

    def docs_of_vectorial_q_mj(self, query):
        return

class DatafileDescriptor:

    def __init__(self, name, manager):
        self.manager = manager
        self.name = name
        self.path = manager.path+'/'+self.name  
        self.text = self.read_file()
        self.build_descriptor()
        self.max_freq = max(dict(self.descriptor).values())

    def read_file(self):
        f = open(self.path,"r")
        t = f.read()
        f.close()
        return t

    def make_tokens(self):
        self.tokens = nltk.word_tokenize(self.remove_punctuation())
        self.tokens = self.remove_stopwords(self.tokens)
        self.tokens = [ t.lower() for t in self.tokens ]

    def remove_punctuation(self):
        regex = r'\W+'
        return re.sub(regex,' ',self.text)

    def remove_stopwords(self, tokens):
        return [ t for t in tokens if not self.manager.stoptokens[t.lower()] ]

    def build_descriptor(self):
        self.make_tokens()
        self.descriptor = Counter(self.tokens)

