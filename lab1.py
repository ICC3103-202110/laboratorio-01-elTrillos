
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
    listatemp3 = []
    daBoard = []
    daBoard2 =[]
    daBoard3 =[]
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
    #print(listaOG)
    random.shuffle(listaOG)
    print(listaOG)
    while n1 < alto:
        while n2 < ancho:
            if listaOG[0] < 10:
                listatemp.append("0"+str(listaOG[0]))
                listatemp2.append("▓▓")
                listatemp3.append("▓▓")
            else:
                listatemp.append(str(listaOG[0]))
                listatemp2.append("▓▓")
                listatemp3.append("▓▓")
            listaOG.pop(0)
            n2 += 1
        daBoard.append(listatemp)
        daBoard2.append(listatemp2)
        daBoard3.append(listatemp3)
        listatemp = []
        listatemp2 = []
        listatemp3 = []
        n2 = 0
        n1 += 1
    #print(daBoard)
    print(daBoard2)
    return daBoard,daBoard2,ancho,alto,daBoard3

def gameui(boardimg):
    for i in boardimg:
        for j in i:
            print(f"{j:>3}",end=(' '))
        print()   

def gameplay():
    curpart = 1
    numss = ["",""]
    score1 = 0
    score2 = 0
    curplaya = 1
    tempBoard = []
    playing = True
    ans = []
    ans1 = []
    ans2 = []
    print("===============================")
    print("  Bienvenido a memorice v1.0   ")
    print("===============================")
    sizee = startui()
    print(sizee)
    daboi,daboi2,ancho,alto,tempBoard = cardgen(sizee)
    qnparte = random.randint(1,2)
    curplaya = qnparte
    print("comienza el jugador", curplaya)
    while playing == True:
        asking = True
        #print("a")
        while asking == True:
            gameui(tempBoard)
            print("Jugador", curplaya , "escoja la coordenada de la carta (x y) numero", curpart)
            ans = input().split(" ")
            if ans[0].isnumeric() and ans[1].isnumeric() == True:
                ans[0] = int(ans[0])
                ans[1] = int(ans[1])
                if curpart == 1:
                    ans1 = list(ans)
                else:
                    ans2 = list(ans)
                if 0 < ans[0] <= ancho and 0 < ans[1] <= alto:
                    #print("ok")
                    #print(tempBoard)
                    #print(daboi2)
                    #print(daboi)
                    #print("")


                    #print(tempBoard)
                    #print(daboi2)
                    #print(daboi)
                    #print("")
                    tempBoard[ans[1]-1][ans[0]-1] = daboi[ans[1]-1][ans[0]-1]
                    #print(tempBoard)
                    #print(daboi2)
                    #print(daboi)
                    gameui(tempBoard)
                    numss[curpart-1] = daboi[ans[1]-1][ans[0]-1]
                    if curpart == 1:
                        curpart = 2
                        print(numss)
                        
                        asking = True
                    else:
                        if ans1 == ans2:
                            print("escribe 2 coordenadas DISTINTAS")
                            curpart = 1
                            numss = ["",""]
                            tempBoard = list(daboi2)
                            print(daboi2)
                            asking = True
                        else:
                            curpart = 1
                            asking = False
                    
                else: 
                    print("error, escribir valores dentro del tamaño de la tabla de juego")
            else:
                print("error, seguir el formato por favor")
        if numss[0] == numss[1]:
            print("jugador" ,curplaya, "acerto!")
            if curplaya == 1:
                curplaya = 2
                score1 +=1
            else:
                curplaya = 1
                score2 +=1
            print(ans1)
            print(ans2)
            tempBoard[ans1[1]-1][ans1[0]-1] = "  "
            tempBoard[ans2[1]-1][ans2[0]-1] = "  "
            daboi2[ans1[1]-1][ans1[0]-1] = "  "
            daboi2[ans2[1]-1][ans2[0]-1] = "  "
            
        else:
            print("jugador" ,curplaya ,"no acerto!")

            if curplaya == 1:
                curplaya = 2
            else:
                curplaya = 1
            tempBoard = []
            for x in daboi2:
                tempBoard.append(list(x))
            #tempBoard = list(daboi2)
            #print("dou")
        print("Jugador 1:",score1 ,"/ Jugador 2:", score2)
        if score1 + score2 == sizee:
            if score1 > score2:
                print("El jugador 1 ha ganado!" )
            elif score2 > score1:
                print("El jugador 2 ha ganado!" )
            else:
                print("Empate!")
            playing = False
        playing = True

    
gameplay()