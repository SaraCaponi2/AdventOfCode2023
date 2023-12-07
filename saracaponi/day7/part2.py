import collections

input = open('input.txt', 'r')
lines = input.read().splitlines()

cardMap = { 
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}

hands = []

for line in lines:
    parsed = line.split()
    hands.append({ 'hand': parsed[0], 'bid': int(parsed[1]), 'type': 0 })

def classify_hand(hand):
    handCollection = collections.Counter(hand)
    handCollectionMostCommonList = handCollection.most_common()
    mostCommonAmount = handCollectionMostCommonList[0][1]

    numOfJ = handCollection['J']

    if handCollectionMostCommonList[0][0] == 'J':
        if numOfJ == 5:
            mostCommonAmount = 0
        else:
            mostCommonAmount = handCollectionMostCommonList[1][1]

    if mostCommonAmount + numOfJ >= 5:
        return 7  # 5 of a kind
    elif mostCommonAmount + numOfJ == 4:
        return 6 # 4 of a kind
    elif mostCommonAmount + numOfJ == 3:
        secondCommonAmount = handCollectionMostCommonList[1][1]
        if secondCommonAmount == 2:
            return 5 # full house
        else:
            return 4  # 3 of a kind
    elif mostCommonAmount + numOfJ == 2:
        secondCommonAmount = handCollectionMostCommonList[1][1]
        if secondCommonAmount == 2:
            return 3  # 2 pairs
        else: 
            return 2   # 1 pairs
    else:
        return 1  # high card

for hand in hands:
    hand['type'] = classify_hand(hand['hand'])


def tie_breaker(a,b):
    for x in range(len(a)):
        if [*a][x] != [*b][x]:
            return {
                'a': cardMap[[*a][x]],
                'b': cardMap[[*b][x]]
            }
        
def bubbleSort(arr):
    for x in range(len(arr)-1,0,-1):
        for i in range(x):
            a = arr[i]['type']
            b = arr[i+1]['type']
            if a > b:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            elif a == b:
                tb = tie_breaker(arr[i]['hand'],arr[i+1]['hand'])
                if tb['a'] > tb['b']:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp

bubbleSort(hands)

grandTotal = 0
for idx, hand in enumerate(hands):
    grandTotal += (idx + 1) * hand['bid']

print(grandTotal)


    