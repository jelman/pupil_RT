# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:21:48 2015

@author: jaelman
"""

import pandas as pd
from sas7bdat import SAS7BDAT
import os

###############################
datadir = '/home/jelman/netshare/K/Projects/Pupil_ReactionTime/data'
pupil_fname = '~/netshare/K/data/Pupillometry/VETSA2/pupilDS_long.csv'
cog_fname = '/home/jelman/netshare/M/PSYCH/KREMEN/Practice Effect Cognition/data/V1V2_CogData_NASAdj_PE.csv'
demo_fname = '~/netshare/K/data/VETSA_Demographics/VETSA_demo_vars2.csv'
rt_fname = '/home/jelman/netshare/K/data/ReactionTime/ReactionTime_processed.csv'
cog_outname = 'ReactionTime_cogData.csv'
mci_fname = '~/netshare/K/data/VETSA_Demographics/VETSA2_MCI.csv'
outname = 'pupil_RT.csv'
###############################

# Load demographic data
demodf = pd.read_csv(demo_fname)

# Load practice effects data to get RT data
cogdf = pd.read_csv(cog_fname)

cols = ['VETSAID','NAS201TRAN','DSFMAX_V2_nasp','SRTLMEANLOG_V2_nasp',
        'SRTLSTDLOG_V2_nasp','SRTRMEANLOG_V2_nasp','SRTRSTDLOG_V2_nasp',
        'SRTGMEANLOG_V2_nasp','SRTGSTDLOG_V2_nasp','CHRTLMEANLOG_V2_nasp',
        'CHRTRMEANLOG_V2_nasp','CHRTLSTDLOG_V2_nasp','CHRTRSTDLOG_V2_nasp',
        'CHRTGMEANLOG_V2_nasp','CHRTGSTDLOG_V2_nasp']
cogdf.columns
cogdf = cogdf.loc[:,cols]
cogdf.rename(columns={'VETSAID':'vetsaid'}, inplace=True)

# Merge demographic and cognitive data
cogdf = demodf.merge(cogdf, how='right', on='vetsaid')

# Save out cognitive data
cog_outfile = os.path.join(datadir, cog_outname)
cogdf.to_csv(cog_outfile, index=False)

# Load pupil data
pupildf = pd.read_csv(pupil_fname)
pupildf = pupildf.drop(['case', 'twin', 'zyg14'], axis=1)

# Load Reaction Time qc data
RTdf = pd.read_csv(rt_fname)
hitratedf = RTdf.pivot(index='vetsaid',columns='TrialType',values='hitrate')
hitratedf = hitratedf.rename(columns={"Choice":"CHHRT", "Simple":"SHRT"})
RTdf = RTdf.loc[RTdf.TrialType=='Simple',['vetsaid','ZRT_v2','RTCOMPLETE_v2']]
RTdf = RTdf.join(hitratedf, on="vetsaid")

# Load MCI data
MCIdf = pd.read_csv(mci_fname)
MCIdf = MCIdf[['vetsaid','rMCI_cons_v2pe']]

#Filter out subjects who were given a Z score of 2 or were not completed
RTdf = RTdf.loc[(RTdf['ZRT_v2']!=2) &
                      (RTdf['RTCOMPLETE_v2']==0)]


## Merge datasets

# Simple RT
pupil_RT = pd.merge(cogdf, pupildf, on='vetsaid', how='right')
pupil_RT = pd.merge(pupil_RT, RTdf, on='vetsaid', how='inner')
pupil_RT = pd.merge(pupil_RT, MCIdf, on='vetsaid', how='left')

# Save out files
outfile = os.path.join(datadir,outname)
pupil_RT.to_csv(outfile, index=False)
