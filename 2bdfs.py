
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}
def dfs(tree, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    for neighbor in tree[node]:
        dfs(tree, neighbor, visited)

    return visited
print("DFS Traversal:", dfs(tree, 1))