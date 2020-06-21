#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: wenrchen
"""

##python script to implement the awk function

import pandas as pd 
import sys

df=pd.read_csv(sys.argv[1],sep='\t',header=None)

drop_index=[]
for i in range(0,df.shape[0]):
    tmp=df.iloc[i][2]
    if((tmp.find('KI270')!=-1) or (tmp.find('GL000')!=-1) or (tmp.find('_alt')!=-1)):
        drop_index.append(i)
        print(i)
    

df=df.drop(df.index[drop_index])

df.to_csv(sys.argv[2],sep='\t',header=None,index=0)
