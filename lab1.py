
import numpy as np
import random
from functools import reduce

def startui():
    print(" ")
    asking = 1
    while asking == 1:

        ans = input("Insert how many pairs of cards you want: ")
        if ans.isnumeric() == True:
            print("ok")
            asking = 0
            ans = int(ans)
            return ans
        else:
            print("error, please write a full value")

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
    aa = (reduce(list.__add__, ([i, numero//i] for i in range(1, int(numero**0.5) + 1) if numero % i == 0))) 
    #lo obtuve de stackoverflow
    alto = aa[-1]
    
    ancho = aa[-2]
    print(alto,ancho)
    while k1 <= size:
        listaOG.append(k1)
        listaOG.append(k1)
        k1 +=1
    #print(listaOG)
    random.shuffle(listaOG)
    #print(listaOG)
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
    #print(daBoard2)
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
    print("================================")
    print("    Welcome to memorice v1.0    ")
    print("                                ")
    print("   Copyright TrillosSoft 2021   ")
    print("================================")
    sizee = startui()
    #print(sizee)
    daboi,daboi2,ancho,alto,tempBoard = cardgen(sizee)
    qnparte = 1
    curplaya = qnparte
    print("Player", curplaya, "starts")
    gameui(tempBoard)
    while playing == True:
        asking = True
        #print("a")
        #gameui(tempBoard)
        while asking == True:
            #gameui(tempBoard)
            print("Player 1", curplaya , "choose the card (x y) number", curpart)
            ans = input().split(" ")
            if ans[0].isnumeric() and ans[1].isnumeric() == True:
                ans[0] = int(ans[0])
                ans[1] = int(ans[1])
                if curpart == 1:
                    ans1 = list(ans)
                else:
                    ans2 = list(ans)
                if 0 < ans[0] <= ancho and 0 < ans[1] <= alto:
                    if daboi2[ans[1]-1][ans[0]-1] != "  ":
                        tempBoard[ans[1]-1][ans[0]-1] = daboi[ans[1]-1][ans[0]-1]
                        print(" ")
                        gameui(tempBoard)
                        print(" ")
                        numss[curpart-1] = daboi[ans[1]-1][ans[0]-1]
                        if curpart == 1:
                            curpart = 2
                            #print(numss)
                            
                            asking = True
                        else:
                            if ans1 == ans2:
                                print("please write 2 DIFFERENT coordinates")
                                curpart = 1
                                numss = ["",""]
                                #tempBoard = list(daboi2)
                                for x in daboi2:
                                    tempBoard.append(list(x))
                                #print(daboi2)
                                asking = True
                            else:
                                curpart = 1
                                gameui(tempBoard)
                                asking = False
                    else:
                        print("error, write coordinates not previously discovered")
                    
                else: 
                    print("error, please insert values inside the limits")
            else:
                print("error, follow the format please")
        if numss[0] == numss[1]:
            #gameui(tempBoard)
            print("Player" ,curplaya, "found a pair!")
            
            if curplaya == 1:
                curplaya = 2
                score1 +=1
            else:
                curplaya = 1
                score2 +=1
            #print(ans1)
            #print(ans2)
            tempBoard[ans1[1]-1][ans1[0]-1] = "  "
            tempBoard[ans2[1]-1][ans2[0]-1] = "  "
            daboi2[ans1[1]-1][ans1[0]-1] = "  "
            daboi2[ans2[1]-1][ans2[0]-1] = "  "
            
        else:
            #gameui(tempBoard)
            print("Player" ,curplaya ,"didn´t find a pair!")

            if curplaya == 1:
                curplaya = 2
            else:
                curplaya = 1
            tempBoard = []
            for x in daboi2:
                tempBoard.append(list(x))
            #tempBoard = list(daboi2)
            #print("dou")
        print("Player 2:",score1 ,"/ Player 2:", score2)
        if score1 + score2 == sizee:
            if score1 > score2:
                print("Player 1 won!" )
                break
            elif score2 > score1:
                print("Player 2 won!" )
                break
            else:
                print("Tie!")
                break
            playing = False
        playing = True

    
gameplay()