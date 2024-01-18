class TreaNode:
    value = 0
    left = None
    right = None

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

answer = 0
def max_sum(root):
    helper(root)
    return answer

def helper(node):
    if node is None:
        return 0
    max_left = max(helper(node.left), 0)
    max_right = max(helper(node.right), 0)
    global answer
    answer = max(answer, max_left + max_right + node.value)
    return max(max_left, max_right) + node.value


tree = TreaNode(-10,
                TreaNode(9, None, None),
                TreaNode(20,
                        TreaNode(-3,
                                TreaNode(5, None,
                                    TreaNode(-2, None, None)),
                                TreaNode(-4, None, None)),
                        TreaNode(8, None,
                            TreaNode(-2, None, None))))
print(max_sum(tree))