f = open('file.txt')

times = f.readline()
distances = f.readline()

times = times[5:].strip().split(' ')
distances = distances[9:].strip().split(' ')
times = [num for num in times if num != '']
times = ''.join(times)
distances = [dist for dist in distances if dist != '']
distances = ''.join(distances)
totWins = []

wins = 0
record = int(distances)
time = int(times)
i = 0
while (i*(time-i) < record):
  i+=1

ways = time-i-(i-1)
print(ways)
