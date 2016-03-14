# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:51:55 2016

@author: jaelman
"""


import pandas as pd
import numpy as np
from sas7bdat import SAS7BDAT
import os

###############################
datadir = 'K:/Projects/Pupil_ReactionTime/data'
pupil_fname = 'K:/data/Pupillometry/pupilDS_long.csv'
cogv2_fname = 'K:/data/VETSA2_April2015/vetsa2merged_1dec2015_edits.sas7bdat'
demo_fname = 'K:/data/VETSA_demo_vars.csv'
cogVars_fname = 'K:/Projects/Pupil_ReactionTime/data/ProcSpeed_CogVariables.csv'
cogdomain_fname = 'K:/Projects/Cognitive Domains/data/V2_CognitiveDomains.csv'
cog_outname = 'ProcSpeed_cogData.csv'
mci_fname = 'K:/data/VETSA2_MCI.csv'
pupilPS_outname = 'pupil_ProcSpeed.csv'
###############################

### Get cognitive and demographic data ###

# Load domegraphic data
demodf = pd.read_csv(demo_fname)

# Load cognitive scores
with SAS7BDAT(cogv2_fname) as f:
    cogdf = f.to_data_frame()
    
cogvars = pd.read_csv(cogVars_fname)
cogdf = cogdf[cogvars['NAME']]

# Set missing missing values in head injury variables
cogdf.ix[cogdf['HADSHINJ_v2']==9,'HADSHINJ_v2'] = None
cogdf.ix[cogdf['NUMHINJ_v2']==99,'NUMHINJ_v2'] = None

# Merge demographic and cognitive data
cogdf = demodf.merge(cogdf, on='vetsaid')

# Load and merge Proc Speed cognitive domain data
cogdomaindf = pd.read_csv(cogdomain_fname)
cogdomaindf = cogdomaindf[['vetsaid','zProcSpeed_v2']]
cogdf = cogdf.merge(cogdomaindf, on='vetsaid')

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
