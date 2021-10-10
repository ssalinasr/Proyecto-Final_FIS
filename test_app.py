import unittest
from DataManage import DataManage
from ChartManage import ChartManage
import pandas as pd
import numpy as np
import beavis
from app import app

class TestAppMethods(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_limpieza(self):
        df_expected = pd.read_excel("dataset.xlsx")
        dat = DataManage()
        df_expected = df_expected.dropna(axis=0, how='any')
        rounded = df_expected["Life Expectancy"].apply(np.ceil)
        df_expected["Life Expectancy"] = rounded

        dat.eliminar_na()
        dat.redondear_le()

        resultado = dat.obtener_dataset()
        
        beavis.assert_pd_equality(resultado, df_expected)

    def test_agrupacion_region(self):
        df_expected = pd.read_excel("dataset.xlsx")
        df_expected = df_expected.dropna(axis=0, how='any')
        rounded = df_expected["Life Expectancy"].apply(np.ceil)
        df_expected["Life Expectancy"] = rounded
        df_expected = df_expected.groupby('Region')[("Country","Country Code","Life Expectancy")].mean()
        rounded = df_expected["Life Expectancy"].apply(np.ceil)
        df_expected["Life Expectancy"] = rounded
        df_expected = df_expected.reset_index()

        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.agrupar_por_region()

        resultado = dat.obtener_dataset()
        beavis.assert_pd_equality(resultado, df_expected)

    def test_agrupacion_ingresos(self):
        df_expected = pd.read_excel("dataset.xlsx")
        df_expected = df_expected.dropna(axis=0, how='any')
        rounded = df_expected["Life Expectancy"].apply(np.ceil)
        df_expected["Life Expectancy"] = rounded
        df_expected = df_expected.groupby('Income Group')[("Country","Country Code","Life Expectancy")].mean()
        rounded = df_expected["Life Expectancy"].apply(np.ceil)
        df_expected["Life Expectancy"] = rounded
        df_expected = df_expected.reset_index()

        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.agrupar_por_ingresos()

        resultado = dat.obtener_dataset()
        beavis.assert_pd_equality(resultado, df_expected)

    def test_agrupacion_años(self):
        df_expected = pd.read_excel("dataset.xlsx")
        df_expected = df_expected.dropna(axis=0, how='any')
        rounded = df_expected["Life Expectancy"].apply(np.ceil)
        df_expected["Life Expectancy"] = rounded
        df_expected = df_expected.groupby('Year')[("Country","Country Code","Life Expectancy")].mean()
        rounded = df_expected["Life Expectancy"].apply(np.ceil)
        df_expected["Life Expectancy"] = rounded
        df_expected = df_expected.reset_index()

        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.agrupar_por_años()

        resultado = dat.obtener_dataset()
        beavis.assert_pd_equality(resultado, df_expected)

    def test_pais(self):
        df_expected = pd.read_excel("dataset.xlsx")
        df_expected = df_expected.dropna(axis=0, how='any')
        rounded = df_expected["Life Expectancy"].apply(np.ceil)
        df_expected["Life Expectancy"] = rounded
        df_expected = df_expected[["Country","Country Code","Income Group","Year","Life Expectancy"]][df_expected["Country"] == "Germany"]
        
        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.obtener_pais("Germany")

        resultado = dat.obtener_dataset()
        beavis.assert_pd_equality(resultado, df_expected)

    def test_index(self):
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(response.status_code, 200)
    
    def test_not_found(self):
        response = self.app.get('/something', follow_redirects = True)
        self.assertEqual(response.status_code, 404)

    def test_dataframe_page(self):
        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        df = dat.obtener_dataset()
        response = self.app.post('/dataframe', data = dict(tables=[df.to_html(classes='data', header="True")]))
        self.assertEqual(response.status_code , 200)

    def test_pais_page(self):
        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.filtro_años_rango(1999, 2015)
        dat.obtener_pais("Germany")
        df = dat.obtener_dataset()
        chart = ChartManage(dat)
        plot_url = chart.generar_grafica_pais("Germany")
        info_est = dat.data_estadistica_pais()
        response = self.app.post('/pais', data = dict(pais = "Germany", iniaño = "1999", finaño = "2015", tables = [df.to_html(classes='data', header="True")], plot_url = plot_url, info_est = info_est, pais_name = "Germany"))
        self.assertEqual(response.status_code, 200)

    def test_region_page(self):
        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.filtro_años_rango(1999, 2015)
        dat.agrupar_por_region()
        df = dat.obtener_dataset()
        chart = ChartManage(dat)
        plot_url = chart.generar_grafica_reg()
        info_est = dat.data_estadistica_agrupacion()
        response = self.app.post('/grafica', data = dict(iniaño = "1999", finaño = "2015", tables = [df.to_html(classes='data', header="True")], plot_url = plot_url, info_est = info_est))
        self.assertEqual(response.status_code, 200)
    
    def test_ingresos_page(self):
        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.filtro_años_rango(1999, 2015)
        dat.agrupar_por_ingresos()
        df = dat.obtener_dataset()
        chart = ChartManage(dat)
        plot_url = chart.generar_grafica_ing()
        info_est = dat.data_estadistica_agrupacion()
        response = self.app.post('/grafica', data = dict(iniaño = "1999", finaño = "2015", tables = [df.to_html(classes='data', header="True")], plot_url = plot_url, info_est = info_est))
        self.assertEqual(response.status_code, 200)
    
    def test_años_page(self):
        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.filtro_años_rango(1999, 2015)
        dat.agrupar_por_años()
        df = dat.obtener_dataset()
        chart = ChartManage(dat)
        plot_url = chart.generar_grafica_año()
        info_est = dat.data_estadistica_agrupacion()
        response = self.app.post('/grafica', data = dict(iniaño = "1999", finaño = "2015", tables = [df.to_html(classes='data', header="True")], plot_url = plot_url, info_est = info_est))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()