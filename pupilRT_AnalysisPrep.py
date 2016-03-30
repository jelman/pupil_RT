# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:21:48 2015

@author: jaelman
"""

import pandas as pd
from sas7bdat import SAS7BDAT
import os

###############################
datadir = 'K:/Projects/Pupil_ReactionTime/data'
pupil_fname = 'K:/data/Pupillometry/pupilDS_long.csv'
cogv2_fname = 'K:/data/VETSA2_April2015/vetsa2merged_1dec2015_edits.sas7bdat'
cogv1_fname = 'K:/data/VETSA1_Aug2014/vetsa1merged_21aug2014.sas7bdat'
cogVars_fname = 'K:/Projects/Pupil_ReactionTime/data/ReactionTime_CogVariables.csv'
demo_fname = 'K:/data/VETSA_demo_vars.csv'
rt_fname = 'K:/data/ReactionTime/ReactionTime_processed.csv'
cog_outname = 'ReactionTime_cogData.csv'
mci_fname = 'K:/data/VETSA2_MCI.csv'
simple_outname = 'pupil_simpleRT.csv'
choice_outname = 'pupil_choiceRT.csv'
###############################

# Load demographic data
demodf = pd.read_csv(demo_fname)

# Load vetsa2merged dataset to get head injury data
with SAS7BDAT(cogv2_fname) as f:
    cogdf = f.to_data_frame()
    
cogdf = cogdf[['vetsaid','DSFMAX_v2','HADSHINJ_v2','NUMHINJ_v2']]

# Set missing missing values in head injury variables
cogdf.ix[cogdf['HADSHINJ_v2']==9,'HADSHINJ_v2'] = None
cogdf.ix[cogdf['NUMHINJ_v2']==99,'NUMHINJ_v2'] = None

# Merge demographic and cognitive data
cogdf = demodf.merge(cogdf, how='right', on='vetsaid')

# Save out cognitive data
cog_outfile = os.path.join(datadir, cog_outname)
cogdf.to_csv(cog_outfile, index=False)

# Load pupil data
pupildf = pd.read_csv(pupil_fname)
pupildf = pupildf.drop(['case', 'twin', 'zyg14'], axis=1)

# Load Reaction Time data
RTdf = pd.read_csv(rt_fname)
simpleRT = RTdf[RTdf['TrialType']=='Simple']
choiceRT = RTdf[RTdf['TrialType']=='Choice']

# Load MCI data
MCIdf = pd.read_csv(mci_fname)

#Filter out subjects who were given a Z score of 2 or were not completed
simpleRT = simpleRT.loc[(simpleRT['ZRT_v2']!=2) & 
                      (simpleRT['RTCOMPLETE_v2']==0)]
                      
choiceRT = choiceRT.loc[(choiceRT['ZRT_v2']!=2) & 
                      (choiceRT['RTCOMPLETE_v2']==0)]    
                      
## Merge datasets

# Simple RT                  
pupil_simpleRT = pd.merge(cogdf, pupildf, on='vetsaid', how='right')                      
pupil_simpleRT = pd.merge(pupil_simpleRT, simpleRT, on='vetsaid', how='inner')                  
pupil_simpleRT = pd.merge(pupil_simpleRT, MCIdf[['vetsaid','rMCI_cons_v2']], 
                         on='vetsaid', how='left')   
                             
# Choice RT                                                
pupil_choiceRT = pd.merge(cogdf, pupildf, on='vetsaid', how='right')                      
pupil_choiceRT = pd.merge(pupil_choiceRT, choiceRT, on='vetsaid', how='inner')                  
pupil_choiceRT = pd.merge(pupil_choiceRT, MCIdf[['vetsaid','rMCI_cons_v2']], 
                         on='vetsaid', how='left')   
                         
# Save out files
simple_outfile = os.path.join(datadir,simple_outname)
pupil_simpleRT.to_csv(simple_outfile, index=False)

choice_outfile = os.path.join(datadir,choice_outname)
pupil_choiceRT.to_csv(choice_outfile, index=False)