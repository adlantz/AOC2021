import numpy as np
binMatrix = np.array(list(map(lambda str : list(str[:-1]),open("3.txt", "r"))),dtype='i')
binArray = np.mean(np.transpose(binMatrix),1)
gammaRate = int("".join(binArray.round().astype(int).astype('str')),2)
epsilonRate = int(("".join(((binArray - 1).round().astype(int)*(-1)).astype('str'))),2)
print(gammaRate*epsilonRate)