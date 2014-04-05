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
output = open( sys.argv[1][:sys.argv[1].rfind('.')] + "ORF" + sys.argv[1][sys.argv[1].rfind('.'):], "w")
for seq in SeqIO.parse(sys.argv[1],"fasta"):
    orfs = lOM.findORF(seq)
    if orfs[1] > 1:
        [SeqIO.write(item, output, "fasta") for item in orfs[0]]
    elif orfs[1] == 1:
        SeqIO.write(orfs[0], output, "fasta")

output.close()

print "2. Output: "
print sys.argv[1][:sys.argv[1].rfind('.')] + "ORF" + sys.argv[1][sys.argv[1].rfind('.'):]
