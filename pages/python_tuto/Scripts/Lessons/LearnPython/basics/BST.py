# Define the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    # Method to add a child node
    def add_child(self, node):
        self.children.append(node)

# Function for DFS traversal
def dfs(node):
    if node is None:
        return
    # Print the value of the current node (visit the node)
    print(node.value, end=' ')
    
    # Recursively visit all children of the current node
    for child in node.children:
        dfs(child)

# Build the tree as shown in the image
root = Node('A')

# Level 1 children
b = Node('B')
c = Node('C')
d = Node('D')
root.add_child(b)
root.add_child(c)
root.add_child(d)

# Level 2 children
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')
b.add_child(e)
c.add_child(f)
c.add_child(g)
d.add_child(h)

# Level 3 children
i = Node('I')
j = Node('J')
e.add_child(i)
f.add_child(j)

# Perform DFS traversal
print("DFS Traversal of the Tree:")
dfs(root)
