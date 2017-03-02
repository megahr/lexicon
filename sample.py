#!/usr/bin/python
import sys,gzip
from random import shuffle
lexemefreq={}
for line in gzip.open('hrLex_v1.2.gz'):
  token,lemma,tag,freq,relfreq=line[:-1].split('\t')
  lexeme=lemma+'#'+tag[:2]
  lexemefreq[lexeme]=lexemefreq.get(lexeme,0)+int(freq)
outf=open('lexeme_frequencies.txt','w')
outfnc=open('nc_frequencies.txt','w')
outfag=open('ag_frequencies.txt','w')
outfvm=open('vm_frequencies.txt','w')
outfas=open('as_frequencies.txt','w')
nc=[]
ag=[]
vm=[]
for lexeme,freq in sorted(lexemefreq.items(),key=lambda x:-x[1]):
  outf.write(lexeme+'\t'+str(freq)+'\n')
  if lexeme.endswith('#Nc'):
    outfnc.write(lexeme+'\t'+str(freq)+'\n')
    if freq>=3000:
      nc.append((lexeme,freq))
  elif lexeme.endswith('#Ag'):
    outfag.write(lexeme+'\t'+str(freq)+'\n')
    if freq>=3000:
      ag.append((lexeme,freq))
  elif lexeme.endswith('#Vm'):
    outfvm.write(lexeme+'\t'+str(freq)+'\n')
    if freq>=3000:
      vm.append((lexeme,freq))
  elif lexeme.endswith('#As'):
    outfas.write(lexeme+'\t'+str(freq)+'\n')
outf.close()
outfnc.close()
outfag.close()
outfvm.close()
outfas.close()
shuffle(nc)
shuffle(ag)
shuffle(vm)
def writedown(l,f):
  for lexeme,freq in l:
    f.write(lexeme+'\t'+str(freq)+'\n')
writedown(nc,open('nc_shuf.txt','w'))
writedown(ag,open('ag_shuf.txt','w'))
writedown(vm,open('vm_shuf.txt','w'))
