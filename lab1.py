
import numpy as np
import random
from functools import reduce

def startui():
    print("wilcom to da game")
    asking = 1
    while asking == 1:

        ans = input("cuantos pares")
        if ans.isnumeric() == True:
            print("ok")
            asking = 0
            ans = int(ans)
            return ans
        else:
            print("error, escribir un valor entero porfavor")

def cardgen(size):           
    numero = size*2
    listaOG = []
    listatemp = []
    listatemp2 = []
    daBoard = []
    daBoard2 =[]
    k1 = 1
    n1 = 0
    n2 = 0
    aa = (reduce(list.__add__, ([i, numero//i] for i in range(1, int(numero**0.5) + 1) if numero % i == 0))) #lo obtuve de stackoverflow
    alto = aa[-1]
    
    ancho = aa[-2]
    print(alto,ancho)
    while k1 <= size:
        listaOG.append(k1)
        listaOG.append(k1)
        k1 +=1
    print(listaOG)
    random.shuffle(listaOG)
    print(listaOG)
    while n1 < alto:
        while n2 < ancho:
            if listaOG[0] < 10:
                listatemp.append("0"+str(listaOG[0]))
                listatemp2.append("▓▓")
            else:
                listatemp.append(str(listaOG[0]))
                listatemp2.append("▓▓")
            listaOG.pop(0)
            n2 += 1
        daBoard.append(listatemp)
        daBoard2.append(listatemp2)
        listatemp = []
        listatemp2 = []
        n2 = 0
        n1 += 1
    print(daBoard)
    print(daBoard2)
    return daBoard,daBoard2,ancho,alto

def gameui(boardrial,boardimg):
    for i in boardimg:
        for j in i:
            print(f"{j:>3}",end=(' '))
        print()   

def gameplay():
    curpart = 1
    numss = []
    score1 = 0
    score2 = 0
    curplaya = 1
    tempBoard = []
    playing = True
    ans = []
    print("===============================")
    print("  Bienvenido a memorice v1.0   ")
    print("===============================")
    sizee = startui()
    print(sizee)
    daboi,daboi2,ancho,alto = cardgen(sizee)
    gameui(daboi,daboi2)
    qnparte = random.randint(1,2)
    curplaya = qnparte
    print("comienza el jugador", curplaya)
    while playing == True:
        asking = True
        while asking == True:
            print("Jugador", curplaya , "escoja la coordenada de la carta (x y) numero", curpart)
            ans = input().split(" ")
            if ans[0].isnumeric() and ans[1].isnumeric() == True:
                ans[0] = int(ans[0])
                ans[1] = int(ans[1])
                if ans[0] <= ancho and ans[1] <= alto:
                    print("ok")
                    
                    tempBoard = list(daboi2)
                    tempBoard[ans[1]-1][ans[0]-1] = daboi[ans[1]-1][ans[0]-1]
                    gameui(daboi,tempBoard)
                    numss[curpart-1] = daboi[ans[1]-1][ans[0]-1]
                    if curpart == 1:
                        curpart = 2
                    else:
                        asking = False
                    return ans
                else: 
                    print("error, escribir valores dentro del tamaño de la tabla de juego")
            else:
                print("error, seguir el formato por favor")
        if curpart[0] == curpart[1]:
            print("oke")
        else:
            print("dou")
        playing = False

        

gameplay()