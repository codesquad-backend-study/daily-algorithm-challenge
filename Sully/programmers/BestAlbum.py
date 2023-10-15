import collections
from typing import List


# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
def solution(genres: List[str], plays: List[int]) -> List[int]:  # (장르, 재생 횟수)
    answer = []

    sum_plays_map = collections.defaultdict(int)
    index_list_plays_map = collections.defaultdict(list)
    for i in range(len(genres)):
        sum_plays_map[genres[i]] += plays[i]
        index_list_plays_map[genres[i]].append([i, plays[i]])

    print(sum_plays_map)
    print(index_list_plays_map)

    for genre, _ in sorted(sum_plays_map.items(), key=lambda x: x[1], reverse=True):
        # [:2] -> 가장 많이 재생된 노래를 "두 개씩" 모아 베스트 앨범 출시
        for index, _ in sorted(index_list_plays_map[genre], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(index)

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
