# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:14:10 2019


@author: German Lopez Pineda

"""


# Programa de cálculo de estabilidad de taludes
# Aplicación de los métodos de Fellenius y de Bishop
# Se usa Fellenius como valor de arranque del método de Bishop
# Desarrollado bajo Python distribución Anaconda
# Para uso académico en el caso de taludes simples
# En este caso solo para taludes secos con un solo material
# Desarrollado por Germán López Pineda
# Ingeniero de Caminos, Canales y Puertos UGR
# Master en Ingeniería del Terreno UCO
# Master en Matemática Computacional UJI
# Profesor asociado de la Universidad de Córdoba



# importación de librerias generales
import time

#importacion de librerias especificas de cálculo
import funciones

 
# traza temporal del trabajo para identificar los archivos de salida
marca_tiempo=str(time.monotonic())


# importacion de datos de la geometria y parámetros del terreno desde archivo xlsx excel
x,y,n,xm,ym,peso_aparente,cohesion,fi,nx,ny,numero_puntos,numero_dovelas=funciones.importexcel()


# correccion de la cohesión y friccion nula para evitar errores
cohesion,fi=funciones.correccion(cohesion,fi)


# generación de la malla de centros
mcx,mcy=funciones.malla(xm,ym,nx,ny)

# prueba con un círculo de rotura concreto
# calculo del punto de salida para un centro y punto de entrada determinados

# centro del arco de prueba
xc=28 # también es el límite para los puntos de entrada de los arcos de rotura
yc=18

# punto de entrada

pex=17
pey=funciones.geometria_talud(pex,x,y)
print('valor de pey es ',pey)


x_salida=funciones.interseccion(xc,yc,pex,pey,x,y)
y_salida=funciones.geometria_talud(x_salida,x,y)
print('psx {0:.2f} psy {1:.2f}'.format(x_salida,y_salida))

# generacion de los puntos del arco

# limites geometricos
x0=min(x)
xf=max(x)

y0=min(y)
yf=max(y)

# vectores de los puntos del arco
xg=[]
yg=[]

x_arco=pex

while x_arco<=xf:
    y_perfil=funciones.geometria_talud(x_arco,x,y)
    y_arco=funciones.circunferencia(xc,yc,pex,pey,x_arco)
    
    if (y_perfil-y_arco)>=0:
        xg.append(x_arco)
        yg.append(y_arco)
        xs=x_arco          
    x_arco+=0.1


# salida de resultados de los cálculos realizados
# representación gráfica del perfil del talud (poner opcional)
    

 
funciones.plot_perfil(x,y,mcx,mcy,xg,yg,marca_tiempo) 

# generacion del archivo de texto de salida de los datos iniciales
funciones.genera_archivo(peso_aparente,cohesion,fi,marca_tiempo)


## colocamos un input para que no se cierre la ventana del sistema operativo
#print("pulsa intro para terminar")
#tecla = input()# colocamos un input para que no se cierre la ventana del sistema operativo

