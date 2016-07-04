class LinkedListNode(object):

  def node(self, data=None, next_node=None):

    self.data = data
    self.next = next_node


class TreeNode(object):

  def __init__(self, data, children=None):

    self.data = data
    self.children = children or []

  def __repr__(self):

    return "data = %s" % self.data


def to_find(node, data):

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
