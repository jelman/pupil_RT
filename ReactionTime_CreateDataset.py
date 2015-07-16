# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:53:44 2015

@author: jaelman
"""

import pandas as pd
import os
import numpy as np
    
def filter_trialproc(df):
    """Filter dataframe for TrialProc procedure. This gets rid of Instructions 
    and Initial Fixation slides that occurred at beginning and end of each 
    block."""
    return df[df['Procedure[Trial]']=='TrialProc']        

def filter_RT(df, minRT=75, maxRT=920):
    """ Set trials with an RT below 75ms or above 920ms to 
    missing """
    idx = (df['Stimulus.RT']<75.0)|(df['Stimulus.RT']>920)
    df.ix[idx,'Stimulus.ACC'] = 0    
    df.ix[idx,'Stimulus.RESP'] = np.nan   
    return df
    
def apply_filters(df):
    df = filter_trialproc(df)
    return df
    
def set_miss_RT(df):
    """ Set any trial with inaccurate response to a missing RT. """    
    df.loc[df['Stimulus.ACC']==0,'Stimulus.RT'] = np.nan 
    return df
    
def main(infile, outfile):
    rt_raw = pd.read_csv(infile, sep=',')
    rt_filt = apply_filters(rt_raw)
    rt_filt = set_miss_RT(rt_filt)
    
    
##############################################################
############## Set paths and parameters ######################
##############################################################
datapath = 'K:/ReactionTime/data' # Specify data path of RT data
fname = 'ReactionTime_UCSD_merged.csv' # Name of input data file
infile = os.path.join(datapath,fname) # Input file
outname = 'ReactionTime_UCSD_processed.csv' # Name of file to save out
outfile = os.path.join(datapath, outname) # Output file
##############################################################

if __name__ == "__main__":
    main(infile, outfile)
