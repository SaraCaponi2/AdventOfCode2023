input = open('input.txt', 'r')
lines = input.read().splitlines()

totals = []

for card in lines:
    parsed = card.split(':')[1].split('|')
    winningNums = parsed[0].split()
    myNums = parsed[1].split()

    points = 0
    for myNum in myNums:
        if myNum in winningNums:
            if points == 0:
                points = 1
            else:
                points = points * 2

    
    totals.append(points)

print(sum(totals))