def solution(formula: str) -> int:
    # answer = 0
    #
    # # 그리디니까 오직 마이너스거나 플러스면 바로 리턴해주자
    # if '-' not in formula and '+' in formula:
    #     return sum(map(int, formula.split('+')))
    # elif '+' not in formula and '-' in formula:
    #     minus_formula = list(map(int, formula.split('-')))
    #     for i in range(len(minus_formula)):
    #         if i == 0:
    #             answer = minus_formula[i]
    #             continue
    #         answer -= minus_formula[i]
    #     return answer
    #
    # # 메인 로직
    # # '-'로 분리해서 순서대로 빼주면 됨
    # plus_formula = formula.split('-')
    # for i in range(len(plus_formula)):
    #     if i == 0 and '+' not in plus_formula[i]:
    #         answer = int(plus_formula[i])
    #         continue
    #
    #     if '+' in plus_formula[i]:
    #         answer -= sum(map(int, plus_formula[i].split('+')))
    #     else:
    #         answer -= int(plus_formula[i])
    #
    # return answer
    # 개킹받아..

    answer = 0

    minus_formula = formula.split('-')
    # 굳이 if로 체크하지 말고 split 할 때, 그 문자가 없으면 얘가 무시해 주니까 바로 하자
    # 20번째 줄에서 내가 했던 걸 쉽게 쉽게
    for minus in minus_formula[0].split('+'):
        answer += int(minus)

    # 이렇게 0번째랑 첫번째부터 마지막까지랑 각각 분리해 주는게 깔끔하니 꼭 기억해 두자
    for minus in minus_formula[1:]:
        for plus in minus.split('+'):
            answer -= int(plus)

    return answer


formula = input()
print(solution(formula))
