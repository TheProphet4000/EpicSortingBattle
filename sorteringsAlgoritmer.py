import sys

#her laver vi en en variabel kladt j, der læser MiniTest.txt filen, og viser dens indhold
with open('testfiles/testcase0.txt', 'r') as file:
    data = file.read().replace('\n', '')
print(data)

#selectionSort()
