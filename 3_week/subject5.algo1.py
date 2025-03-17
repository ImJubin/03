'''
3
6 2
100101
7 3
1001011
7 5
1001011


N은 이진수 길이, K는 1 포함 수

1 발견할 때 비로소 시작, 사이 0까지 고려하고, 1 세면서 돌다가, K개 다 채워지면 끝냄
카운트한 리스트 길이값 비교, 더 큰 값 갱신.
K개에 못미치면 0개임.

1.
T
N,K
max_count
arr
    count

2. 1 세주기

3. 1들어간 값 비교후 최댓값 갱신

'''

T = int(input())

for tc in range(1,T+1):
    answer = 0
    N, K = map(int, input().split())
    bins = input()
    
    for l in range(N-K):
        for r in range(l+1, N):
            cur_binary = bins[l:r+1]
            if cur_binary[0] == '1' and cur_binary[-1] == '1':
                if cur_binary.count('1') == K:
                    answer = max(answer, r-1+1)
                    break


    print(f'#{tc} {answer}')
