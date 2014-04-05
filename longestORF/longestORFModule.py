#!/usr/bin/python
## Author: Omid Shams Solari
## E-mail: omid@genapsys.com
## Date: 03/16/2014

import numpy as np
from Bio import Seq, SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord

def createRecord(seq, parentRec):
    """ inputs: seq <Seq object>
                parentRec <record object>
        returns: a new record in which newRec.seq = seq, newRec.id = parentRec.id,
                 newRec.name = parentRec.name, newRec.description = parentRec.description,
                 newRec.dbxrefs = parentRec.dbxrefs """
    newRec = SeqRecord(seq)
    newRec.id = str(parentRec.id)
    newRec.name = parentRec.name
    newRec.description = parentRec.description
    newRec.dbxrefs = parentRec.dbxrefs
    
    return newRec


def findORF(proteinRec, table = 11, secondLongestRatio = .5, minLen = 10):
    """ inputs: protein <SeqRecord object>
                table <int> translation table number, default value = 11
                secondLongestRatio <float> ratio of the second longest ORF, default value = .5
        returns: Longest ORF, if length of the second longest is
                 more than secondLongestRatio of the longest, then return both. """
    L = []
    c = 0
    for SEQ in [proteinRec.seq, proteinRec.seq.reverse_complement()]:
        for frame in range(3):
            length = 3 * ((len(proteinRec)-frame) // 3)
            for pro in SEQ[frame:frame+length].translate(table).split("*"):
                if "M" in pro:
                    tmp = pro[pro.find("M"):]
                    if len(tmp) > minLen:
                        L.append(tmp)
                        c = c + 1
    L.sort(key = len)
    #print len(L)
    #print c
    if c > 1:
    	if len(L[-2])>secondLongestRatio*len(L[-1]):
        	return [[createRecord(L[-1],proteinRec),createRecord(L[-2],proteinRec)],c]
    	else:
        	return [createRecord(L[-1],proteinRec),1]
    elif c == 1:
    	return [createRecord(L[-1],proteinRec),1]
    else:
    	return [L,c]


