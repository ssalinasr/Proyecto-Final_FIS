#Proyecto Final Fundamentos Ingenieria de Software

Integrantes:

- Julian Andrés Sánchez Rivera - 20181020169
- Sebastián Salinas Rodríguez - 20181020058

-------------------------- DataSet a Utilizar ---------------------------------

	-life expentancy at birth (desde 1960 hasta 2015)
	-14728 rows, 6 cols (Country, Country Code, Region, Income Group, Year, Life expentancy[número decimal])
	
------------------------------------------------------------------------------


------------------------ Historias de Usuario --------------------------------

Metodología a utilizar: Extreme Programming (XP)

Como usuario se desea:

    1. Cargar la información alojada en el dataset
        - Dentro de la carga, se hace la filtración y limpie-
        za del dataset. (Completo)
    
    2. Realizar la visualización de los datos de acuerdo a
    las agrupaciones: región, ingresos, años. (completo)
        
    3. Obtener gráficos útiles de acuerdo a los agrupamientos como:
    
        - Mejor esperanza de vida por región/ingresos/años.
        - Peor esperanza de vida por región/ingresos/años.
        - Cambios en los valores durante el tiempo.
        - Mostrar información respecto a ese valor de esperanza.
        
    4. Consultar la información de un país en particular, reali-
    zando las mismas operaciones que para los agrupamientos. (Completo)
    
    5. Obtener  y viusalizar datos estadísticos descriptivos de la 
    información proveniente del dataset.
    
------------------------------------------------------------------------------

------------------------------- Clases definidas -----------------------------

Clase WebApp:
    *Encargada de la gestión de los procesos en entorno web, utili-
    zando Flask.
    
    Métodos:
    
    *hello(): muestra la página índice (index.html)
    *procesar_pais(): muestra la página donde se visualiza la información si se seleccionó un país 
    en específico (gráfica_país.html)
    *mostrar_df(): muestra la página donde se carga el dataframe para su visualización 
    (dataframe.html).
    *procesar(): muestra la página donde se visualiza la información de acuerdo a la agrupación
    seleccionada: región (grafica_region.html), ingresos (grafica_ingresos.html), año 
    (grafica_año.html).
    
    
Clase DataManage:
    *Obtiene el dataset, genera el dataframe, y realiza la limpieza/
    filtración de los datos.
    
    Métodos:
    
    *_init_(): carga el dataset desde el archio excel (xlsx)
    *eliminar_na(): remueve las filas con valores 'na' dentro del dataset
    *redondear_le(): redondea los valores de 'Life expectancy' dentro del dataset
    *filtro_años_max(year): filtra el dataframe desde la fecha incial (1960) hasta la fecha
    indicada por 'year'.
    *filtro_años_min(year): filtra el dataframe desde la fecha inicial indicada por 'year'
    hasta la fecha final máxima (2015).
    *filtro_años_rango(year_min, year_max): filtra el dataframe desde la fecha incial indicada
    por year_min hasta 	la fecha máxima indicada por 'year_max'.
    *agrupar_por_region(): realiza la agrupación de los datos según su región, con la función
    groupby del dataframe.
    *agrupar_por_ingresos(): realiza la agrupación de los datos según sus ingresos, con la función
    groupby del dataframe. 
    *agrupar_por_años(): realiza la agrupación de los datos según los años, con la función
    groupby del dataframe.
    *obtener_pais(country): obtiene las filas del dataframe, donde 'Country' es igual al país 
    seleccionado por la variable 'country'.
    *obtener_dataset(): obtiene el dataframe actual.
    *data_estadistica_pais(): obtiene la información estadística del dataframe creado si se 
    seleccionó un país.
    *data_estadistica_agrupacion(): obtiene la información estadística del dataframe creado si se 
    seleccionó una agrupación (región, ingresos, años).
    
Clase ChartManage:
    *Realiza la ejecución de los métodos encargados de generar las
    gráficas.
    
    Metodos:
    
    *_init_(data): Obtiene y carga el dataframe creado.
    *generar_grafica_pais(country): genera el grafico de barras para la selección
    por país específico. country = pais seleccionado.
    *generar_grafica_ing(): genera el grafico de barras para la selección
    por ingresos económicos.
    *generar_grafica_reg(): genera el grafico de barras para la selección
    por región.
    *generar_grafica_año(): genera el grafico de barras para la selección
    por un rango de años específico.
    *Cada método retorna la url de la imagen asociada a la gráfica en formato
    png.
   
  -----------------------------------------------------------------------------    

------------------------------- Librerías y recursos --------------------------

	*Numpy
	*matplotlib
	*pandas
	*flask

	*Para la ejecución de la aplicación, se requiere de la creación de un entorno virtual
	'venv', cuya instalación para vscode se encuentra aqui:
	https://code.visualstudio.com/docs/python/tutorial-flask

	*Dentro del entorno virtual, es necesario hacer instalación de las librerías mencionadas
	al inicio. Dicha instalación se realiza con el comando:

	python -m pip install <libreria>

	*ejecución de flask:
	python -m flask run
 
 
  ----------------------------------------------------------------------------- 

*El propósito de esta aplicación es netamente educativo.
