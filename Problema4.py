#En esta funcion se agregan los valores del coeficiente de la cuadratura de Gauss(wi) y el valor de las abscisas de la cuadratura de Gauss(z1) (DE TABLA)
def numeros(numberofpoints,listz,listw):
    while numberofpoints >= 1:
        if numberofpoints == 1:
            w = 2
            z = 0
            listz.append(z)
            listw.append(w)
            return listz, listw
        if numberofpoints == 2:
            w1 = 1
            w2 = 1
            z1 = -0.5773502692
            z2 = 0.5773502692
            listz.append(z1)
            listz.append(z2)
            listw.append(w1)
            listw.append(w2)
            return listz, listw
        elif numberofpoints == 3:
            w1 = 0.55555
            w2 = 0.88888
            w3 = 0.55555
            z1 = -0.7745966692
            z2 = 0
            z3 = 0.7745966692
            listz.append(z1)
            listz.append(z2)
            listz.append(z3)
            listw.append(w1)
            listw.append(w2)
            listw.append(w3)
            return listz, listw
        elif numberofpoints == 4:
            w1 = 0.3478548451
            w2 = 0.6521451549
            w3 = 0.6521451549
            w4 = 0.3478548451
            z1 = -0.8611363116
            z2 = -0.3399810436
            z3 = 0.3399810436
            z4 = 0.8611363116
            listz.append(z1)
            listz.append(z2)
            listz.append(z3)
            listz.append(z4)
            listw.append(w1)
            listw.append(w2)
            listw.append(w3)
            listw.append(w4)
            return listz, listw
        elif numberofpoints == 5:
            w1 = 0.2369268851
            w2 = 0.4786286705
            w3 = 0.56888
            w4 = 0.4786286705
            w5 = 0.2369268851
            z1 = -0.9061798459
            z2 = -0.5384693101
            z3 = 0
            z4 = 0.5384693101
            z5 = 0.9061798459
            listz.append(z1)
            listz.append(z2)
            listz.append(z3)
            listz.append(z4)
            listz.append(z5)
            listw.append(w1)
            listw.append(w2)
            listw.append(w3)
            listw.append(w4)
            listw.append(w5)
            return listz, listw
        elif numberofpoints == 6:
            w1 = 0.1713244924
            w2 = 0.3607615730
            w3 = 0.4679139346
            w4 = 0.4679139346
            w5 = 0.3607615730
            w6 = 0.1713244924
            z1 = -0.9324695142
            z2 = -0.6612093865
            z3 = -0.2386191861
            z4 = 0.2386191861
            z5 = 0.6612093865
            z6 = 0.9324695142
            listz.append(z1)
            listz.append(z2)
            listz.append(z3)
            listz.append(z4)
            listz.append(z5)
            listz.append(z6)
            listw.append(w1)
            listw.append(w2)
            listw.append(w3)
            listw.append(w4)
            listw.append(w5)
            listw.append(w6)
            return listz, listw

#Esta funcion lee el archivo de texto y toma las variables que definen el rango de estudio (donde empieza y termina la interconectividad)
#Permite que el codigo se aplique a cualquier malla con elementos de 4 nodos.
def general(valores):
    with open(mesh, 'r') as f:
        lineas = [linea.split() for linea in f]
    lista = []
    for i in range(len(lineas)):
        if len(lineas[i]) == 9:
            lista.append(int(lineas[i][0]))
            if len(lineas[i]) == i:
                lista.append(int(lineas[1][0]))
                break
    valores.append(lista[0])
    lista.reverse()
    valores.append(lista[0])
    
    for j in range(len(lineas)):
        if len(lineas[j]) == 9:
            if lineas[j] == valores[0]:
                valores.append(int(lineas[j][0]))
                break
    c = 0
    primer = 0
    x = str(valores[0])
    for j in range(len(lineas)):
        c += 1
        if lineas[j][0] == x:
            primer += 1
        if primer == 2:
            valores.append(c-1)
            break
    return valores

#La funcion recibe el numero del elemento de la malla y almacena una lista llamada "lineaelemento", donde almacena los 4 nodos correspondientes al elemento
def nodosdeelemento(element,lineaelemento):
    #El contador cuenta la cantidad de caracteres con espacio vacio en cada linea
    contador = 0
    nodo1 = ""
    nodo2 = ""
    nodo3 = ""
    nodo4 = ""
    q = listt[2] - listt[0]
    for caracter in lineas[q+element]:
        if caracter == " ":
            contador += 1
        #Luego de 5 caracteres en blanco, empiezan los valores utiles
        if contador == 5:
            #Se descarta el quinto caracter de espacio
            if caracter != " ":
                nodo1 += caracter
        if contador ==6 :
            if caracter != " ":
                nodo2 += caracter
        if contador == 7:
            if caracter != " ":
                nodo3 += caracter
        if contador == 8:
            if caracter != " ":
                nodo4 += caracter
    #Se agregan todos a una lista y se transforman de string a enteros
    lineaelemento.append(int(nodo1))
    lineaelemento.append(int(nodo2))
    lineaelemento.append(int(nodo3))
    lineaelemento.append(int(nodo4.rstrip('\n')))
    return lineaelemento

#Al llamar esta funcion, se guarda en 2 listas (cx,cy), las coordenadas de x e y para cada nodo de la lista de "lineaelemento"
def coordenadas(lineaelemento,cx,cy):
    #El contador cuenta el primer caracter de espacio
    coordenadax = ""
    coordenaday = ""
    contador = 0
    for j in range(1,5):
        for caracter in lineas[1 + lineaelemento[j-1]]:
            if caracter == " ":
                contador += 1
            if contador == 1:
                #descartando el primer espacio
                if caracter != " ":
                    coordenadax += caracter
            if contador == 2:
                if caracter != " ":
                    coordenaday += caracter
        #Se añaden las coordenadas a las listas cx y cy como valores flotantes            
        cx.append(float(coordenadax))
        cy.append(float(coordenaday))
        coordenadax = ""
        coordenaday = ""
        contador = 0

#Esta funcion recibe las coordenadas x,y de los 4 nodos correspondientes a un elemento determinado, tambien recibe los valores de eta, epsilon, wi,wj.
#Estos valores se evaluan y la funcion retorna el resultado de la funcion evaluada, por el jacobiano, por wi, por wj
def functionandjaco(x1,x2,x3,x4,y1,y2,y3,y4,eta,ep,wi,wj):
    #Definiendo el cambio de variable
    x = (x1)*(((1-ep)/2)*((1-eta)/2)) + (x2)*(((1+ep)/2)*((1-eta)/2)) + (x3)*(((1+ep)/2)*((1+eta)/2)) + (x4)*(((1-ep)/2)*((1+eta)/2))
    y = (y1)*(((1-ep)/2)*((1-eta)/2)) + (y2)*(((1+ep)/2)*((1-eta)/2)) + (y3)*(((1+ep)/2)*((1+eta)/2)) + (y4)*(((1-ep)/2)*((1+eta)/2))
    #Calculando las expresiones para calcular el jacobiando
    dxdep = (((1-eta)/4)*(x2-x1)+((1+eta)/4)*(x3-x4))
    dxdeta = (((1+ep)/4)*(x3-x2)+((1-ep)/4)*(x4-x1))
    dydep = (((1-eta)/4)*(y2-y1)+((1+eta)/4)*(y3-y4))
    dydeta = (((1+ep)/4)*(y3-y2)+((1-ep)/4)*(y4-y1))
    #Formula del jacobiano
    jaco = dxdep*dydeta-dydep*dxdeta
    f = 5*y*((math.sin(x))**2) + 3*(x**2)+ 5*(y**2) + 5*x*y
    return f*jaco*wi*wj

#Funcion calcula la formula de la cuadratura
def sumatoria(n,cx0,cx1,cx2,cx3,cy0,cy1,cy2,cy3,listz,listw):
    total = []
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            total.append(functionandjaco(cx0,cx1,cx2,cx3,cy0,cy1,cy2,cy3,listz[i-1],listz[i-1],listw[i-1],listw[j-1]))
            j += 1
        i += 1
    return sum(total)

#Permite calcular la integral para cada elemento del dominio de la malla
def calculoGauss(puntodegauss):
    integraciontotal = 0
    q1 = listt[0]
    q2 = listt[1] + 1
    for nod in range(q1,q2):
        listz = []
        listw = []
        #Definiendo valores de zi, wi
        numeros(puntodegauss,listz,listw)
        #Definiendo los nodos de cada elemento
        lineaelemento = []
        nodosdeelemento(nod,lineaelemento)
        #Guardando las coordenadas de cada nodo en cx,cy
        cx = []
        cy = []
        coordenadas(lineaelemento,cx,cy)
        #Sumando los resultados de la integral en cada elemento
        integraciontotal += sumatoria(puntodegauss,cx[0],cx[1],cx[2],cx[3],cy[0],cy[1],cy[2],cy[3],listz,listw)
    return integraciontotal

import math
mesh = input(("""Ingrese el nombre de la malla (con formato):

      Para tamaño de celda = 2, escriba Malla1.txt
      Para tamaño de celda = 1, escriba Malla2.txt
      Para tamaño de celda = 0.5, escriba Malla3.txt
      Para tamaño de celda = 0.1, escriba Malla4.txt
      Para mallado no uniforme, escriba Malla5.txt
      Para nueva malla ingrese el nombre completo.
      Mesh:"""))
      
#Leyendo el archivo de texto
archi1 = open(mesh,"r")
lineas = archi1.readlines()
archi1.close()
GAUSS = int(input("Ingrese los numeros de Gauss: "))
#Capturando parametros importantes de la malla
listt = []
general(listt)

print(calculoGauss(GAUSS))


