#!-*-coding:utf8-*-
from pyexcel_ods import save_data
from collections import OrderedDict
import os

def update_dict(d,value,stream):
  for line in stream:
    key=line.split('#')[0]
    if key in d:
      print 'Houston, we have a collision!',key
    d[key]=value

data=OrderedDict()
pos={}
update_dict(pos,'G',open('vm_shuf_1000.txt'))
update_dict(pos,'P',open('ag_shuf_1000.txt'))
update_dict(pos,'I',open('nc_shuf_1000.txt'))

user_index=[]
for doc in sorted(os.listdir('docs/')):
  header=['leksem',u'vr']
  for i in range(20):
    user_index.append(doc.split('.')[0]+'.'+str(i+1).zfill(2))
    header.append('p'+str(i+1).zfill(2))
    header.append(u'd'+str(i+1).zfill(2))
  data.update({doc.split('.')[0]:[header]+[[e.strip().decode('utf8'),pos[e.strip()]] for e in open('docs/'+doc)]})
data.update({'ispitanici':[['ispitanik','spol','godine',u'mjesto rođenja',u'mjesto života','strani jezici',u'čitanje']]+[[e] for e in user_index]})
save_data("megahr.predočivost.ods", data)
