lines = [4,7,21,5,7,4,2,1]

def selectionSort(lines):
    for i in range(len(lines)-1):
        min = i
        for j in range(i+1,len(lines)):
            if lines[min]>lines[j]:
                min = j
        lines[min],lines[i] = lines[i],lines[min]
    return lines
print(selectionSort(lines))
