# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:12:40 2019

@author: German
"""


# funciones de gestion de entrada de datos visuales
# datos fisicos del terreno
# geometria del terreno
# control del calculo

from tkinter import *

       
def datos_fisicos():
  # entrada de datos fisicos del terreno del talud  

    def quit():
        # cerramos la ventana
        ventana.destroy()
       
    
    # características de la ventana
    ventana=Tk()
    ventana.title('Parámetros físicos del terreno') # título
    ventana.resizable(width=False, height=False) # fijamos dimensiones
    
    # declaracion de variables de entrada
    peso_especifico = StringVar()
    cohesion = StringVar()
    rozamiento = StringVar()
    
    # etiquetas
    Label(ventana, text="Peso específico [kN/m3]").grid(pady=5, row=0, column=0)
    Label(ventana, text="Cohesión [kN/m2]").grid( pady=5, row=1, column=0)
    Label(ventana, text="Ángulo de rozamiento [º]").grid( pady=5, row=2, column=0)
    
    # cuadros de entrada
    Entry(ventana, width=10,textvariable=peso_especifico,justify=LEFT).grid(padx=5, row=0, column=1)
    Entry(ventana, width=10,textvariable=cohesion,justify=LEFT).grid(padx=5, row=1, column=1)
    Entry(ventana, width=10,textvariable=rozamiento,justify=LEFT).grid(padx=5, row=2, column=1)
    
    
    
    
    # botón de salida
    Button(ventana, text="Salir", width=50, command=quit).grid(padx=20, pady=20, row=3, column=0, columnspan=2)
    
    
    # bucle de mantemiento de la ventana activa
    ventana.mainloop()
    
    
    
def malla_centros():
  # coodenadas de los puntos de la malla 

    def quit():
        # cerramos la ventana
        ventana.destroy()
       
    
    # características de la ventana
    ventana=Tk()
    ventana.title('Puntos de la malla de centros') # título
    ventana.resizable(width=False, height=False) # fijamos dimensiones
    
    # esquina inferior izquierda
    x1 = StringVar()
    y1 = StringVar()
    
    # esquina inferior derecha
    x2 = StringVar()
    y2 = StringVar()
    
    # esquina superior izquierda
    x3 = StringVar()
    y3 = StringVar()
    
    # esquina suoerior derecha
    x4 = StringVar()
    y4 = StringVar()
    
    
    # etiquetas
    Label(ventana, text="x1").grid(pady=5, row=0, column=0)
    Label(ventana, text="y1").grid(pady=5, row=1, column=0)
    Label(ventana, text="x2").grid(pady=5, row=2, column=0)
    Label(ventana, text="y2").grid(pady=5, row=3, column=0)
    Label(ventana, text="x3").grid(pady=5, row=4, column=0)
    Label(ventana, text="y3").grid(pady=5, row=5, column=0)
    Label(ventana, text="x4").grid(pady=5, row=6, column=0)
    Label(ventana, text="y4").grid(pady=5, row=7, column=0)

    
    # cuadros de entrada
    Entry(ventana, width=10,textvariable=x1,justify=LEFT).grid(padx=5, row=0, column=1)
    Entry(ventana, width=10,textvariable=y1,justify=LEFT).grid(padx=5, row=1, column=1)
    Entry(ventana, width=10,textvariable=x2,justify=LEFT).grid(padx=5, row=2, column=1)
    Entry(ventana, width=10,textvariable=y2,justify=LEFT).grid(padx=5, row=3, column=1)
    Entry(ventana, width=10,textvariable=x3,justify=LEFT).grid(padx=5, row=4, column=1)
    Entry(ventana, width=10,textvariable=y3,justify=LEFT).grid(padx=5, row=5, column=1)
    Entry(ventana, width=10,textvariable=x4,justify=LEFT).grid(padx=5, row=6, column=1)
    Entry(ventana, width=10,textvariable=y4,justify=LEFT).grid(padx=5, row=7, column=1)
      
    
    
    # botón de salida
    Button(ventana, text="Salir", width=50, command=quit).grid(padx=20, pady=20, row=8, column=0, columnspan=2)
    
    
    # bucle de mantemiento de la ventana activa
    ventana.mainloop()