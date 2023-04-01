import math

def solution(fees, records):

    enter = {} # 입차 기록 { 차량번호 : 시간 }
    result = {} # { 차량번호 : 누적시간}
   
    for s in records :
        car = s[6:10]
        tmp = s[:5].split(':')
        time = int(tmp[0])*60 + int(tmp[1])
        
        if 'IN' in s :
            enter[car] = time
            result[car] = 0
        else :
            total = time - enter[car]
            del enter[car]
            result[car] += total
            
    allDay = (23*60+59) # 출차하지 않았을 때

    for car in enter :
        total = allDay - enter[car]
        if car in result :
            result[car] += total
        else : 
            result[car] = total

    nums = sorted(result)
    answer = []

    for car in nums :
        time = result[car]
        if time <= fees[0] :
            answer.append(fees[1])
        else :
            fee = math.ceil((time - fees[0]) /fees[2]) * fees[3] + fees[1]
            answer.append(fee)

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))