commandArray = map(lambda str : str[:-1].split(" "),open("2.txt", "r"))
zpos = 0
xpos = 0
for command in commandArray:
    if command[0] == "forward":
      xpos += int(command[1])
    if command[0] == "up":
      zpos -= int(command[1])
    if command[0] == "down":
      zpos += int(command[1])
print(xpos*zpos)