import argparse
import gzip
import tool

parser = argparse.ArgumentParser(description='K-mer Locations.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-k' ,'--kvalue', type=int, default=3,
    help='kvalue [%(default)i]')
parser.add_argument('-r' ,'--reverse', action = 'store_true', 
    help='softmask for reverse kmer')
arg = parser.parse_args()

seqs = []
# extracting sequence from fasta file
with gzip.open(arg.file, 'rt') as fp:

    while True:
        line = fp.readline()
        if line == '': break
        line = line.rstrip()
        if line.startswith('>'): continue
        seqs.append(line)

seq = ''.join(seqs)

d_forward = dict()
                    
# output for forward strand
for i in range(0, len(seq) - arg.kvalue +1 ):
                    
    kmer = seq[ i: i+arg.kvalue ]
    
    if kmer in d_forward:
        d_forward[kmer].append(i+1)
    else: 
        d_forward[kmer] = [i+1]
                    
# creating reverse strand
if arg.reverse:
    rseqs = tool.revcomp(seq)
    d_reverse = dict() 
    rseq = ''.join(rseqs)
    

# collecting kmers for both forward and reverse
if arg.reverse:
                    
    for i in range(0, len(rseq) - arg.kvalue +1 ):
                    
        rkmer = rseq[ i: i+arg.kvalue ]
    
        if rkmer in d_reverse:
            d_reverse[rkmer].append(i+1)
        
        else: 
            d_reverse[rkmer] = [i+1]

# final output for forward
print(f'>forward sequence')

for kmer in d_forward:
    positions = ' '.join( map(str, d_forward[kmer]) )
    print(f"{kmer} {positions}")
            

# final output for reverse
if arg.reverse:
    print(f'\n>reverse sequence')
                    
    for rkmer in d_reverse:
        positions = ' '.join( map(str, d_reverse[rkmer]) )
        print(f"{rkmer} {positions}")
