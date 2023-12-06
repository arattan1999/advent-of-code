f = open('file.txt')

times = f.readline()
distances = f.readline()

times = times[5:].strip().split(' ')
distances = distances[9:].strip().split(' ')
times = [num for num in times if num != '']
distances = [dist for dist in distances if dist != '']
totWins = []
for number in range(len(distances)):
  wins = 0
  record = int(distances[number])
  time = int(times[number])
  i = 0
  while i < time:
    if(i*(time-i) > record):
      wins+=1
    i+=1
  totWins.append(wins)

out = 1
for i in totWins:
  out*=i
print(out)