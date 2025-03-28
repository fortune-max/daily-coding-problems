from typing import Set

class Node:
    def __init__(self, val):
        self.val = val
        self.children_length = len(val) + 1
        self.children: Set[Node] = set()

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.val == other.val
        return False
    
    def __hash__(self) -> int:
        return hash(self.val)

    def get_leaves(self):
        if not self.children:
            return [self.val]
        leaves = []
        for child in self.children:
            leaves.extend(child.get_leaves())
        return leaves

def make_treap(possible_queries):
    [process_word(query) for query in possible_queries]

def get_parent(word):
    parent = root
    while parent and parent.children_length != len(word):
        substr = word[:parent.children_length]
        parent = next((new_parent for new_parent in parent.children if new_parent.val == substr), None)
    return parent or Node("")

def put_in_treap(word):
    parent: Node = get_parent(word)
    assert parent.children_length == len(word)
    parent.children.add(Node(word))

def process_word(word):
    substrings = [word[:x+1] for x in range(len(word))]
    [put_in_treap(substring) for substring in substrings]

def get_node(word):
    return get_parent(word + 'a')


root = Node("")
possible_queries = ["dog", "deer", "deal"]
make_treap(possible_queries)

print(get_node("de").get_leaves()) # deer, deal
