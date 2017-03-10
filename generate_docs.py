#!/usr/bin/python
ag=[e.split('\t')[0].split('#')[0] for e in open('ag_shuf_1000.txt')]
nc=[e.split('\t')[0].split('#')[0] for e in open('nc_shuf_1000.txt')]
vm=[e.split('\t')[0].split('#')[0] for e in open('vm_shuf_1000.txt')]
from random import shuffle
all=ag+nc+vm
shuffle(all)
for i in range(30):
	docid=str(i+1).zfill(2)
	open('docs/'+docid+'a.txt','w').write('\n'.join(all[i*100:(i+1)*100])+'\n')
	open('docs/'+docid+'b.txt','w').write('\n'.join(reversed(all[i*100:(i+1)*100]))+'\n')
	