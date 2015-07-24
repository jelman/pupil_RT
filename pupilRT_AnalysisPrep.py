# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:21:48 2015

@author: jaelman
"""

import pandas as pd
import numpy as np
from sas7bdat import SAS7BDAT
import os

datadir = 'K:/ReactionTime/data'

### Get cognitive data ###
# Load cognitive scores
fname = 'K:/pupillometry/data/cognitive/vetsa2merged_23apr2015.sas7bdat'
with SAS7BDAT(fname) as f:
    cogdf = f.to_data_frame()
    
fname = 'K:/ReactionTime/data/ReactionTime_CogVariables.csv'
cogvars = pd.read_csv(fname)
cogdf = cogdf[cogvars['NAME']]

# Create Apoe 4 carrier variable
apoeidx = cogdf.apoe2014.str.contains('4')
cogdf.ix[apoeidx, 'apoe4'] = 1
cogdf.ix[~apoeidx, 'apoe4'] = 0

# Set missing missing values in head injury variables
cogdf.ix[cogdf['HADSHINJ_v2']==9,'HADSHINJ_v2'] = None
cogdf.ix[cogdf['NUMHINJ_v2']==99,'NUMHINJ_v2'] = None

# Save out cognitive data
outfile = os.path.join(datadir, 'cogData.csv')
cogdf.to_csv(outfile, index=False)

## Load pupil data
pupildf = pd.read_csv('K:/data/Pupillometry/pupilDS_long.csv')

## Load Reaction Time data
axcptdf = pd.read_csv('K:/data/ReactionTime/ReactionTime_processed.csv')