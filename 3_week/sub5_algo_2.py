T = int(input())

def pre_order(idx):
    results[0] = results[0] + tree[idx]
    if idx*2 <= N:
        pre_order(idx*2)
    elif idx*2 + 1 <= N:
        pre_order(idx*2+1)

def in_order(idx):

    
    if idx*2 <= N:
        in_order(idx*2)
        results[1] = results[1] + tree[idx]
    elif idx*2 + 1 <= N:
        in_order(idx*2+1)

def post_order(idx):

    
    if idx*2 <= N:
        post_order(idx*2)
    elif idx*2 + 1 <= N:
        post_order(idx*2+1)
    results[2] = results[2] + tree[idx]

for tc in range(1,T+1):
    N = int(input())
    tree = [-1]


    tree += input().split()

    results = ['', '', '']

    pre_order(1)
    in_order(1)
    post_order(1)
    results = list(map(int, results, [2,2,2]))
    print(max(results))

