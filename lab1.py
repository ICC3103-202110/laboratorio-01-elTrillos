
import numpy as np


def startui():
    print("wilcom to da game")
    asking = 1
    while asking == 1:

        ans = input("cuantos pares")
        if ans.isnumeric() == True:
            print("ok")
            asking = 0
            ans = int(ans)
            
        else:
            print("error, escribir un valor entero porfavor")

def cardgen(size):           
    return 0
def gameui(size, cards):
    return 0

startui()
