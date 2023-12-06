f = open('file.txt', 'r')

seedLine = f.readline()
seedLine = seedLine[7:-1]

seeds = seedLine.split(' ')
f.readline()
f.readline()
line = f.readline()
seedToSoil = {}
while line != '\n':
  temp = line.split(' ')
  source = int(temp[1])
  dest = int(temp[0])
  for i in range(int(temp[2])-1):
    seedToSoil[source] = dest
    source+=1
    dest+=1
    print(source)
    print(dest)
  # print(line)
  line = f.readline()
print(seedToSoil)
# f.readline()
# line = f.readline()
# while line != '\n':
#   print(line)
#   line = f.readline()
# f.readline()
# line = f.readline()
# while line != '\n':
#   print(line)
#   line = f.readline()
print(seeds)