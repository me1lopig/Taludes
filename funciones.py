# funciones auxiliares 


# importacion de librerias especificas para el uso de las funciones

import matplotlib.pyplot as plt
import pandas
import numpy as np



def genera_archivo(peso_aparente,cohesion,ang_rozamiento,tiempo):
    
    # funcion para la creación de archivos de los datos del suelo
    # creamos el archivo
    texto_archivo='Calculo_'+tiempo+'.txt'
    f = open (texto_archivo,'w')
     
    # datos del terreno a enviar al archivo
    f.write('Datos del terreno \n')
    f.write('Peso específico aparente del terreno  {0} kN/m3\n'.format(peso_aparente))
    f.write('Cohesión del terreno  {0} kN/m2\n'.format(cohesion))
    f.write('Ángulo de rozamiento del terreno  {0} º\n'.format(ang_rozamiento))
    
    f.close() #cerramos el archivo


#def geometria_entrada(x,xc,numero_puntos):
#    # generación de los vectores de puntos de entrada de círculos de rotura
#    # se genera un vector de círculos de rotura hasta el punto xc del círculo
#   
#    # cálculo del número de puntos
#    numero_puntos=abs(xc-x[0])/numero_puntos 
#    # construccion del vector de puntos de entrada
#    x_entrada=np.arange(x[0],xc,numero_puntos)
#
#    return x_entrada

   


def malla(xm,ym,px,py):
    # funcion que genera la malla de centros en dos vectores
    # xc e yc son los vectores de las coordenadas de las esquinas de la malla de centros
    # px y py son el número de divisiones de la malla en cada dirección
    
    x=np.min(xm) 
    # declaracion de los vectores de salida
    xp=[]
    yp=[]

    # número de divisiones
    nx=px
    ny=py
    
    ix=(max(xm)-min(xm))/nx
    iy=(max(ym)-min(ym))/ny
    
    # calculo de los centros de la malla
    while x <= max(xm):
        y=min(ym)
        while y<=max(ym):
            xp.append(x)
            yp.append(y)
            y+=iy
        x+=ix  
    return xp,yp 
        
        
def circunferencia(xc,yc,pex,pey,x):
    # calculo de los puntos de la circunferencia
    # los datos de entrada son xc, yc y el radio
    # xc abcisa del centro
    # yc ordenada del centro
    # pex punto de entrada en x
    # pey punto de entrada en y
    # r radio del arco de circunferencia
    # x es el valor del que queremos conocer la y del arco
    # como salida nos da el valor de y correspondiente a x
    # ojo hay que controlar la salida de los límites de la geometría
    
    r=((xc-pex)**2+(yc-pey)**2)**0.5
    raiz=r**2-(x-xc)**2
    return yc-np.sqrt(raiz)
    

    
    
def geometria_talud(x_geo,x,y):
    #funcion que define la geometria del talud y/o del nivel freático en su caso
    # x_geo es la posicion de la abcisa de la que queremos conocer la ordenada
    # (x, y) son los valores de los parametros de las rectas del talud
    
    n_vector=len(x)
    if (x_geo==min(x)):
        return y[0]
        
    for i in range(n_vector+1):
        if (x[i]>=x_geo):
            y_geo=y[i]+(y[i-1]-y[i])*(x[i]-x_geo)/(x[i]-x[i-1])
            return y_geo
            break     
  

def plot_perfil(x,y,xmc,ymc,x_arco,y_arco,tiempo):
    
    #Representeamos la función utilizando el objeto plt de matplotlib
    # se puede adaptar a la entrada de títulos en x,y y general del gráfico
    # x,y es la geometría del perfil
    # xmc,ymc es la malla de centros
    
    plt.xlabel("$ x (m) $")
    plt.ylabel("$ z (m) $")
    plt.legend()
    plt.title("Perfil del talud ")
    plt.grid(True)
    plt.plot(x,y,xmc,ymc,'+',x_arco,y_arco)
    plt.axis('equal') # ejes equidistantes
    texto_archivo='Seccion_'+tiempo+'.png'
    plt.savefig(texto_archivo, bbox_inches='tight')
    plt.show()


def importexcel():
   
    # importacion de datos de hoja excel 
    # se importa del archivo geometria.xlsx'

    # importacion de datos de la geometria desde archivo xlsx excel
    datos_geometria='geometria_2.xlsx'
    df=pandas.read_excel(datos_geometria)
    n=len(df) # numero de datos de la geometria
    
    # x,y son la geometria del perfil del terreno
    # xc, yc son los puntos de la malla de centros
    # pe, peso especifico
    # c, es la cohesión
    # fi, es el peso específico
    # nx, número de divisiones del lado x de la malla de centros
    # ny, número de divisiones del lado y de la malla de centrol
    # npes, número de puntos de entrada y de salida
    # nd, número de dovelas
    # los valores con subincide se toman asi para no añadir NaN 
    
    # pasamos los valores de series a list
    x=df.x.tolist()
    y=df.y.tolist()
    xc=df.xc[0:4].tolist()    
    yc=df.yc[0:4].tolist()
    pe=df.pe[0].tolist()
    c=df.c[0].tolist()
    fi=df.fi[0].tolist()
    nx=df.nx[0].tolist()
    ny=df.ny[0].tolist()
    npes=df.npes[0].tolist()
    nd=df.nd[0].tolist()  

    # envio de los resutados
    return x,y,n,xc,yc,pe,c,fi,nx,ny,npes,nd


def correccion(cohesion,fi):
    # correccion de los valores nulos de cohesion y/o ángulo de rozamiento
    
    # correccion de la cohesión nula
    if cohesion==0:
        cohesion=0.01

    # correccion del ángulo de rozamiento nulo
    if fi==0:
        fi=0.01

    return cohesion,fi


def interseccion(xc,yc,pex,pey,x,y):
    # funcion para el calculo del punto de salida de la intersección circulo de rotura
    # x,y perfil del terreno
    # xc, yc son el centro del circulo
    # pex, pey es el punto de entrada en el perfil del terreno
    
    # cálculos intermedios 
    xf=max(x)  
    x_arco=pex

    while x_arco<=xf:
        y_perfil=geometria_talud(x_arco,x,y)
        y_arco=circunferencia(xc,yc,pex,pey,x_arco)
        
        if (y_perfil-y_arco)>=0:
            xs=x_arco          
        x_arco+=0.1 
    
    if (xs+0.1)<=xf: 
        return xs # punto de salida del círculo de rotura correcto
    
    return 0 #sale 0 en el caso de que el círculo no sea válido