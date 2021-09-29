# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:47:31 2021

@author: sebas
"""

import pandas as pd

df = pd.read_excel("dataset.xlsx")

dfg = df.groupby(('Year')).mean()
dfh = df.groupby(('Region')).mean()
dfi = df.groupby(('Income Group')).mean()


