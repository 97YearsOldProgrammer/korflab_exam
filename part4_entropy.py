import argparse
import sys
import math
import gzip
import tool

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=11,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
arg = parser.parse_args()

x = str(arg.entropy).split('.')
y = int(''.join(x))

m = 0       # we used to track the location of the sliding window

for defline, seq in tool.read_fasta(arg.file):
    
    k = -1
    seqs = list(seq)
    
    for i in range( len(seqs) - arg.size +1 ):

        part = seq[ i: i+ arg.size ]
        en_f = tool.seq_en( part, arg.size )
        en 	 = int( round(en_f, ndigits=1 ) * 10 ) 
        k	+= 1             # how we track the start point of sliding window         

        if en < y:

            for j in range(arg.size): 

                if m == arg.size: 
                    m = 0
                    break
                    
                m += 1
                z  = k+m-1
                if 	 seqs[z] == 'A': seqs[z] = 'a'
                elif seqs[z] == 'C': seqs[z] = 'c'
                elif seqs[z] == 'G': seqs[z] = 'g'
                elif seqs[z] == 'T': seqs[z] = 't'
                
    seq = ''.join(seqs)
    print(f'{defline}\t{seq}')
    
    