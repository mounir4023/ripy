import os 
import re

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
