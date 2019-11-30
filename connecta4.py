#coding: utf-8#
import string
import itertools
from funtions4 import *

def newGame(nj,c,f):
    numberofplayers = nj
    torn = 1
    T=creaTaulell(f,c)
    finishgame = False
    while finishgame == False:
        if torn > numberofplayers:
            torn = 1
        escriureTaulell(T)
        print ""
        print "[  PLAYER",torn,"  ] - IS YOUR TURN!"
        print ""
        okpos = False
        oknumber = False
        while okpos == False or oknumber == False:
            numberplayedentered = raw_input("Enter column pos: ")
            oknumber = checkNumber(numberplayedentered)
            if oknumber == True:
                x=int(numberplayedentered)
                okpos = comprovaCord(x,T)
                if okpos == True:
                    break
        if oknumber == True and okpos == True:
            T=tirada(torn,T,x)
            cfourH=quatrihor(T)
            cfourV=quatriver(T)
            cfourDP=quatridiagprinc(T,torn)
            cfourDS=quatridiagsecun(T,torn)
            if cfourH or cfourV or cfourDP or cfourDS:
                escriureTaulell(T)
                print ""
                print "Player",torn,"win the game!!! Congratulations!!!"
                print ""
                break
            else:
                torn+=1
