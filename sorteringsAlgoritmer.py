#laver en variable kaldt lines, og 
lines = [4,7,21,5,7,4,2,1]

#Laver en fungtion der kun køres, når kaldt.
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
    #viser os hvad der er sorteret i terminalen
print(selectionSort(lines))
