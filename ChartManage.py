# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:59:57 2021

@author: sebas
"""

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

class ChartManage:
    
    def __init__(self, data):
        self.data = data
        self.df = data.obtener_dataset()

    def generar_grafica_pais(self, country):
        
        buf =BytesIO()
        cmap = plt.get_cmap("Spectral")
        rescale = lambda y: ((y - np.min(y)) /(np.max(y) - np.min(y)))
        plt.figure(figsize =(10,10))
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
        plt.savefig(buf, format='png', transparent=True)
        #plt.show()
        plt.close()
        buf.seek(0)
        buffer = b''.join(buf)
        b2 = base64.b64encode(buffer)
        plot_url = b2.decode('utf-8')

        return plot_url
        
    def generar_grafica_ing(self):
        
        buf = BytesIO()
        cmap = plt.get_cmap("Spectral")
        rescale = lambda y: ((y - np.min(y)) /(np.max(y) - np.min(y)))
        
        plt.figure(figsize =(10,10))
        x_values = self.df['Income Group']
        y_values = self.df['Life Expectancy']
        ax = plt.subplot()
        
        ax.set_xticks(range(0,len(x_values)))
        ax.set_xticklabels(x_values)
        ax.set_yticks([i*5 for i in range(17)])
        
        
        ax.set_title("Esperanza de vida por Ingresos")
        
        ax.set_xlabel('Grupo')
        ax.set_ylabel('Esperanza de vida')
        
        
        plt.legend(['Esperanza de vida'])
        plt.xticks(rotation = 90, ha='right')
        
        plt.bar(x_values, y_values, color = cmap(rescale(y_values)))
        plt.savefig(buf, format='png', transparent=True)
        #plt.show()
        plt.close()
        buf.seek(0)
        buffer = b''.join(buf)
        b2 = base64.b64encode(buffer)
        plot_url = b2.decode('utf-8')

        return plot_url
        
    def generar_grafica_reg(self):
        
        cmap = plt.get_cmap("Spectral")
        rescale = lambda y: ((y - np.min(y)) /(np.max(y) - np.min(y)))
        buf = BytesIO()

        plt.figure(figsize =(10,10))
        x_values = self.df['Region']
        y_values = self.df['Life Expectancy']
        ax = plt.subplot()
        
        ax.set_xticks(range(0,len(x_values)))
        ax.set_xticklabels(x_values)
        ax.set_yticks([i*5 for i in range(17)])
        
        ax.set_title("Esperanza de vida por Region")
        
        ax.set_xlabel('Grupo')
        ax.set_ylabel('Esperanza de vida')
        
        
        plt.legend(['Esperanza de vida'])
        plt.xticks(rotation = 90, ha='right')
        
        plt.bar(x_values, y_values, color=cmap(rescale(y_values)))
        plt.savefig(buf, format='png', transparent=True)
        #plt.show()
        plt.close()
        buf.seek(0)
        buffer = b''.join(buf)
        b2 = base64.b64encode(buffer)
        plot_url = b2.decode('utf-8')

        return plot_url

    def generar_grafica_año(self):

        buf = BytesIO()
        cmap = plt.get_cmap("Spectral")
        rescale = lambda y: ((y - np.min(y)) /(np.max(y) - np.min(y)))
        
        plt.figure(figsize =(10,10))
        x_values = self.df['Year']
        y_values = self.df['Life Expectancy']
        ax = plt.subplot()
        
        ax.set_xticks(x_values)
        ax.set_yticks([i*5 for i in range(17)])
        
        ax.set_title("Esperanza de vida por Años")
        
        ax.set_xlabel('Grupo')
        ax.set_ylabel('Esperanza de vida')
        
        
        plt.legend(['Esperanza de vida'])
        plt.xticks(rotation = 90, ha='right')
        
        plt.bar(x_values, y_values, color= cmap(rescale(y_values)))
        plt.savefig(buf, format='png', transparent=True)
        #plt.show()
        plt.close()
        buf.seek(0)
        buffer = b''.join(buf)
        b2 = base64.b64encode(buffer)
        plot_url = b2.decode('utf-8')

        return plot_url


