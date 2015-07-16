# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:53:44 2015

@author: jaelman
"""

import pandas as pd
import os
import numpy as np
    
def filter_trialproc(df):
    """Filter dataframe for TrialProc procedure. This gets rid of InitialPause 
    and Break slides that occurred at beginning and end of each block."""
    return df[df['Procedure[Trial]']=='TrialProc']
    
def main(infile, outfile):
    pass

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
