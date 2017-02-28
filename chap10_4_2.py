class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree(node):
    if node is not None:
        print(node.value)
        print_tree(node.left)
        print_tree(node.right)