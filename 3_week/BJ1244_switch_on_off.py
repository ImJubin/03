'''
1.입력값
N
switches

person (학생수)
gender, k

남자일 때, k배수만큼 스왑
여자일 때, k 기준으로 ,m

한줄에 20개 출력
'''

N = int(input())
switches = list(map(int, input().split()))
person = int(input())
for _ in range(person):
    gender, step = map(int, input().split())
