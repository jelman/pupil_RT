# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:21:48 2015

@author: jaelman
"""

import pandas as pd
import numpy as np
from sas7bdat import SAS7BDAT
import os

###############################
datadir = 'K:/ReactionTime/data'
pupil_fname = 'K:/data/Pupillometry/pupilDS_long.csv'
cogv2_fname = 'K:/pupillometry/data/cognitive/vetsa2merged_23apr2015.sas7bdat'
cogv1_fname = 'K:/pupillometry/data/cognitive/vetsa1merged_21aug2014.sas7bdat'
cogVars_fname = 'K:/ReactionTime/data/ReactionTime_CogVariables.csv'
rt_fname = 'K:/data/ReactionTime/ReactionTime_processed.csv'
cog_outname = 'cogData.csv'
mci_fname = 'K:/data/VETSA2_MCI.csv'
simple_outname = 'pupil_simpleRT.csv'
choice_outname = 'pupil_choiceRT.csv'
###############################

## Get cognitive data ###
# Load cognitive scores
with SAS7BDAT(cogv2_fname) as f:
    cogdf = f.to_data_frame()
    
cogvars = pd.read_csv(cogVars_fname)
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

# Load pupil data
pupildf = pd.read_csv(pupil_fname)

# Load Reaction Time data
RTdf = pd.read_csv(rt_fname)
simpleRT = RTdf[RTdf['TrialType']=='Simple']
choiceRT = RTdf[RTdf['TrialType']=='Choice']

# Load MCI data
MCIdf = pd.read_csv(mci_fname)

## Merge datasets
# Simple RT
pupil_simpleRT = pd.merge(pupildf, simpleRT, left_on='vetsaid', 
                   right_on='SubjectID', how='inner')                  
pupil_simpleRT = pd.merge(pupil_simpleRT, cogdf, left_on='vetsaid', 
                   right_on='vetsaid', how='inner')
pupil_simpleRT = pupil_simpleRT.drop(['case_y','twin_y','zyg14_y',
                                      'SubjectID'], axis=1)
pupil_simpleRT = pupil_simpleRT.rename(columns={'case_x':'case',
                                                'twin_x':'twin',
                                                'zyg14_x':'zyg14'})
pupil_simpleRT = pd.merge(pupil_simpleRT, MCIdf[['vetsaid','rMCI_cons_v2']], 
                         left_on='vetsaid',right_on='vetsaid', how='left')   
                             
# Choice RT                                                
pupil_choiceRT = pd.merge(pupildf, choiceRT, left_on='vetsaid', 
                   right_on='SubjectID', how='inner')
pupil_choiceRT = pd.merge(pupil_choiceRT, cogdf, left_on='vetsaid', 
                   right_on='vetsaid', how='inner')    
pupil_choiceRT = pupil_choiceRT.drop(['case_y','twin_y','zyg14_y',
                                      'SubjectID'], axis=1)                   
pupil_choiceRT = pupil_choiceRT.rename(columns={'case_x':'case',
                                                'twin_x':'twin',
                                                'zyg14_x':'zyg14'})                   
pupil_choiceRT = pd.merge(pupil_choiceRT, MCIdf[['vetsaid','rMCI_cons_v2']], 
                         left_on='vetsaid',right_on='vetsaid', how='left') 
                         
# Save out files
simple_outfile = os.path.join(datadir,simple_outname)
pupil_simpleRT.to_csv(simple_outfile, index=False)

choice_outfile = os.path.join(datadir,choice_outname)
pupil_choiceRT.to_csv(choice_outfile, index=False)