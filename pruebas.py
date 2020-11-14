# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:14:10 2019

@author: German
"""
#import pandas
import numpy as np
import funciones
import matplotlib.pyplot as plt



# importacion de datos de la geometria y parámetros del terreno desde archivo xlsx excel
x,y,n,xm,ym,peso_aparente,cohesion,fi,nx,ny,numero_puntos,numero_dovelas=funciones.importexcel()





# bordes de la geometría del talud
x0=np.min(x) # valores de x de la geometrís del talud
xf=np.max(x)

y0=np.min(y) # valores de y de la geometría del talud
yf=np.max(y)

# limites de la malla

x_malla_max=np.min(xm) # valor de x minimo de la malla de centros
x_malla_min=np.max(xm) # valor de x máximo de la malla de centros

y_malla_max=np.min(ym) # valor de y minimo de la malla de centros
y_malla_min=np.max(ym) # valor de y maximo de la malla de centros


# vectores de la malla de centros
px=10 # numero de divisiones de la malla de centros
py=10
xmalla,ymalla=funciones.malla(xm,ym,px,px)

# se toma un solo punto de la malla de centros de prueba

xc=28 # también es el límite para los puntos de entrada de los arcos de rotura
yc=18
pex=x0

while pex<=xc:

    # pruebas con la función circunferencia
    # datos de entrada
    pey=funciones.geometria_talud(pex,x,y)
    
    # cálculos intermedios
    #r=((xc-pex)**2+(pey-yc)**2)**0.5
    xg=[]
    yg=[]
    
    xp=[]
    yp=[]
    
    x_arco=pex
    
    while (x_arco not in x[1:len(x)-1]) and (x_arco<=xf):
        y_perfil=funciones.geometria_talud(x_arco,x,y)
        y_arco=funciones.circunferencia(xc,yc,pex,pey,x_arco)
        
        if (y_perfil-y_arco)>=0:
            xg.append(x_arco)
            yg.append(y_arco)
            
            xp.append(x_arco)
            yp.append(y_perfil)  
            xs=x_arco          
        x_arco+=0.1
    #    print(x_arco)
    
    
    
    if (xs+0.1)<=xf:
        plt.xlabel("$ x (m) $")
        plt.ylabel("$ z (m) $")
        plt.legend()
        plt.title("Perfil del talud ")
        plt.grid(True)
        plt.plot(xg,yg,xp,yp)
        plt.axis('equal') # ejes equidistantes
        plt.show()

    pex+=0.10 # incremento de pex

#
#for a in range(0,len(xmalla)):
#    print('x_malla {0:.2f} y_malla {1:.2f}'.format(xmalla[a],ymalla[a]))



     
#            punto_salida=funciones.interseccion(xc,yc,pex,pey,x,y)
#            if punto_salida!=0:
#                print('pe {0:.2f} x_c {1:.2f} y_c {2:.2f} ps {3:.2f}'.format(pex,xc,yc,punto_salida))
#
#x_puntos=funciones.geometria_entrada(x,25,20)
#print(x_puntos,len(x_puntos))

    


## colocamos un input para que no se cierre la ventana del sistema operativo
#print("pulsa intro para terminar")
#tecla = input()# colocamos un input para que no se cierre la ventana del sistema operativo