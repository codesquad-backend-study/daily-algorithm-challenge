# 원래 생각했던 풀이 숫자를 일일히 계산해가며 셀프 넘버 아닌걸 출력하려고 했음, 그러나 규칙이 까탈스러움
# divisorList = [1001, 101, 11]
#
# for num in range(1, 10001):
#     dividend = num
#     if dividend in range(10, 20) and dividend % 2 == 0:
#         dividend = 0
#     for divisor in divisorList:
#         dividend = dividend % divisor
#     if dividend != 0 and (dividend + 11) % 2 != 0:
#         print(num)

# 풀이 참고해서 푼 풀이, 셀프넘버를 찾고 넣어준 다음 셀프 아닌 걸 출력하는 방식
numList = {i: 0 for i in range(10001)}

for cnt in range(10001):
    num = cnt
    # 불필요한 반복문 제거하기 위해서 일일히 계선(범위가 정해져 있음)
    num = num + num // 1000 + (num % 1000) // 100 + (num % 100) // 10 + num % 10
    # 여기에 구한 셀프넘버가 10000이상이면 탈출하면 되지만, 셀퍼넘버가 단조롭게 증가 하지 않고, 셀프넘버와 범위(10000)사이에 차이가 크지 않아 그냥 진행
    numList[num] = 1
for element in numList:
    if numList[element] == 0:
        print(element)
