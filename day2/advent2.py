f = open('games.txt','r')
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
tot = 0
pos = 1
for line in f.readlines():
  goodGame = True
  line = line[line.find(':')+1:]
  lines=line.split(';')
  for item in lines:
    redNum = 0
    greenNum = 0
    blueNum = 0
    redIndex = item.find('red')
    blueIndex = item.find('blue')
    greenIndex = item.find('green')
    if(redIndex > 0):
      while redIndex > 0:
        if(item[redIndex].isnumeric()):
          if(item[redIndex-1].isnumeric()):
            redNum = item[redIndex-1:redIndex+1]
            break
          redNum = item[redIndex]
          break
        else:
          redIndex-=1
    if(blueIndex > 0):
      while blueIndex > 0:
        if(item[blueIndex].isnumeric()):
          if(item[blueIndex-1].isnumeric()):
            blueNum = item[blueIndex-1:blueIndex+1]
            break
          blueNum = item[blueIndex]
          break
        else:
          blueIndex-=1
    if(greenIndex > 0):
      while greenIndex > 0:
        if(item[greenIndex].isnumeric()):
          if(item[greenIndex-1].isnumeric()):
            greenNum = item[greenIndex-1:greenIndex+1]
            break
          greenNum = item[greenIndex]
          break
        else:
          greenIndex-=1
    if(int(redNum) > MAX_RED or int(greenNum) > MAX_GREEN or int(blueNum) > MAX_BLUE):
      goodGame = False
  if(goodGame):
    tot+=pos
  pos+=1
print(tot)