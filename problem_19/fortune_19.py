house_colors_matrix = [
  [14, 2, 11],
  [11, 14, 5],
  [14, 3, 10],
]

N, K = len(house_colors_matrix), len(house_colors_matrix[0]) # Num houses, colors

for n in range(1, N):
  last_best_two = sorted(enumerate(house_colors_matrix[n-1]), key=lambda x: x[1])[:2]
  for k in range(K):
    best_prev_cost = last_best_two[0][1] if last_best_two[0][0] != k else last_best_two[1][1]
    house_colors_matrix[n][k] += best_prev_cost

print(min(house_colors_matrix[N-1]))
