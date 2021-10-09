from flask import Flask, render_template, request, flash
from DataManage import DataManage
from ChartManage import ChartManage

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/dataframe', methods=['POST','GET'])
def mostrar_df():
    dat = DataManage()
    dat.eliminar_na()
    dat.redondear_le()
    df = dat.obtener_dataset()
    return render_template('dataframe.html', tables=[df.to_html(classes='data', header="True")])

@app.route('/pais', methods=['POST','GET'])
def procesar_pais():
    pais = request.form.get("pais")
    a_inicio = int(request.form.get("iniaño"))
    a_final = int(request.form.get("finaño"))

    if pais != "":       
        dat = DataManage()
        dat.eliminar_na()
        dat.redondear_le()
        dat.filtro_años_rango(a_inicio, a_final)
        dat.obtener_pais(pais)
        df = dat.obtener_dataset()
        chart = ChartManage(dat)
        plot_url = chart.generar_grafica_pais(pais)
        info_est = dat.data_estadistica_pais()
        #print(info_est)
        return render_template('grafica_pais.html', tables=[df.to_html(classes='data', header="True")], plot_url = plot_url, info_est = info_est, pais_name = pais)
    else:
        flash('Valor inválido en el campo país')
        return render_template('index.html')

@app.route('/grafica', methods=['POST', 'GET'])
def procesar():
    valor = request.form.get("agrupar")
    a_inicio = int(request.form.get("iniaño"))
    a_final = int(request.form.get("finaño"))

    dat = DataManage()
    dat.eliminar_na()
    dat.redondear_le()
    dat.filtro_años_rango(a_inicio, a_final)

    if valor == "region":
        dat.agrupar_por_region()
        df = dat.obtener_dataset()
        chart = ChartManage(dat)
        plot_url = chart.generar_grafica_reg()
        info_est = dat.data_estadistica_agrupacion()
        return render_template('grafica_region.html', tables=[df.to_html(classes='data', header="True")], plot_url = plot_url, info_est = info_est)
    elif valor == "ingresos":
        dat.agrupar_por_ingresos()
        df = dat.obtener_dataset()
        chart = ChartManage(dat)
        plot_url = chart.generar_grafica_ing()
        info_est = dat.data_estadistica_agrupacion()
        return render_template('grafica_ingresos.html', tables=[df.to_html(classes='data', header="True")], plot_url = plot_url, info_est = info_est)
    elif valor == "años":
        dat.agrupar_por_años()
        df = dat.obtener_dataset()
        chart = ChartManage(dat)
        plot_url = chart.generar_grafica_año()
        info_est = dat.data_estadistica_agrupacion()
        return render_template('grafica_años.html', tables=[df.to_html(classes='data', header="True")], plot_url = plot_url, info_est = info_est)
    else:
        return render_template('index.html')
    









