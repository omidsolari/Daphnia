#!/usr/bin/python
## Author: Omid Shams Solari
## E-mail: omid@genapsys.com
## Date: 05/08/2014


import numpy as np
from Bio import Seq, SeqIO
import os
import sys
import raxmlModule as rax

groupAdd = str(sys.argv[1])
print groupAdd
goodProteinsAdd = str(sys.argv[2])
print goodProteinsAdd

# groupAdd = '../data/NewTwoSpeciesmagmel/testGroup1'
# goodProteinsAdd = '../data/NewTwoSpeciesmagmel/goodProteins.fasta'

print "1. Creating Group Dictionary"
groupFileHandle = open(groupAdd, "r")
groupFile = groupFileHandle.read()
groupFileHandle.close()
groups = groupFile.split('\n')[:-1]

groupDict = {}
for i in groups:
	iTmp = i.split(' ')
	groupDict[iTmp[0][:-1]] = iTmp[1:]

print "2. Creating Good Protein Dictionary"
goodProtDict = {}
for seq in SeqIO.parse(goodProteinsAdd,"fasta"):
	goodProtDict[seq.id] = seq

print "3. RAxML"
rax.muscleRAxML(goodProtDict, groupDict)