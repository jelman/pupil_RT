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
cog_outname = 'ReactionTime_cogData.csv'
mci_fname = 'K:/data/VETSA2_MCI.csv'
simple_outname = 'pupil_simpleRT.csv'
choice_outname = 'pupil_choiceRT.csv'
###############################

### Get cognitive data ###
# Load cognitive scores
with SAS7BDAT(cogv2_fname) as f:
    cogdf = f.to_data_frame()
    
cogvars = pd.read_csv(cogVars_fname)
cogdf = cogdf[cogvars['NAME']]

# Rename variables for ethinicity, racial category, and education
cogdf = cogdf.rename(columns={'N1_v2':'ETHNICITY',
                              'N2_v2':'RACIALCAT',
                              'tedrev':'EDUCATION'})
                              
# Load vetsa 1 cog data to get handedness
with SAS7BDAT(cogv1_fname) as f:
    cogdf_v1 = f.to_data_frame()

# Rename ethnicity, racial category and education data
cogdf_v1 = cogdf_v1[['vetsaid','L1','L2','tedrev']]
cogdf_v1 = cogdf_v1.rename(columns={'L1':'ETHNICITY',
                                    'L2':'RACIALCAT',
                                    'tedrev':'EDUCATION'})
#Replace missing data values with NA
cogdf_v1['ETHNICITY'] = cogdf_v1['ETHNICITY'].replace(9,np.nan)
cogdf_v1['RACIALCAT'] = cogdf_v1['RACIALCAT'].replace(9,np.nan)
cogdf_v1['EDUCATION'] = cogdf_v1['EDUCATION'].replace(9,np.nan)

# Update missing data in v2 with v1 data
v1cols = ['ETHNICITY','RACIALCAT','EDUCATION']
cogdf = cogdf.set_index('vetsaid')
cogdf_v1 = cogdf_v1.set_index('vetsaid')
cogdf[v1cols] = cogdf[v1cols].combine_first(cogdf_v1[v1cols])
cogdf = cogdf.reset_index()


# Create Apoe 4 carrier variable
apoeidx = cogdf.apoe2014.str.contains('4')
cogdf.ix[apoeidx, 'apoe4'] = 1
cogdf.ix[~apoeidx, 'apoe4'] = 0

# Discretize performance into quantiles
cogdf['dsfquantile_V2'] = pd.qcut(cogdf['dsfraw_V2'], q=4, labels=[1,2,3,4])
cogdf['dsbquantile_V2'] = pd.qcut(cogdf['dsbraw_V2'], q=4, labels=[1,2,3,4])
cogdf['dsptotquantile_V2'] = pd.qcut(cogdf['dsptot_V2'], q=4, labels=[1,2,3,4])
cogdf['DSFMAXquantile_v2'] = pd.qcut(cogdf['DSFMAX_v2'], q=4, labels=[1,2,3,4])
cogdf['afqtquantile_v2'] = pd.qcut(cogdf['afqtpcttran_v2'],q=4,labels=[1,2,3,4])
cogdf['lnquantile_V2'] = pd.qcut(cogdf['lntot_V2'],q=4,labels=[1,2,3,4])

# Set missing missing values in head injury variables
cogdf.ix[cogdf['HADSHINJ_v2']==9,'HADSHINJ_v2'] = None
cogdf.ix[cogdf['NUMHINJ_v2']==99,'NUMHINJ_v2'] = None


# Save out cognitive data
cog_outfile = os.path.join(datadir, cog_outname)
cogdf.to_csv(cog_outfile, index=False)

# Load pupil data
pupildf = pd.read_csv(pupil_fname)

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
pupil_simpleRT = pd.merge(pupildf, simpleRT, left_on='vetsaid', 
                   right_on='vetsaid', how='inner')                  
pupil_simpleRT = pd.merge(pupil_simpleRT, cogdf, left_on='vetsaid', 
                   right_on='vetsaid', how='inner')
pupil_simpleRT = pupil_simpleRT.drop(['case_y','twin_y','zyg14_y'], axis=1)
pupil_simpleRT = pupil_simpleRT.rename(columns={'case_x':'case',
                                                'twin_x':'twin',
                                                'zyg14_x':'zyg14'})
pupil_simpleRT = pd.merge(pupil_simpleRT, MCIdf[['vetsaid','rMCI_cons_v2']], 
                         left_on='vetsaid',right_on='vetsaid', how='left')   
                             
# Choice RT                                                
pupil_choiceRT = pd.merge(pupildf, choiceRT, left_on='vetsaid', 
                   right_on='vetsaid', how='inner')
pupil_choiceRT = pd.merge(pupil_choiceRT, cogdf, left_on='vetsaid', 
                   right_on='vetsaid', how='inner')    
pupil_choiceRT = pupil_choiceRT.drop(['case_y','twin_y','zyg14_y'], axis=1)                   
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