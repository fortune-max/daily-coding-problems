num_map = {'2': "abc", '3': "def"}

num_input = "23"

def get_chars(num_in: str):
  if len(num_in) == 1:
    return list(num_map[num_in])

  ans = []
  for x in num_map[num_in[0]]:
    for y in get_chars(num_in[1:]):
      ans.append(x + y)
  return ans

print(get_chars("23"))
