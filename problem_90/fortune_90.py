from random import randrange
from bisect import bisect_left, bisect_right

n = 39
l = {11, 13, 34, 37, 400}
l = sorted(l)

nums_to_skip = bisect_left(l, n)

# 1 -> 0, 2 -> 1, 3 -> 2, 4 -> 3, .., 9 -> 8, 10 -> 9, 11 -> 10, 12 -> 12, 13 -> 14, 33 -> 35

new_arr = [(0, -1)]

for skipped, x in enumerate(l, start=0):
  new_arr.append((x + 1 - skipped, x + 1))

chosen_idx = randrange(n - nums_to_skip) + 1 # 1-idxed

idx = bisect_right(new_arr, (chosen_idx, float("inf")))
left = new_arr[idx - 1]

steps_right = chosen_idx - left[0]
ans = left[1] + steps_right
