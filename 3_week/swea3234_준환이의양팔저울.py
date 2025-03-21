'''
백트래킹버전전
'''
from math import factorial

T = int(input())

def perm(cnt, left_weight, right_weight):
    global answer

    if right_weight > left_weight:
        return
    elif left_weight > right_weight + (total_weight-left_weight-right_weight):
        answer += 2**(N-cnt)*factorial(N-cnt)   #N-cnt ,,

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            perm(cnt+1, left_weight + weights[i], right_weight)
            perm(cnt+1, left_weight, right_weight + weights[i])


    # 내가 다 놓을 수 있다면
    if cnt == N:
        answer += 1
        return
    

for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    total_weight = sum(weights)
    visited = [0]*N
    answer = 0      #가짓수
    
    perm(0, 0, 0)   #왜 세개인자를? (몇개골랐는지, 왼쪽무게추, 오른쪽무게추.)


###################################################################디피

