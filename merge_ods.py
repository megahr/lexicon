#!-*-coding:utf8-*-
from pyexcel_ods import get_data
from collections import OrderedDict
import os,sys

data=get_data('megahr.final.ods')
freqs=dict([e[:-1].decode('utf8').split('\t') for e in open('lexeme_frequencies.txt')])
print type(data)
for key in data:
  if len(key)!=3:
    print 'other',key
    continue
  for idx in range(40):
    data[key][0][idx+2]=key+'.'+data[key][0][idx+2][1:]+'.'+data[key][0][idx+2][0]
  print len(data[key][0]),len(data[key][1])
  data[key][0]=data[key][0][:len(data[key][1])]
  print len(data[key][0]),len(data[key][1])
  if key.endswith('a'):
    output=data[key][:101]
  else:
    output[0].extend(data[key][0][2:])
    for idx in range(100):
      output[idx+1].extend(data[key][100-idx][2:])
  if key.endswith('b'):
    output[0].insert(2,'frek')
    for line in output[1:]:
      line.insert(2,freqs[line[0]+'#'+{'G':'Vm','I':'Nc','P':'Ag'}[line[1]]])
    print 'out',key
    f=open('outs/'+key[:2]+'.txt','w')
    for line in output:
      f.write('\t'.join([unicode(e) for e in line]).encode('utf8')+'\n')
    f.close()
