# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:06:31 2015

@author: jaelman
"""

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

