# Proyecto Final
## Mediante metodologia XP
<hr>

## Fundamentos de Ingenieria de Software  
## Ingenieria de Sistemas 2021-1.
### Proyecto del curso.

* _Julian Andres Sanchez Rivera - 20181020169_
* _Sebastian Salinas Rodriguez - 20181020058_

## --------------------  Descripcion  -------------------

El presente repositorio, contiene el documentado de los procesos llevados a cabo para el desarrollo de un 
entorno web y el uso de un compilado de datos, generando una interpretacion grafica, aparte de las visualizacion
interactiva de los datos por medio de graficas, se busca aplicar cierta metodologia para el desarrollo de dicho
entorno, especificamente hablamos de una de las metodologias agiles mas utilizadas como lo es la programacion 
extrema ideal para proyectos con tiempos tan cortos como este.

<hr>

## DataSet a utiizar

* Life expentancy at birth (desde 1960 hasta 2015)
  14728 rows, 6 cols (Country, Country Code, Region, Income Group, Year, Life expentancy[número decimal])	  
  _Obtenido de_: https://www.kaggle.com/shitalgaikwad123/life-expectancy-at-birth-for-different-countries 
	
<hr>

## ---------------------- Analisis --------------------------

**_Metodología a utilizar: Extreme Programming (XP)_**

## Historias de usuario

Como usuario se desea:

    1. Cargar la información alojada en el dataset
        * Dentro de la carga, se hace la filtración y limpieza del dataset.
    
    2. Realizar la visualización de los datos de acuerdo a
    las agrupaciones: región, ingresos, años.
        
    3. Obtener gráficos útiles de acuerdo a los agrupamientos como:
    
        * Mejor esperanza de vida por región/ingresos/años.
        * Peor esperanza de vida por región/ingresos/años.
        * Cambios en los valores durante el tiempo.
        * Mostrar información respecto a ese valor de esperanza.
        
    4. Consultar la información de un país en particular, realizando las mismas operaciones que para
    los agrupamientos.
    
    5. Obtener  y viusalizar datos estadísticos descriptivos de la 
    información proveniente del dataset.
    
<hr>

## -------------------- Clases definidas --------------------

Clase WebApp:

    * Encargada de la gestión de los procesos en entorno web, utilizando Flask.
    
Clase DataManage:

    * Obtiene el dataset, genera el dataframe, y realiza la limpieza/ filtración de los datos.
    
Clase ChartManage:

    * Realiza la ejecución de los métodos encargados de generar las gráficas.
  
 <hr> 
  ----------------------------------------------------------
  
## Dependencias

* <code> Pandas </code>
* <code> Matplotlib </code>
* <code> Flask </code>

_El objetivo de este proyecto es netamente educativo_
