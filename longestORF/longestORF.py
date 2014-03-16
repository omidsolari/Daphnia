#!/usr/bin/python
## Author: Omid Shams Solari
## E-mail: omid@genapsys.com
## Date: 03/16/2014
## description: reads the fasta file in sys.argv[1] and writes another multi-fasta
## file in the same directory as input file with longest ORFs


import numpy as np
from Bio import Seq, SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
import longestORFModule as lOM
import sys

print "1. Finding ORFs"

ORF = []
for seq in SeqIO.parse(sys.argv[1],"fasta"):
    orfs = lOM.findORF(seq)
    if len(orfs) == 2:
        [ORF.append(item) for item in orfs]
    else:
        ORF.append(orfs)

print "2. Writing Output"

output = open( sys.argv[1][:sys.argv[1].rfind('.')] + "ORF" + sys.argv[1][sys.argv[1].rfind('.'):], "w")
SeqIO.write(ORF, output, "fasta")
output.close()