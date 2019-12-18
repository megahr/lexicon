#!-*-coding:utf8-*-
from pyexcel_ods import get_data
from collections import OrderedDict
import datetime
import os,sys,json
import re
jezici=set()
space_re=re.compile(r'\s+',re.UNICODE)
#date_to_range={datetime.date(2017, 2, 1):'1-2',datetime.date(2017, 4, 3):'3-4',datetime.date(2017, 6, 5):'5-6'}
date_to_range={datetime.date(2017, 2, 1):'1-2',datetime.date(2017, 4, 3):'3-4',datetime.date(2017, 6, 5):'5-6',datetime.date(2017, 1, 2):'1-2',datetime.date(2017, 3, 4):'3-4',datetime.date(2017, 5, 6):'5-6',datetime.date(2018, 2, 1):'1-2',datetime.date(2018, 4, 3):'3-4',datetime.date(2018, 6, 5):'5-6'}
data=get_data('megahr.konkretnost.ods')
print 'data loaded'
freqs=dict([e[:-1].decode('utf8').split('\t') for e in open('lexeme_frequencies.txt')])
print 'freqs loaded'
ispitanici={}
podaci_ispitanici=data['ispitanici']
for ispitanik in podaci_ispitanici[1:]:
  if len(ispitanik)>1:
    try:
      ispitanik[6]=date_to_range.get(ispitanik[6],ispitanik[6])
    except e:
      print e
      print ispitanik
    ispitanici[ispitanik[0]]=dict(zip(podaci_ispitanici[0][1:],ispitanik[1:]))
    if 'strani jezici' in ispitanici[ispitanik[0]]:
      ispitanici[ispitanik[0]]['strani jezici']=space_re.sub(' ',ispitanici[ispitanik[0]]['strani jezici'].strip(' .').replace('eng','en').replace('.',''))
      for jezik in ispitanici[ispitanik[0]]['strani jezici'].split(' '):
        jezici.add(jezik)
print jezici
#print ispitanici
open('megahr.konkretnost.ispitanici.json','w').write(json.dumps(ispitanici,indent=4).decode('unicode-escape').encode('utf8'))
for key in data:
  print key
  if len(key)!=3:
    print 'other',key
    continue
  for idx in range(40):
    data[key][0][idx+2]=key+'.'+data[key][0][idx+2][1:]+'.'+data[key][0][idx+2][0]
  print len(data[key][0]),len(data[key][1])
  ###!!!
  data_len=max([len(data[key][i]) for i in range(1,20)])
  data[key][0]=data[key][0][:data_len]
  print len(data[key][0]),len(data[key][1])
  if key.endswith('a'):
    output=data[key][:101]
    for row in output:
      if len(row)<data_len:
        row.extend(['']*(data_len-len(row)))
    #print output
  else:
    output[0].extend(data[key][0][2:])
    for idx in range(100):
      output[idx+1].extend(data[key][100-idx][2:])
  if key.endswith('b'):
    output[0].insert(2,'frek')
    for line in output[1:]:
      line[1]={'G':'Vm','I':'Nc','P':'Ag'}[line[1]]
      line.insert(2,freqs[line[0]+'#'+line[1]])
    print 'out',key
    f=open('outs.konkretnost/'+key[:2]+'.txt','w')
    for key in output[0][3:]:
      if key[:-2] not in ispitanici:
        print 'missing ispitanik',key
        break
    for line in output:
      f.write('\t'.join([unicode(e) for e in line]).encode('utf8')+'\n')
    f.close()
