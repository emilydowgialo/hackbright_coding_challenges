class LinkedListNode(object):

  def node(self, data=None, next_node=None, prev_node=None):

    self.data = data
    self.next = next_node
    self.prev = prev_node


class TreeNode(object):

  def __init__(self, data, children=None):

    self.data = data
    self.children = children or []

  def __repr__(self):

    return "data = %s" % self.data


def to_find(node, data):
  """ Recursively find the node """

  # Base case
  if node.data == data:
    return node

  found_node = None
  for n in node.children:

    # Recursion
    found_node = to_find(n, data)
    if found_node is not None:
      return found_node

  return None


def find_node(self, data):
  """ Non-recursively find the node using DEPTH-FIRST SEARCH """

  to_visit = [self]

  while to_visit:

    # Depth-first search because this traverses the tree and each node's children
    node = to_visit.pop()

    if node.data == data:
      return node

    to_visit.extend(node.children)


def find_node_breadth(self, data):
  """ Non-recursively find the node using BREADTH-FIRST SEARCH """

  to_visit = [self]

  while to_visit:

    # Breadth-first because popping from the front - this means first in
    # first out is happening
    node = to_visit.pop(0)

    if node.data == data:
      return node

    to_visit.extend(node.children)


treeroot = TreeNode('Sharon', [
    TreeNode('Angie', [TreeNode('Paria')]),
    TreeNode('Joel', [TreeNode('Balloonicorn', [
                               TreeNode('Heather'),
                               TreeNode('Leslie'),
                               TreeNode('Lavinia'),
                               TreeNode('Jessica'),
                               TreeNode('Ally')]),
                      TreeNode('Meggie'),
                      TreeNode('Rachel')]),
    TreeNode('Stefan', [TreeNode('Kari')])
])

g = to_find(treeroot, 'Balloonicorn')
print g
