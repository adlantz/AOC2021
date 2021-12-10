import numpy as np

def getRating(binMatrix,col,ratingType):
  if binMatrix.shape[0] == 1:
    return np.array(binMatrix[0])
  if ratingType == 'oxygen':
    avd = np.mean(np.transpose(binMatrix)[col])
    if avd == 0.5:
      d = 1
    else:
      d = round(avd)
  else:
    avd = (np.mean(np.transpose(binMatrix)[col])-1)*(-1)
    if avd == 0.5:
      d = 0
    else:
      d = round(avd)
  bm = []
  for bin in binMatrix:
    if bin[col] == d:
      bm.append(bin)
  return getRating(np.array(bm),col+1,ratingType)

binMatrix = np.array(list(map(lambda str : list(str[:-1]),open("3.txt", "r"))),dtype='i')
oxygenRating=int("".join(getRating(binMatrix,0,'oxygen').astype('str')),2)
CO2Rating=int("".join(getRating(binMatrix,0,'CO2').astype('str')),2)
print(oxygenRating*CO2Rating)