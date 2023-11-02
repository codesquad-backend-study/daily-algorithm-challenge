# 첫번째 풀이
# i랑 그 자리수들을 다 더한 값을 num에 계속 저장하자
# 그 num이 생성자인지 아닌지 판단하고, 생성자가 아니면 출력하자 (X)

# 라고 생각했었는데 그렇게 되면 셀프 넘버 판별이 힘들지
# 그냥 한꺼번에 각 자리수만 저장 후 나중에 셀프 넘버를 판별하는 식으로 가자!
# 배열 생성 (각 자리수 더한 배열)
digit_sum_list = []
for i in range(1, 10001):
    # 10으로 나누면서 해줄 수는 있겠지만 귀찮으니
    # 그냥 스트링으로 하고 다시 변환하는 방법 사용
    for j_str in str(i):
        i += int(j_str)

    # 각 자리수를 더한 배열 계속 저장
    digit_sum_list.append(i)

for i in range(1, 10001):
    if i not in digit_sum_list:
        print(i)

# 두번째 풀이
digit_sum_list = set()
for i in range(1, 10001):
    # 10으로 나누면서 해줄 수는 있겠지만 귀찮으니
    # 그냥 스트링으로 하고 다시 변환하는 방법 사용
    for j_str in str(i):
        i += int(j_str)

    # 각 자리수를 더한 집합 계속 저장
    digit_sum_list.add(i)

# self_num = sorted([i for i in range(1, 10001)] - digit_sum_list)
# 배열은 빼기가 안 되네.. 검색 후 집합으로 수정
# 라고 생각을 했었는데 또 이걸 빼줄 필요가 없었음
# 그래서 두가지 풀이로 풀 수 있음

for answer in sorted(set(range(1, 10001)) - digit_sum_list):
    print(answer)
