# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:59:57 2021

@author: sebas
"""

import matplotlib.pyplot as plt
import numpy as np

class ChartManage:
    
    def __init__(self, data):
        self.data = data
        self.df = data.obtener_dataset()

    def generar_grafica_pais(self, country):
        
        cmap = plt.get_cmap("Spectral")
        rescale = lambda y: ((y - np.min(y)) /(np.max(y) - np.min(y)))
        plt.figure(figsize =(15,15))
        x_values = self.df['Year']
        y_values = self.df['Life Expectancy']
        ax = plt.subplot()
        
        ax.set_xticks(x_values)
        ax.set_yticks([i*5 for i in range(17)])
        
        ax.set_title("Esperanza de vida de "+country)
        
        ax.set_xlabel('Años')
        ax.set_ylabel('Esperanza de vida')
        
        
        plt.legend(['Esperanza de vida'])
        plt.xticks(rotation = 90, ha='right')
        
        plt.bar(x_values, y_values, color = cmap(rescale(y_values)))
        plt.show()
        plt.savefig("Gráfica_por_país.png")
        
    def generar_grafica_ing(self):
        
        cmap = plt.get_cmap("Spectral")
        rescale = lambda y: ((y - np.min(y)) /(np.max(y) - np.min(y)))
        
        plt.figure(figsize =(15,15))
        x_values = self.df['Income Group']
        y_values = self.df['Life Expectancy']
        ax = plt.subplot()
        
        ax.set_xticks(range(0,len(x_values)))
        ax.set_xticklabels(x_values)
        ax.set_yticks([i*5 for i in range(17)])
        
        
        ax.set_title("Esperanza de vida de por Ingresos")
        
        ax.set_xlabel('Grupo')
        ax.set_ylabel('Esperanza de vida')
        
        
        plt.legend(['Esperanza de vida'])
        plt.xticks(rotation = 90, ha='right')
        
        plt.bar(x_values, y_values, color = cmap(rescale(y_values)))
        plt.show()
        plt.savefig("Gráfica_por_ingresos.png")
        
    def generar_grafica_reg(self):
        
        cmap = plt.get_cmap("Spectral")
        rescale = lambda y: ((y - np.min(y)) /(np.max(y) - np.min(y)))
        
        plt.figure(figsize =(15,15))
        x_values = self.df['Region']
        y_values = self.df['Life Expectancy']
        ax = plt.subplot()
        
        ax.set_xticks(range(0,len(x_values)))
        ax.set_xticklabels(x_values)
        ax.set_yticks([i*5 for i in range(17)])
        
        ax.set_title("Esperanza de vida de por Region")
        
        ax.set_xlabel('Grupo')
        ax.set_ylabel('Esperanza de vida')
        
        
        plt.legend(['Esperanza de vida'])
        plt.xticks(rotation = 90, ha='right')
        
        plt.bar(x_values, y_values, color=cmap(rescale(y_values)))
        plt.show()
        plt.savefig("Gráfica_por_región.png")

    def generar_grafica_año(self):
        cmap = plt.get_cmap("Spectral")
        rescale = lambda y: ((y - np.min(y)) /(np.max(y) - np.min(y)))
        
        plt.figure(figsize =(15,15))
        x_values = self.df['Year']
        y_values = self.df['Life Expectancy']
        ax = plt.subplot()
        
        ax.set_xticks(x_values)
        ax.set_yticks([i*5 for i in range(17)])
        
        ax.set_title("Esperanza de vida de por Años")
        
        ax.set_xlabel('Grupo')
        ax.set_ylabel('Esperanza de vida')
        
        
        plt.legend(['Esperanza de vida'])
        plt.xticks(rotation = 90, ha='right')
        
        plt.bar(x_values, y_values, color= cmap(rescale(y_values)))
        plt.show()
        plt.savefig("Gráfica_por_años.png")


