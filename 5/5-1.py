import numpy as np
inputList = open("5.txt", "r").readlines()

pntslist = []
for line in inputList:
  splitline = line[:-1].split(" ")
  p1 = tuple((int(splitline[0].split(',')[0]),int(splitline[0].split(',')[1])))
  p2 = tuple((int(splitline[-1].split(',')[0]),int(splitline[-1].split(',')[1])))
  if(p1[0] == p2[0]):
    for i in range(min(p1[1],p2[1]),max(p1[1],p2[1])+1):
      pntslist.append((p1[0],i))
  elif p1[1] == p2[1]:
    for i in range(min(p1[0],p2[0]),max(p1[0],p2[0])+1):
      pntslist.append((i,p1[1]))


coordsMatrix = np.zeros((999,999))

for t in pntslist:
  coordsMatrix[t[0]][t[1]] +=1

dups=0
for c in coordsMatrix.flatten():
  if c>1:
    dups+=1

print(dups)


#first attempt that failed because it took too long!
# foundList = []
# dupset = set()
# for t in pntslist:
#   if t not in foundList:
#     foundList.append(t)
#   else:
#     dupset.add(t)
  
# print(len(dupset))