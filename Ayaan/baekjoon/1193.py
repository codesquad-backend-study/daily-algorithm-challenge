def solution():
    X = int(input())
    std = 1
    step = 1
    # step : X가 있는 대각선 라인의 숫자 개수
    # std : 대각선 라인의 시작하는 숫자
    while(True):
        std = std + step
        if X < std:
            break    
        step += 1
        
    std = std - step
    # std와 step을 알면 답을 구할 수 있다.
    if step % 2 == 0:
        print("{0}/{1}".format(1+(X-std), step-(X-std)))
    else:
        print("{1}/{0}".format(1+(X-std), step-(X-std)))

solution()