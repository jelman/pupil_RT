# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:06:31 2015

@author: jaelman
"""

import pandas as pd
from glob import glob
from sas7bdat import SAS7BDAT
import re
import os, time

def get_sublist(pth,globstr):
    filelist = glob(os.path.join(pth,globstr))
    sublist = [re.sub('.*[Left,Right]-','',w) for w in filelist]
    sublist = [re.sub('.txt','',w) for w in sublist]
    sublist = [re.sub('-1','A',w) for w in sublist]
    sublist = [re.sub('-2','B',w) for w in sublist]
    return sublist
    
def get_mtime(pth, globstr):
    filelist = glob(os.path.join(pth, globstr))    
    mtimes = [time.ctime(os.path.getmtime(f)) for f in filelist]
    return mtimes
    
#################################################################

# Get VETSA 2 data  
datapath = 'K:/data/VETSA2_April2015/vetsa2merged_23apr2015.sas7bdat'
with SAS7BDAT(datapath) as f:
    vetsa2df = f.to_data_frame()
    
rtinfo = vetsa2df[['vetsaid','SITE_v2','RTCOMPLETE_v2','RTCOMPUTER_v2',
                    'RTTIM_v2','ZRT_v2']] 

# Extract vetsaid numbers. This can be used as master list of subject id
vetsaid = vetsa2df.vetsaid

########################################################
# Find duplicate and practice subjects in UCSD dataset #
# before re-generating and merging edat files.         #
########################################################

## Get file listings of UCSD data. 
globstr = '*.txt'
pth = 'K:/data/ReactionTime/UCSD Reaction Time/UCSD V2T2 (VETSA 2 Follow-up)'
vetsaidUC = pd.DataFrame({'vetsaid': get_sublist(pth,globstr), 
                             'mtime': get_mtime(pth,globstr)})
                             
# Check that merged UC edat files contain correct IDs (ie., same as filename)
pth = 'K:/data/ReactionTime/UCSD Reaction Time/UCSD V2T2 (VETSA 2 Follow-up)'
vetsaidUC = pd.Series(get_sublist(pth,globstr), name='vetsaid')
mergedUC = pd.read_csv('K:/data/ReactionTime/UCSD Reaction Time/UCSD V2T2 (VETSA 2 Follow-up)/ReactionTime_UCSD_merged.csv')
mergedUC = pd.Series(mergedUC['SubjectID'].unique(), name='vetsaid')

# Check for ids that are different between filenames and merged edats
# These have been corrected manually 
# This code should not find any discrepancies
diffUC = list(set(vetsaidUC).symmetric_difference(set(mergedUC)))

# Find UCSD practice subjects. These should not be included in the main dataset.
# Practice files have been manually moved to practice subfolder. This should 
# not find anymore subjects.
UCpractice = list(set(vetsaidUC).difference(set(vetsaid)))
UCpractice = pd.Series(UCpractice, name='vetsaid')

# Find missing subjects
UCmissingRT = pd.Series(list(set(vetsaid).difference(set(vetsaidUC))), 
                         name='vetsaid')
UCmissingRT.to_csv('K:/data/ReactionTime/missingReactionTime_UCSD.csv', index=False)

########################################################
# Find duplicate and practice subjects in BU dataset   #
# before re-generating and merging edat files.         #
########################################################