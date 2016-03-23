# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:51:55 2016

@author: jaelman
"""

from sas7bdat import SAS7BDAT
import pandas as pd
import numpy as np
import os

###############################
datadir = 'K:/Projects/Pupil_ReactionTime/data'
pupil_fname = 'K:/data/Pupillometry/pupilDS_long.csv'
cogv2_fname = 'K:/data/VETSA2_April2015/vetsa2merged_1dec2015_edits.sas7bdat'
demo_fname = 'K:/data/VETSA_demo_vars.csv'
cogdomainV1_fname = 'K:/Projects/Cognitive Domains/data/V1_CognitiveDomains_All.csv'
cogdomainV2_fname = 'K:/Projects/Cognitive Domains/data/V2_CognitiveDomains_All.csv'
cog_outname = 'ProcSpeed_cogData.csv'
mci_fname = 'K:/data/VETSA2_MCI.csv'
pupilPS_outname = 'pupil_ProcSpeed.csv'
procspeedVars = ['zProcSpeed','zstrwraw','zstrcraw','ztrl2tran','ztrl3tran',
                 'strwraw','strcraw','TRL2TRAN','TRL3TRAN']
###############################

### Get cognitive and demographic data ###

# Load demographic data
demodf = pd.read_csv(demo_fname)

# Load vetsa2merged dataset to get head injury data
with SAS7BDAT(cogv2_fname) as f:
    cogdf = f.to_data_frame()
    
cogdf = cogdf[['vetsaid','HADSHINJ_v2','NUMHINJ_v2']]

# Set missing missing values in head injury variables
cogdf.ix[cogdf['HADSHINJ_v2']==9,'HADSHINJ_v2'] = None
cogdf.ix[cogdf['NUMHINJ_v2']==99,'NUMHINJ_v2'] = None

# Merge demographic and cognitive data
cogdf = demodf.merge(cogdf, how='right', on='vetsaid')

# Load and merge Proc Speed cognitive domain data
cogdomainV1df = pd.read_csv(cogdomainV1_fname)
cogdomainV1df = cogdomainV1df[['vetsaid']+procspeedVars]
cogdomainV2df = pd.read_csv(cogdomainV1_fname)
cogdomainV2df = cogdomainV2df[['vetsaid']+procspeedVars]
cogdf = cogdf.merge(cogdomainV1df, how='left', on='vetsaid')
cogdf = cogdf.merge(cogdomainV2df, how='left', on='vetsaid', 
                    suffixes=('_v1','_v2'))

# Save out cognitive data
cog_outfile = os.path.join(datadir, cog_outname)
cogdf.to_csv(cog_outfile, index=False)

# Load pupil data
pupildf = pd.read_csv(pupil_fname)
pupildf = pupildf.drop(['case','twin','zyg14'],axis=1)

# Load MCI data
MCIdf = pd.read_csv(mci_fname)
                      
## Merge datasets
pupil_procspeed = pd.merge(cogdf, pupildf, on='vetsaid', how='inner')                  
pupil_procspeed = pupil_procspeed.merge(MCIdf[['vetsaid','rMCI_cons_v2']], 
                         on='vetsaid', how='left')   
                         
# Save out file
procspeed_outfile = os.path.join(datadir,pupilPS_outname)
pupil_procspeed.to_csv(procspeed_outfile, index=False)
