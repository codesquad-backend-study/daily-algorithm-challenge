def solution():
    N, K = map(int, input().split())
    
    def binomial_recursive(N, K):
        # N개 중 0개를 뽑는 경우는 1
        # N개 중 N개를 뽑는 경우도 1
        if K == 0 or N == K:
            return 1

        return binomial_recursive(N-1, K) + binomial_recursive(N-1, K-1)
    
    print(binomial_recursive(N, K))
    
solution()