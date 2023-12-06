f = open('file.txt')

lines = f.readlines()
tot = 0
gearMap = {}
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
        if(line[j] == '*'):
          if((str(i)+str(j)) in gearMap.keys()):
            gearMap[(str(i)+str(j))]['count']+=1
            gearMap[(str(i)+str(j))]['value'].append(int(currNum))
          else:
            gearMap[(str(i)+str(j))] = {'count': 1,'value':[int(currNum)]}
      if(start > 0):
        start-=1
        if(line[start] == '*'):
          if((str(i)+str(start)) in gearMap.keys()):
            gearMap[(str(i)+str(start))]['count']+=1
            gearMap[(str(i)+str(start))]['value'].append(int(currNum))
          else:
            gearMap[(str(i)+str(start))] = {'count': 1,'value':[int(currNum)]}
      if(i > 0):
        temp = start
        while temp < start+(j-start)+1:
          if(lines[i-1][temp] == '*'):
            if((str(i-1)+str(temp)) in gearMap.keys()):
              gearMap[(str(i-1)+str(temp))]['count']+=1
              gearMap[(str(i-1)+str(temp))]['value'].append(int(currNum))
            else:
              gearMap[(str(i-1)+str(temp))] = {'count': 1,'value':[int(currNum)]}
          temp+=1
      if(i<len(lines)-1):
        temp = start
        while temp < start+(j-start)+1:
          if(lines[i+1][temp] == '*'):
            if((str(i+1)+str(temp)) in gearMap.keys()):
              gearMap[(str(i+1)+str(temp))]['count']+=1
              gearMap[(str(i+1)+str(temp))]['value'].append(int(currNum))
            else:
              gearMap[(str(i+1)+str(temp))] = {'count': 1,'value':[int(currNum)]}
          temp+=1
    else:
      j+=1
  i+=1

for entries in gearMap.values():
  print(entries)
  if(entries['count'] == 2):
    tot+=entries['value'][0]*entries['value'][1]
print(tot)
