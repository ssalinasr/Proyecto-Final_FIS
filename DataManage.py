# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 11:17:50 2021

@author: sebas
"""

import pandas as pd
import numpy as np

class DataManage:
    
    def __init__(self):
        self.dat = pd.read_excel("dataset.xlsx")
        
    def eliminar_na(self):
        self.dat = self.dat.dropna(axis=0, how='any')
        
    def redondear_le(self):
        rounded = self.dat["Life Expectancy"].apply(np.ceil)
        self.dat["Life Expectancy"] = rounded

    def filtro_años_max(self, year_max):
        self.dat = self.dat.where(self.dat["Year"] >= year_max)
        self.dat = self.dat.dropna(axis=0 , how='any')
        
    def filtro_años_min(self, year_min):
        self.dat = self.dat.where(self.dat["Year"] <= year_min)
        self.dat = self.dat.dropna(axis=0 , how='any')
        
    def filtro_años_rango(self, year_min, year_max):
        self.dat = self.dat.where((self.dat["Year"] >= year_min) & (self.dat["Year"] <= year_max))
        self.dat = self.dat.dropna(axis=0 , how='any') 
        
    def agrupar_por_region(self):
        self.dat = self.dat.groupby('Region')[("Country","Country Code","Life Expectancy")].mean()
        self.redondear_le()
        self.dat = self.dat.reset_index()

    def agrupar_por_ingresos(self):
        self.dat = self.dat.groupby('Income Group')[("Country","Country Code","Life Expectancy")].mean()
        self.redondear_le()
        self.dat = self.dat.reset_index()
        
    def agrupar_por_años(self):
        self.dat = self.dat.groupby('Year')[("Country","Country Code","Life Expectancy")].mean()
        self.redondear_le()
        self.dat = self.dat.reset_index()
        
    def obtener_pais(self, country):
        self.dat = self.dat[["Country","Country Code","Income Group","Year","Life Expectancy"]][self.dat["Country"] == country]
            
    def obtener_dataset(self):
        return self.dat
    
    def data_estadistica_pais(self):

        lbl = 'Esperanza de vida máxima: \n'
        max_e = str(self.dat['Life Expectancy'].max()) + "\n"
        lbl_a = 'año: \n'
        año_e = str(self.dat['Year'][self.dat["Life Expectancy"] == self.dat['Life Expectancy'].max()])+"\n"
        lbl_m = 'Esperanza de vida mínima: \n'
        min_e = str(self.dat['Life Expectancy'].min())+"\n"
        lbl_f = 'año: \n'
        año_m = str(self.dat['Year'][self.dat["Life Expectancy"] == self.dat['Life Expectancy'].min()])+"\n"
        desc = str(self.dat["Life Expectancy"].describe())

        list = []
        list.append(lbl)
        list.append(max_e)
        list.append(lbl_a)
        list.append(año_e)
        list.append(lbl_m)
        list.append(min_e)
        list.append(lbl_f)
        list.append(año_m)
        list.append(desc)

        return list

    def data_estadistica_agrupacion(self):
        lbl = 'Esperanza de vida máxima: \n'
        max_e = str(self.dat['Life Expectancy'].max()) + "\n"
        lbl_m = 'Esperanza de vida mínima: \n'
        min_e = str(self.dat['Life Expectancy'].min())+"\n"
        desc = str(self.dat["Life Expectancy"].describe())

        list = []
        list.append(lbl)
        list.append(max_e)
        list.append(lbl_m)
        list.append(min_e)
        list.append(desc)

        return list