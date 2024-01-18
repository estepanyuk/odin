class TreaNode:
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

tree = TreaNode(1,
                TreaNode(4,
                         TreaNode(2, None, None),
                         TreaNode(3, None,
                                  TreaNode(1, None, None))),
                TreaNode(7,
                         TreaNode(5, None, None),
                         TreaNode(4, None, None)))
print(max_sum(tree))