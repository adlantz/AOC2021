import numpy as np

input = np.loadtxt('1.txt',dtype='i')

count = 0
i=0
while(i+3<len(input)):
  if sum(input[i:i+3]) < sum(input[i+1:i+4]):
    count+=1
  i+=1
print(count)