import re

input = open('input.txt', 'r')
lines = input.read().splitlines()

time = lines[0].split(':')[1]
# remove whitespace and parse as int
time = int(re.sub(r"[\n\t\s]*", "", time))

distance = lines[1].split(':')[1]
# remove whitespace and parse as int
distance = int(re.sub(r"[\n\t\s]*", "", distance))

waysToBeat = 0

def calculate_distance(holdingTime, raceTime):
   return holdingTime * (raceTime - holdingTime)

for testingTime in range(0, time):
    if calculate_distance(testingTime, time) > distance:
        waysToBeat += 1


print(waysToBeat)
