# 'testfiles/testcase0.txt' Dette er den rigtige test
#----------------------------------------------------------------------
# åbner txt filen der indeholder det, der skal sorteres.
#bruger data.read til at læse hele teksten i en køre. Gemmer det som lines
with open('MiniTest.txt', 'r') as data:
    lines = data.read()
#finder maksimal størrelse
størrelse = len(lines)

# Looper igennem hver enklete bogstav i lines variablen
for i in lines:
