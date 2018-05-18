# -*- coding: utf-8 -*-
"""
Created on Fri May 18 21:59:48 2018

@author: Sateesh
"""

#%%
#The Code is TOO Slow. COuld not finish the run

import pandas as pd

data = pd.read_csv('C:\\Users\Sateesh\Downloads\AIDAPP\SoftwareEngineer-Summer-2018-master\input.txt')
#%%
maxHealth = 2000
maxInjuries = 1000000
#%%
sequence = data['1000000']
numberSlayed = [-1]*len(sequence)
#%%
for start in range(len(sequence)):
    healthLost =0
    injuries = 1
    if max(numberSlayed) > (len(sequence) - start):
        break
    numberSlayed[start] = 0
    for i in range(start,len(sequence)):
        D = sequence[i]
        healthLost += D
        injuries = injuries*D
        if (injuries >= maxInjuries) | (healthLost >= maxHealth):
            break
        numberSlayed[start] += 1
    print('Done ', start)

#%%
for i in range(len(numberSlayed)):
    if numberSlayed[i] == 19:
        print(i)
        
