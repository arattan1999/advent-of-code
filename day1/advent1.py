f = open('file.txt', 'r')
numList = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}
numbers = []
def findFirst(i: str) -> int:
  checkStr = ''
  for c in range(len(i)):
    if(i[c].isdigit()):
      return int(i[c])*10
    else:
      checkStr+=i[c]
      for c2 in i[c+1:]:
        checkStr+=c2
        if(checkStr in numList):
          return numList[checkStr]*10
      checkStr = ''

def findLast(i: str) -> int:
  lastVal: int = 0
  checkStr = ''
  for c in range(len(i)):
    if(i[c].isdigit()):
      lastVal = int(i[c])
    else:
      checkStr+=i[c]
      for c2 in i[c+1:]:
        checkStr+=c2
        if(checkStr in numList):
          lastVal = numList[checkStr]
      checkStr = ''
  return int(lastVal)
    
for i in f.readlines():
  number = 0
  number+=findFirst(i)
  number+=findLast(i)
  numbers.append(number)
print(numbers)
out = 0
for i in numbers:
  out += i

print(out)