from grafiti import Node
from icecream import ic

print=ic
def sample_func():
    str_ = "Hello World!"
    return str_

n2 = lambda: 'this is n2'
n3 = lambda: 'this is n3'

n2_node = Node(n2)
node = Node(sample_func, depends_on=[n2_node])
node_n3 = Node(n3, depends_on=[node])
print()
print(n2_node.output)
ans = node.backward()
print(node.output)

print((n2_node.output))
