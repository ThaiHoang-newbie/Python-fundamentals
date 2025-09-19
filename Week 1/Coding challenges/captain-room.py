from collections import Counter

k = int(input())
roomsList = input()
counterList = Counter(roomsList.split())
for room, count in counterList.items():
    if(count == 1):
        print(room)