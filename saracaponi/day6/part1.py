input = open('input.txt', 'r')
lines = input.read().splitlines()

times = lines[0].split(':')[1].split()
distances =  lines[1].split(':')[1].split()

races = []

for idx in range(0, 4):
    race = {
        'time': int(times[idx]),
        'distance': int(distances[idx]),
        'waysToBeat': 0
    }
    races.append(race)

def calculate_distance(holdingTime, raceTime):
   return holdingTime * (raceTime - holdingTime)

for race in races: 
    for testingTime in range(0, race['time']):
        if calculate_distance(testingTime, race['time']) > race['distance']:
            race['waysToBeat'] += 1


total = races[0]['waysToBeat'] * races[1]['waysToBeat'] * races[2]['waysToBeat'] * races[3]['waysToBeat']
print(total)