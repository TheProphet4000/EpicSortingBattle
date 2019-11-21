#Laver en funktion der kun køres, når kaldt.
def selectionSort(case):
    #Laver en kopi, så man ikke redigere i den orginale. Altså den laver en kopi i RAM.
    case.copy()
    #her er der i loop, der looper igennem alle talende i case -1
    for i in range(len(case)-1):
        #laver en variable kaldt "min" og giver den værdien i
        min = i
        # loop ligesom sidste loop, men denne gang lægger den 1+ til variablen i, for hvert tal i case
        for j in range(i+1,len(case)):
            # hvis min er større end j loop
            if case[min]>case[j]:
                #laver variablen "min" fra i til j
                min = j
            #bytter om på værdierne af de to variabler min og i
        case[min],case[i] = case[i],case[min]
        #retunere variablen case
    return case

#laver en funktion der kun køres når kaldt
def insertionSort(case):
    #Laver en kopi, så man ikke redigere i den orginale. Altså den laver en kopi i RAM.
    case.copy()
    #Looper igennem alle tal fra 1 og op
    for i in range(1, len(case)):
        #laver en array
        curNum = case[i]
        #Lopper igennem den nye array "k" og siger -1
        for j in range(i-1,-1,-1):
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

#laver en funktion der kun køres når kaldt
def bubbleSort(case):
   #køre igennem længten af case, og laver i, samt tæller ned (første gang er det x, næste gang siger den x-1)
   for i in range(len(case)-1,0,-1):
      #køre igennem længten af i, og kalder dem j
       for j in range(i):
           #Hvis j er større end j+1(dette er index i array)
           if case[j] > case[j+1]:
               #så byt om på talende
               temp = case[j]
               case[j] = case[j+1]
               case[j+1] = temp
    #retunere case
   return case

#køre kun dette kode, når man køre fra denne side
if __name__ == '__main__':
    #printer en mini test, så vi kan se at programmet fungere
    print(bubbleSort([7,6,100,4,6,7,88,5,9]))
    print(insertionSort([7,6,100,4,6,7,88,5,9]))
    print(selectionSort([7,6,10,7,6,7,88,5,9]))
