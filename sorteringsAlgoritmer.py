#laver en variable kaldt lines, og
lines = [4,7,21,5,7,4,2,1]

#Laver en funktion der kun køres, når kaldt.
def selectionSort(lines):
    #her er der i loop, der looper igennem alle talende i lines -1
    for i in range(len(lines)-1):
        #laver en variable kaldt "min" og giver den værdien i
        min = i
        # loop ligesom sidste loop, men denne gang lægger den 1+ til variablen i, for hvert tal i lines
        for j in range(i+1,len(lines)):
            # hvis min er større end j loop
            if lines[min]>lines[j]:
                #laver variablen "min" fra i til j
                min = j
            #bytter om på værdierne af de to variabler min og i
        lines[min],lines[i] = lines[i],lines[min]
        #retunere variablen lines
    return lines

#laver en funktion der kun køres når kaldt
def insertionSort(case):
    #Looper igennem alle tal fra 1 og op
    for k in range(1, len(case)):
        #laver en array
        curNum = case[k]
        #Lopper igennem den nye array "k" og siger -1
        for j in range(k-1,-1,-1):
            # hvis array j er større end curNum
            if case [j] > curNum:
                #lav j+1 til j
                case [j+1] = case [j]
                #ellers
            else:
                # j+1 er lig med curNum
                case [j+1] = curNum
                #stop koden, så det ikke crasher, eller gør uønsket ting.
                break
