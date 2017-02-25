#!/usr/bin/python
import sys,gzip
lexemefreq={}
for line in gzip.open('hrLex_v1.2.gz'):
  token,lemma,tag,freq,relfreq=line[:-1].split('\t')
  lexeme=lemma+'#'+tag[:2]
  lexemefreq[lexeme]=lexemefreq.get(lexeme,0)+int(freq)
outf=open('lexeme_frequencies.txt','w')
for lexeme,freq in sorted(lexemefreq.items(),key=lambda x:-x[1]):
  outf.write(lexeme+'\t'+str(freq)+'\n')
outf.close()