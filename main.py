import os
os.system('cls')
import matplotlib.pyplot as plt
from decimal import *
getcontext().prec = 999999999999999999
import time

import colorama
from colorama import Fore, Back
colorama.init()


def nachkommastellen(zahl):
    
    zahl = str(zahl)
    zahl_list = list(zahl)
    kommaIndex = zahl_list.index('.')
    kommaStelle = kommaIndex+1
    nachkommastellen = len(zahl)-kommaStelle
    
    return nachkommastellen



def nat_quadratzahlen_generieren(num,quadcub):
    nat_quadratzahlen = []
    nat_wurzeln_aus_quadratzahlen = []
    for i in range(num):
        i+=1
        nat_quadratzahlen.append(i**quadcub)
        nat_wurzeln_aus_quadratzahlen.append(i)
    return nat_quadratzahlen,nat_wurzeln_aus_quadratzahlen

def mittelwert_bestimmen(a,b):
    return Decimal((a+b)/2)

def end():
    input()
    exit()

temp1 = input(Fore.CYAN + 'Quadratzahlen Listengröße: ')
quadcub = int(input(Fore.CYAN + 'Wurzelexponent: '))
nat_quadratzahlen, nat_wurzeln_aus_quadratzahlen = nat_quadratzahlen_generieren(int(temp1),quadcub) 


def quadratwurzel_bestimmen(zahl,annäherungen,delay,JakobModus):

    time1 = float(time.perf_counter()) #


    xAchse = []
    yAchse = []

    if zahl in nat_quadratzahlen:
        print(Fore.GREEN + 'Die Wurzel aus ',zahl,' ist ',nat_wurzeln_aus_quadratzahlen[nat_quadratzahlen.index(zahl)],'.', sep='')   #Fore.Green
        end()

    if JakobModus:
        print(Back.BLACK)
        print(Back.GREEN + 'Natürliche Zahlen:',nat_quadratzahlen)
        print(Back.BLACK)
        print(Back.GREEN + 'Wurzeln aus den natürlichen Zahlen:',nat_wurzeln_aus_quadratzahlen)            ###
        print(Back.BLACK)


    nat_quadratzahlen.append(zahl)
    nat_quadratzahlen.sort()


    obergrenze = nat_quadratzahlen[nat_quadratzahlen.index(zahl)+1]
    print(Fore.CYAN + 'Obergrenze^Wurzelexponent:',obergrenze)
    untergrenze = nat_quadratzahlen[nat_quadratzahlen.index(zahl)-1]
    print(Fore.CYAN + 'Untergrenze^Wurzelexponent:',untergrenze)

    nat_quadratzahlen.remove(zahl)

    obergrenze = nat_wurzeln_aus_quadratzahlen[nat_quadratzahlen.index(obergrenze)]
    print(Fore.CYAN + 'Obergrenze:',obergrenze)
    untergrenze = nat_wurzeln_aus_quadratzahlen[nat_quadratzahlen.index(untergrenze)]
    print(Fore.CYAN + 'Untergrenze:',untergrenze)

    mittelwert = 0
    color = 1
    for i in range(annäherungen):
        alter_mittelwert = mittelwert
        mittelwert = Decimal(mittelwert_bestimmen(untergrenze,obergrenze))

        if mittelwert**quadcub < zahl:
            untergrenze = mittelwert
        if mittelwert**quadcub > zahl:
            obergrenze = mittelwert


        time.sleep(delay)

        if color == 1:
            print(Fore.WHITE + str(mittelwert))
            color = 2
        elif color == 2:
            print(Fore.YELLOW + str(mittelwert))
            color = 1

        xAchse.append(i+1)
        yAchse.append(mittelwert)

        if alter_mittelwert == mittelwert:
            time2 = time.perf_counter()
            break
    

    time2 = float(time.perf_counter())

        
    print()
    print(Fore.GREEN + 'Abgeschlossen in',i+1,'Annäherungen!') #Fore.Green
    try:
        print(Fore.GREEN + 'Abgeschlossen in',float(time2-time1),'Sekunden!') #Fore.Green
    except:
        print(Fore.GREEN + 'Abgeschlossen in '+ Fore.RED +' Fehler '+ Fore.GREEN +'Sekunden!')
    
    try:
        print(Fore.GREEN + 'Die durchschnittliche Rechenzeit für jede Annäherung beträgt',float((time2-time1)/(i+1)),'Sekunden!')
    except:
        print(Fore.GREEN + 'Die durchschnittliche Rechenzeit für jede Annäherung beträgt '+Fore.RED+' Fehler'+Fore.GREEN+' Sekunden!')

    print(Fore.GREEN + 'Das Ergebnis der letzten Annäherung hat',nachkommastellen(mittelwert),'Nachkommastellen!')



    plt.plot(xAchse, yAchse, color='green', linestyle='dashed', linewidth = 1,
         marker='.', markerfacecolor='blue', markersize=8)

    plt.xlabel('Annäherungen')
    plt.ylabel('Ergebnis')
    title = f'Intervallhalbierungsverfahren zur {quadcub}. Wurzel aus ' + str(zahl)
    plt.title(title)

    print(Fore.GREEN + 'Enter drücken um Graphen anzuzeigen...')
    input()
    plt.show()

    end()
        
        


def menu():
    zahl = input(Fore.CYAN + 'Radikand: ')
    annäherungen = input(Fore.CYAN + 'Wie viele Annäherungen: ')
    delay = input(Fore.CYAN + 'Delay: ')
    JakobModus = input(Fore.CYAN + 'Jakob Modus? (Y/N): ')
    if JakobModus.lower() == 'y':
        JakobModus = True
    elif JakobModus.lower() == 'n':
        JakobModus = False
    else:
        print(Fore.RED + 'Syntax Fehler. Jakob Modus wird auf False gesetzt.')

    
    zahl = Decimal(zahl)         
    annäherungen = int(annäherungen)
    delay = float(delay)

    #quadratwurzel_bestimmen_jit = jit(nopython=True)(quadratwurzel_bestimmen)
    #quadratwurzel_bestimmen_jit(zahl,annäherungen,delay)
    quadratwurzel_bestimmen(zahl,annäherungen,delay,JakobModus)









if __name__ == '__main__':
    menu()