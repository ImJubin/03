### # BOJ 2477. 참외밭

K = int(input())
dirs = [0]*6
lengths = [0]*6
count_dir = [0]*5
count2_idxs = []

for i in range(6):
    dirs[i], lengths[i] = map(int, input().split())
    count_dir[dirs[i]] += 1
    if count_dir[dirs[i]] >= 2:
        count2_idxs.append(i)

max_idx = lengths.index(max(lengths))
if lengths[max_idx-1] > lengths[(max_idx+1)%6]:
    second_idx = max_idx-1
else:
    second_idx = (max_idx+1)%6
total_area = lengths[max_idx]*lengths[second_idx]

l, r = count2_idxs
minus_area = -1
if dirs[l-2] == dirs[l] and dirs[r-2] == dirs[r]:
    minus_area = lengths[l]*lengths[l-1]
elif dirs[r-2] == dirs[r]:
    minus_area = lengths[r]*lengths[r-1]
elif dirs[l-2] == dirs[l]:
    minus_area = lengths[l-2]*lengths[l-1]
else:
    minus_area = lengths[0]*lengths[-1]

print((total_area-minus_area)*K)