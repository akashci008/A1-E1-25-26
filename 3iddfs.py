

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def DLS(node, depth_limit, result):
    if node is None:
        return
    
    result.append(node.value)
    
    if depth_limit <= 0:
        return
    
    for child in node.children:
        DLS(child, depth_limit - 1, result)

def IDDFS(root, max_depth):
    for depth in range(max_depth + 1):
        result = []
        DLS(root, depth, result)
        print(f"Depth Limit {depth}: Visited nodes {result}")

root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

root.children = [n2, n3]
n2.children = [n4, n5]
n3.children = [n6, n7]

max_depth = 2
print("IDDFS Traversal:")
IDDFS(root, max_depth)