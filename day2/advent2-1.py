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
  redNum = 0
  greenNum = 0
  blueNum = 0
  temp = 0
  for item in lines:
    redIndex = item.find('red')
    blueIndex = item.find('blue')
    greenIndex = item.find('green')
    if(redIndex > 0):
      while redIndex > 0:
        if(item[redIndex].isnumeric()):
          if(item[redIndex-1].isnumeric()):
            if(int(item[redIndex-1:redIndex+1]) > redNum):
              redNum = int(item[redIndex-1:redIndex+1])
            break
          if(int(item[redIndex]) > redNum):
            redNum = int(item[redIndex])
          break
        else:
          redIndex-=1
    if(blueIndex > 0):
      while blueIndex > 0:
        if(item[blueIndex].isnumeric()):
          if(item[blueIndex-1].isnumeric()):
            if(int(item[blueIndex-1:blueIndex+1]) > blueNum):
              blueNum = int(item[blueIndex-1:blueIndex+1])
            break
          if(int(item[blueIndex]) > blueNum):
            blueNum = int(item[blueIndex])
          break
        else:
          blueIndex-=1
    if(greenIndex > 0):
      while greenIndex > 0:
        if(item[greenIndex].isnumeric()):
          if(item[greenIndex-1].isnumeric()):
            if(int(item[greenIndex-1:greenIndex+1]) > greenNum):
              greenNum = int(item[greenIndex-1:greenIndex+1])
            break
          if(int(item[greenIndex]) > greenNum):
            greenNum = int(item[greenIndex])
          break
        else:
          greenIndex-=1
  pos+=1
  if(redNum > 0 and blueNum > 0 and greenNum > 0):
    temp+=redNum * blueNum * greenNum
  elif(redNum > 0 and blueNum > 0 and greenNum == 0):
    temp+=redNum * blueNum
  elif(redNum > 0 and blueNum == 0 and greenNum > 0):
    temp+=redNum * greenNum
  elif(redNum > 0 and blueNum == 0 and greenNum == 0):
    temp+=redNum
  elif(redNum == 0 and blueNum > 0 and greenNum > 0):
    temp+=blueNum * greenNum
  elif(redNum == 0 and blueNum == 0 and greenNum > 0):
    temp+=greenNum
  elif(redNum == 0 and blueNum > 0 and greenNum == 0):
    temp+=blueNum
  tot+=temp
print(tot)