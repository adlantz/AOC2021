import numpy as np

input = np.loadtxt('1.txt',dtype='i')

count = 0
for i in range(1,len(input)):
  if input[i]>input[i-1]:
    count+=1

print(count)