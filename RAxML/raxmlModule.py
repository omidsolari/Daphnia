#!/usr/bin/python
## Author: Omid Shams Solari
## E-mail: omid@genapsys.com
## Date: 05/08/2014

import numpy as np
from Bio import Seq, SeqIO
import os


def findGroup(goodProtDict, groupID, groupProt):
    """ inputs: goodProtDict < dict {proteinID:proteinSeqObject} >
                groupID < string >
                groupProt < list > the proteins belonging to the group with groupID
        output: groupSeq < list [Seq Object] > """
    tmpFile = open('tmpProt.fasta', "w")
    for prot in groupProt:
        SeqIO.write(goodProtDict[prot],tmpFile,"fasta")
    tmpFile.close()
    os.system("./muscle -in tmpProt.fasta -fastaout tmpMuscle.fasta")
    os.system("./raxmlHPC-PTHREADS-AVX -m PROTGAMMAWAG -p 12345 -s tmpMuscle.fasta -T 4 -n " + groupID + ".T")
    os.system("rm tmpProt.fasta tmpMuscle.fasta")


def muscleRAxML(goodProtDict, groupDict):
    """ inputs: goodprotDict < dict {prteinID: proteinSeqObject} >
                groupDict < dict {groupID: groupProteins} >
                destination < string > directory where outputs are written
        outputs: muscle outputs are wrtitten in separate fasta files in destination """
    
    for k,v in groupDict.iteritems():
        if len(v) > 2:
        	print k
        	findGroup(goodProtDict, k , v)


