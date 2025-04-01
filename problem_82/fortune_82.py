file_pos = {}

def read7(file_name: str) -> str:
  with open(file_name, "r") as f:
    f.seek(pos := file_pos.get(file_name, 0))
    file_pos[file_name] = pos + 7
    return f.read(7) or ""

print(read7("problem_82/readme.md"))
print(read7("problem_82/readme.md"))
