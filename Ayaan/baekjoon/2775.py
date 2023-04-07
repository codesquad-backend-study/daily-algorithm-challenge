def solution():
    T = int(input())
    for _ in range(T):
        floor = int(input())
        room = int(input())
        print(howManyPeople(floor, room))
        
# 재귀로 몇명 살고 있는지 구하기
def howManyPeople(floor, room):
    if floor == 0:
        return room
    
    people = 0
    for i in range(1, room+1):
        people += howManyPeople(floor-1, i)
    return people
        
solution()