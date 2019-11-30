# -*- coding: utf-8 -*-
from funtions4 import *
from connecta4 import *
import string

def menu1(np,a,f):
    """
    Mostra per pantalla menu i retorna opcio desitjada
    """
    N = np
    A = a
    F = f
    print ""
    print "CONNECT4 GAME"
    print ""
    print "1. NEW GAME"
    print "2. GAME SETTINGS"
    print "0. Exit"
    print ""
    c=raw_input("Enter option: ")
    while c!="2" and c!="1" and c!="0":
        print "[  X  ] Invalid option."
        c=raw_input("Enter option: ")
    return c

def menu2(np,a,f):
    """
    Mostra per pantalla menu i retorna opcio desitjada
    """
    N = np
    A = a
    F = f
    print "------------------------------------------------------------"
    print "GAME SETTINGS"
    print ""
    print "1. NUMBER OF PLAYERS (NOW PLAYING",N,"PLAYERS)"
    print "2. HOW MANY ROWS DO YOU WANT? (NOW",F,"ROWS)"
    print "3. HOW MANY COLUMNS DO YOU WANT? (NOW",A,"COLUMNS)"
    print "0. GO BACK"
    print ""
    c=raw_input("Enter option: ")
    while c!="3" and c!="2" and c!="1" and c!="0":
        print "[  X  ] Invalid option."
        c=raw_input("Enter option: ")

    if c == "1":
        statusnum=False
        t = False
        while statusnum == False or t==False:
            n=raw_input("Enter number of players: ")
            statusnum=checkNumber(n)
            if statusnum == True:
                if int(n) > 8:
                    print "[  X  ] The maximum number of players is 8."
                    t=False
                else:
                    t=True
                    P=int(n)
                    return P,a,f


    elif c=="2":
        statusnum=False
        t = False
        while statusnum == False or t==False:
            n=raw_input("Enter number of rows you want: ")
            statusnum=checkNumber(n)
            if statusnum == True:
                if int(n) > 20:
                    print "[  X  ] The maximum number of rows is 20."
                    t=False
                elif int(n) < 6:
                    print "[  X  ] The minimum number of rows is 6."
                    t=False
                else:
                    t=True
        if t==True:
            P=int(n)
            return np,a,P

    elif c=="3":
        statusnum=False
        t=False
        while statusnum == False or t==False:
            n=raw_input("Enter number of columns you want: ")
            statusnum=checkNumber(n)
            if statusnum == True:
                if int(n) > 20:
                    print "[  X  ] The maximum number of columns is 20."
                    t=False
                elif int(n) < 7:
                    print "[  X  ] The minimum number of columns is 7."
                    t=False
                else:
                    t=True
        if t==True:
            P=int(n)
            return np,P,f
    else:
        return N,A,F



    #return c

if __name__ == '__main__':
    NofP=2
    numoff=6
    numofc=7
    m=menu1(NofP,numofc,numoff)
    while m!= "0":
        if m == "2":
            Y=menu2(NofP,numofc,numoff)
            y=list(Y)
            NofP=y[0]
            numofc=y[1]
            numoff=y[2]
            m = menu1(NofP,numofc,numoff)
        elif m == "1":
            newGame(NofP,numofc,numoff)
            m = menu1(NofP,numofc,numoff)
    print "--------------------END-------------------"
