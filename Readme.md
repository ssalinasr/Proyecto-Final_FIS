-------------------------- DataSet a Utilizar ---------------------------------

	-life expentancy at birth (desde 1960 hasta 2015)
	-14728 rows, 6 cols (Country, Country Code, Region, Income Group, Year, Life expentancy[número decimal])
	
------------------------------------------------------------------------------


------------------------ Historias de Usuario --------------------------------

Metodología a utilizar: Extreme Programming (XP)

Como usuario se desea:

    1. Cargar la información alojada en el dataset
        - Dentro de la carga, se hace la filtración y limpie-
        za del dataset.
    
    2. Realizar la visualización de los datos de acuerdo a
    las agrupaciones: región, ingresos, años.
        
    3. Obtener gráficos útiles de acuerdo a los agrupamientos como:
    
        - Mejor esperanza de vida por región/ingresos/años.
        - Peor esperanza de vida por región/ingresos/años.
        - Cambios en los valores durante el tiempo.
        - Mostrar información respecto a ese valor de esperanza.
        
    4. Consultar la información de un país en particular, reali-
    zando las mismas operaciones que para los agrupamientos.
    
    5. Obtener  y viusalizar datos estadísticos descriptivos de la 
    información proveniente del dataset.
    
------------------------------------------------------------------------------

------------------------------- Clases definidas -----------------------------

Clase WebApp:
    *Encargada de la gestión de los procesos en entorno web, utili-
    zando Flask.
    
Clase DataManage:
    *Obtiene el dataset, genera el dataframe, y realiza la limpieza/
    filtración de los datos.
    
Clase ChartManage:
    *Realiza la ejecución de los métodos encargados de generar las
    gráficas.
    
  -----------------------------------------------------------------------------    

