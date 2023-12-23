A = [3, 7, 8, 10]
B = [99, 1, 8, 10]

MAX_NODE_VAL = 999
is_in_a = [False] * (MAX_NODE_VAL + 1)

[is_in_a.__setitem__(a, True) for a in A]

ans = [b for b in B if is_in_a[b]][0]
print(ans)
