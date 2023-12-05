input = open('input.txt', 'r')
lines = input.read().splitlines()

rows = 140
cols = 140

symbols = "#*$+@&-=%/"

neighbors = [-1, 0, 1]

matrix = [[0]*cols for i in range(rows)]

for rIdx, line in enumerate(lines):
    for cIdx, c in enumerate(line):
        matrix[rIdx][cIdx] = c

num = ''
valid = False
validNums = []
for x in range(0, rows):   
    for y in range(0, cols):
        if matrix[x][y].isdigit():
            num += matrix[x][y]

            for xNeighbor in neighbors:
                for yNeighbor in neighbors:
                    try: 
                        if matrix[x + xNeighbor][y + yNeighbor] in symbols:
                            valid = True
                    except: IndexError

        # if at last index or if next index is not a number
        if y == cols -1 or not matrix[x][y + 1].isdigit():
            if valid:
                validNums.append(int(num))
            num = ''
            valid = False

print(sum(validNums))
