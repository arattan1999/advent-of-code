f = open('file.txt')

lines = f.readlines()
tot = 0
symbols = ['@','#','$','%','&','*','-','=','+','/']
sumList = []
i = 0
while i < len(lines):
  line = lines[i]
  j = 0
  while j < len(line):
    currNum = ''
    if(line[j].isdigit()):
      start=j
      include = False
      while line[j].isdigit() and j < len(line):
        currNum+=line[j]
        j+=1
      j-=1
      if(j < len(line)-1):
        j+=1
        if(line[j] in symbols):
          include = True
      if(start > 0):
        start-=1
        if(line[start] in symbols):
          include = True
      checkStr = ''
      if(i > 0):
        checkStr+=lines[i-1][start:j+1]
      if(i<len(lines)-1):
        checkStr+=lines[i+1][start:j+1]
      for item in checkStr:
        if(item in symbols):
          include=True
      if(include):
        sumList.append(int(currNum))
    else:
      j+=1
  i+=1

tot = 0
for i in sumList:
  tot+=i
print(tot)