import collections
from typing import List


def solution(participant: List[str], completion: List[str]) -> str:
    # 카운터 사용 불가능할 수도 있으니 최대한 직접 구현
    participant_dict = collections.defaultdict(int)
    for p in participant:
        participant_dict[p] += 1

    completion_dict = collections.defaultdict(int)
    for c in completion:
        completion_dict[c] += 1

    # key, value 뽑을 때도 items() 꼭 붙여주기
    for key, value in participant_dict.items():
        if value != completion_dict[key]:
            return key

    return ''


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
