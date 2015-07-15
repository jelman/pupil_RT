# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:06:31 2015

@author: jaelman
"""

import pandas as pd
from glob import glob
from sas7bdat import SAS7BDAT
import re
import os

def get_sublist(pth,globstr):
    filelist = glob(os.path.join(pth,globstr))
    sublist = [re.sub('.*[Left,Right]-','',w) for w in filelist]
    sublist = [re.sub('.txt','',w) for w in sublist]
    sublist = [re.sub('-1','A',w) for w in sublist]
    sublist = [re.sub('-2','B',w) for w in sublist]
    return sublist
    
#################################################################

# Get VETSA 2 data  
datapath = 'K:/data\VETSA2_April2015/vetsa2merged_23apr2015.sas7bdat'
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
# Computer 405
globstr = '*.txt'
pth = 'K:/data/SimpleRT/405'
vetsaidUC405 = pd.Series(get_sublist(pth,globstr), name='vetsaid')
# Computer 406
pth = 'K:/data/SimpleRT/406'
vetsaidUC406 = pd.Series(get_sublist(pth,globstr), name='vetsaid')

# Find subjects with data on both computers
# Duplicate files have been manually removed. This should not 
# find any duplicates between computers 103 and 104.
UCdups = list(set(vetsaidUC405).intersection(set(vetsaidUC406)))
UCdups = pd.Series(UCdups, name='vetsaid')
