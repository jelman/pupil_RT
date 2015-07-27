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

def set_miss_RT(df):
    """ Set any trial with inaccurate response to a missing RT. """    
    df.loc[df['Stimulus.ACC']==0,'Stimulus.RT'] = np.nan 
    return df

def filter_minRT(df, minRT=150):
    """ Set any trial with RT less than the minimum cut-off to missing."""
    minRTmask = df['Stimulus.RT']<minRT
    df.loc[minRTmask,'Stimulus.ACC'] = 0
    df.loc[minRTmask,'Stimulus.RT'] = np.nan 
    return df
    
def filter_maxRT(df):
    """ Set trials with an RT exceeding 3 SD's from the mean 
    within each subject and trial type to missing. """
    filtMaxRT = lambda x: x > (x.mean() + (3*x.std()))
    maxRTmask = df.groupby(['SubjectID','TrialType'])['Stimulus.RT'].apply(filtMaxRT)
    df.loc[maxRTmask,'Stimulus.ACC'] = 0    
    df.loc[maxRTmask,'Stimulus.RESP'] = np.nan   
    return df
    
def apply_filters(df):
    filt_df = filter_trialproc(df)
    filt_df = set_miss_RT(filt_df)
    filt_df = filter_minRT(filt_df)
    filt_df = filter_maxRT(filt_df)
    return filt_df

def calc_hits(trialdf):
    """ Calculate hits (correct responses) """
    return (trialdf['Stimulus.ACC']==1).sum()  
    
def calc_misses(trialdf):
    """ Calculate misses (incorrect response) """
    misses = ((trialdf['Stimulus.ACC']==0) & 
                (trialdf['Stimulus.RESP'].notnull())).sum()
    return misses
    
def calc_NR(trialdf):
    """ Calculate no responses """
    NR = ((trialdf['Stimulus.ACC']==0) & 
                (trialdf['Stimulus.RESP'].isnull())).sum()
    return NR

def calc_medianRT(trialdf):
    """ Calculate median RT for correct trials. """
    return trialdf.ix[trialdf['Stimulus.ACC']==1,'Stimulus.RT'].median()    

def calc_meanRT(trialdf):
    """ Calculate mean RT for correct trials. """
    return trialdf.ix[trialdf['Stimulus.ACC']==1,'Stimulus.RT'].mean()    

def calc_stdRT(trialdf):
    """ Calculate standard deviation of RT for correct trials. """
    return trialdf.ix[trialdf['Stimulus.ACC']==1,'Stimulus.RT'].std()    

def calc_trim_meanRT(trialdf, meanRT, stdRT):
    """ Calculate trimmed mean of RT for correct trials. Excludes any 
    trials that fall outside of 3 standard deviations of the mean. """
    idx = ((trialdf['Stimulus.ACC']==1) &
            (trialdf['Stimulus.RT'] > meanRT-(3*stdRT)) &
            (trialdf['Stimulus.RT'] < meanRT+3*(stdRT)))
    return trialdf.ix[idx,'Stimulus.RT'].mean()

def calc_cvRT(meanRT, stdRT):
    """ Calculate coefficient of variation of RT for correct trials. 
    Divides the standard deviation of RT by mean RT. """
    return meanRT / stdRT

def calc_trial_scores(trialdf):
    """ 
    Calculates summary scores for a given trial type. 
    Input is a dataframe containing trials of one trial type from
    one subject.
    Output is a series where each observation is named by the 
    summary score.
    """
    hits =  calc_hits(trialdf)
    misses =  calc_misses(trialdf)
    NR = calc_NR(trialdf)
    meanRT = calc_meanRT(trialdf)
    medianRT = calc_medianRT(trialdf)
    stdRT = calc_stdRT(trialdf)
    trim_meanRT = calc_trim_meanRT(trialdf, meanRT, stdRT)
    cvRT = calc_cvRT(meanRT, stdRT)
    ntrials = len(trialdf)
    summary_scores = pd.Series({'hits': hits, 'misses': misses, 'NR': NR,
                        'meanRT': meanRT, 'trim_meanRT': trim_meanRT,
                        'medianRT': medianRT, 'stdRT': stdRT, 'cvRT': cvRT, 
                        'ntrials':ntrials})
    return summary_scores

def calc_subject_scores_sides(subjectdf):
    """
    Calculates summary scores for each subject, iterating over trial types. 
    Input is a dataframe containing all trial types for one subject. 
    Output contains one row per trial type and one column per summary score.
    """
    return subjectdf.groupby(['TrialType','SideOfStimuli']).apply(calc_trial_scores)  

def calc_subject_scores_both(subjectdf):
    """
    Calculates summary scores for each subject, iterating over trial types. 
    Input is a dataframe containing all trial types for one subject. 
    Output contains one row per trial type and one column per summary score.
    """
    return subjectdf.groupby('TrialType').apply(calc_trial_scores)  

def summarise_subjects(df):
    """
    Calculates summary scores for the group, iterating over subjects. 
    Input is a dataframe containing all trial types for all subjects.
    Output is transformed such that each row is a subject, and each
    column is a combination of trial type and summary score.
    """
    lrdf = df.groupby('SubjectID').apply(calc_subject_scores_sides)
    lrdf = lrdf.unstack()
    lrdf = lrdf.reorder_levels([1,0], axis=1)
    lrdf.columns = [''.join([col[0][0].lower(),col[1]]).strip() 
                            for col in lrdf.columns.values]
    bothdf = df.groupby('SubjectID').apply(calc_subject_scores_both)
    summed_df = bothdf.merge(lrdf, left_index=True, right_index=True)
    return summed_df

def calc_hitmiss_rate(hits, misses):
    """ Given the number of hits and misses for a particular trial type, 
    calculates the hit rate and miss rate. """
    hitrate = hits / (hits + misses)
    missrate = 1. - hitrate    
    return hitrate, missrate
    
def get_hitmiss_rate(summed_df, trialtypes=[' ','Left','Right']):
    """ Loops over trial types and inserts hit and miss rate for each into 
    the passed dataframe. """
    for trial in trialtypes:
        trial = trial[0].lower().strip()
        hits = summed_df[''.join([trial,'hits'])]
        misses = summed_df[''.join([trial,'misses'])]
        hitratevarname = ''.join([trial,'hitrate'])
        missratevarname = ''.join([trial,'missrate'])
        summed_df[hitratevarname], summed_df[missratevarname] = calc_hitmiss_rate(hits,misses)
    return summed_df

def transform_scores(df, varnames=['mean','std','cv']):
    pattern = '|'.join(varnames)
    varlist = df.columns[df.columns.str.contains(pattern).tolist()].tolist()
    for var in varlist:
        df['_'.join(['log',var])] = np.log(df[var])
    return df
        
def apply_excludes(df):
    """ Placeholder function. """
    exclude_idx =  ((df['lntrials']<8) |
                    (df['rntrials']<8) |
                    (df['ntrials']<16))
    return df.ix[~exclude_idx]
    
def main(infile, outfile):
    rt_raw = pd.read_csv(infile, sep=',')
    rt_filt = apply_filters(rt_raw)
    rt_summed = summarise_subjects(rt_filt)
    rt_rates = get_hitmiss_rate(rt_summed)
    rt_trans = transform_scores(rt_rates)
    rt_clean = apply_excludes(rt_trans)
    rt_clean.to_csv(outfile, index=True)    
    
    
##############################################################
############## Set paths and parameters ######################
##############################################################
datapath = 'K:/data/ReactionTime' # Specify data path of RT data
fname = 'ReactionTime_merged.csv' # Name of input data file
infile = os.path.join(datapath,fname) # Input file
outname = 'ReactionTime_processed.csv' # Name of file to save out
outfile = os.path.join(datapath, outname) # Output file
##############################################################

if __name__ == "__main__":
    main(infile, outfile)
