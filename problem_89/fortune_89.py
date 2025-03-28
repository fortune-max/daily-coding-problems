class Node(object):
  value = None
  left = None
  right = None

  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def node_valid(curr: Node, min_val=float("-inf"), max_val=float("inf")):
  ans = min_val <= curr.value <= max_val
  if not ans:
    print("culprit", curr.value)
  if curr.left:
    ans &= node_valid(curr.left, min_val, curr.value)
  if curr.right:
    ans &= node_valid(curr.right, curr.value, max_val)
  return ans

root = Node(15, Node(10), Node(14))
print(node_valid(root)) 
