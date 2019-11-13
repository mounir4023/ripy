import re
import os

original = open('cacm.all').read()

#failed regex
#clean = re.sub(r'^[.]B(?:.|\s)*?[.](?:I|$)','',original)

#this removes also .I
#clean = re.sub(r'(?:^|\n)[.]B(?:.|\s)*?(?:[.]I|$)','',original)

#replace with .I
clean = re.sub(r'(?:^|\n)[.]B(?:.|\s)*?(?:[.]I|$)',r'\n.I',original)

#remove last .I
clean = re.sub(r'[.]I$','',clean)

print(clean)
final = open("cacm_i_t_w.all",'w')
final.write(clean)
final.close()


