# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 09:36:07 2015

@author: jaelman
"""
import matplotlib.pyploy as plt
import seaborn as sns
import pandas as pd

rt_clean_untrim = pd.read_csv('K:/data/ReactionTime/ReactionTime_processed_untrim.csv')
rt_clean_trim = pd.read_csv('K:/data/ReactionTime/ReactionTime_processed_trim.csv')


f, ax = plt.subplots(nrows=4, ncols=2)
sns.set_style('ticks')

rt_clean_untrim.xs('Simple',level='TrialType')['log_meanRT'].hist(
                            bins=50,ax=ax[0,0],label='Untrimmed',normed=True)
rt_clean_trim.xs('Simple',level='TrialType')['log_meanRT'].hist(
                            bins=50,ax=ax[0,0],alpha=.7,label='Trimmed',normed=True)
ax[0,0].set_xlabel('Simple Log Mean RT')
ax[0,0].legend()

rt_clean_untrim.xs('Simple',level='TrialType')['log_stdRT'].hist(
                            bins=50,ax=ax[1,0],label='Untrimmed',normed=True)
rt_clean_trim.xs('Simple',level='TrialType')['log_stdRT'].hist(
                            bins=50,ax=ax[1,0],alpha=.7,label='Trimmed',normed=True)
ax[1,0].set_xlabel('Simple Log Std RT')
ax[1,0].legend()

rt_clean_untrim.xs('Simple',level='TrialType')['resid_log_stdRT'].hist(
                            bins=50,ax=ax[2,0],label='Untrimmed',normed=True)
rt_clean_trim.xs('Simple',level='TrialType')['resid_log_stdRT'].hist(
                            bins=50,ax=ax[2,0],alpha=.7,label='Trimmed',normed=True)
ax[2,0].set_xlabel('Simlple Log Residual Std RT')
ax[2,0].legend()

rt_clean_untrim.xs('Simple',level='TrialType')['log_cvRT'].hist(
                            bins=50,ax=ax[3,0],label='Untrimmed',normed=True)
rt_clean_trim.xs('Simple',level='TrialType')['log_cvRT'].hist(
                            bins=50,ax=ax[3,0],alpha=.7,label='Trimmed',normed=True)
ax[3,0].set_xlabel('Simple Log CV RT')
ax[3,0].legend()

rt_clean_untrim.xs('Choice',level='TrialType')['log_meanRT'].hist(
                            bins=50,ax=ax[0,1],label='Untrimmed',normed=True)
rt_clean_trim.xs('Choice',level='TrialType')['log_meanRT'].hist(
                            bins=50,ax=ax[0,1],alpha=.7,label='Trimmed',normed=True)
ax[0,1].set_xlabel('Choice Log Mean RT')
ax[0,1].legend()

rt_clean_untrim.xs('Choice',level='TrialType')['log_stdRT'].hist(
                            bins=50,ax=ax[1,1],label='Untrimmed',normed=True)
rt_clean_trim.xs('Choice',level='TrialType')['log_stdRT'].hist(
                            bins=50,ax=ax[1,1],alpha=.7,label='Trimmed',normed=True)
ax[1,1].set_xlabel('Choice Log Std RT')
ax[1,1].legend()

rt_clean_untrim.xs('Choice',level='TrialType')['resid_log_stdRT'].hist(
                            bins=50,ax=ax[2,1],label='Untrimmed',normed=True)
rt_clean_trim.xs('Choice',level='TrialType')['resid_log_stdRT'].hist(
                            bins=50,ax=ax[2,1],alpha=.7,label='Trimmed',normed=True)
ax[2,1].set_xlabel('Choice Log Residual Std RT')
ax[2,1].legend()

rt_clean_untrim.xs('Choice',level='TrialType')['log_cvRT'].hist(
                            bins=50,ax=ax[3,1],label='Untrimmed',normed=True)
rt_clean_trim.xs('Choice',level='TrialType')['log_cvRT'].hist(
                            bins=50,ax=ax[3,1],alpha=.7,label='Trimmed',normed=True)
ax[3,1].set_xlabel('Choice Log CV RT')
ax[3,1].legend()

sns.despine()
plt.tight_layout()
plt.savefig('K:/Experiments/Pupil_ReactionTime/results/ReactionTime_TrimVsUntrim_RT.pdf', dpi=300)

###################################################

f, ax = plt.subplots(ncols=2)
sns.set_style('ticks')

rt_clean_untrim.xs('Simple',level='TrialType')['hits'].hist(
                                    bins=20,ax=ax[0],label='Untrimmed')
rt_clean_trim.xs('Simple',level='TrialType')['hits'].hist(
                                    bins=20,ax=ax[0],alpha=.5,label='Trimmed')
ax[0].set_xlabel('Simple Hits')
ax[0].legend()

rt_clean_untrim.xs('Choice',level='TrialType')['hits'].hist(
                                    bins=20,ax=ax[1],label='Untrimmed')
rt_clean_trim.xs('Choice',level='TrialType')['hits'].hist(
                                    bins=20,ax=ax[1],alpha=.5,label='Trimmed')
ax[1].set_xlabel('Choice Hits')
ax[1].legend()   

sns.despine()
plt.tight_layout()
plt.savefig('K:/Experiments/Pupil_ReactionTime/results/ReactionTime_TrimVsUntrim_Hits.pdf', dpi=300)
                                         