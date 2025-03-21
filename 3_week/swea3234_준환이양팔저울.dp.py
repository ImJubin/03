'''
dp[state] = {key : val}
                    경우의수
어떤 무게추 사용하고 있니? > 비트로, visited처리 000000000 < 


'''
from math import factorial

T = int(input())

def perm(cnt, left_weight, right_weight):
    global answer

    if right_weight > left_weight:
        return 0


    if dp[state].get(left_weight):
        return dp[state][left_weight]


    # 내가 다 놓을 수 있다면
    if cnt == N:
        dp[state][left_weight] = 1
        return dp[state][left_weight]
    
    elif left_weight > right_weight + (total_weight-left_weight-right_weight):
        dp[state][left_weight] =    #N-cnt ,,    
        return dp[state][left_weight]
    
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    total_weight = sum(weights)
    visited = [0]*N
    dp = [{} for _ in range(2**9)] #2**9 -1
    answer = 0      #가짓수

    dp[0][0] = 0
    perm(0, 0, 0)   #왜 세개인자를? (몇개골랐는지, 왼쪽무게추, 오른쪽무게추.)


###################################################################디피

