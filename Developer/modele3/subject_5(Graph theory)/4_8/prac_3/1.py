class TreeNode:
    value = 0
    left = None
    right = None

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def max_sum(root):
    if root is None:
        return 0
    max_left = max_sum(root.left)
    max_right = max_sum(root.right)
    return max(max_left, max_right) + root.value

tree = TreeNode(1,
                TreeNode(4,
                         TreeNode(2, None, None),
                         TreeNode(3, None,
                                  TreeNode(1, None, None))),
                TreeNode(7,
                         TreeNode(5, None, None),
                         TreeNode(4, None, None)))

print(max_sum(tree))