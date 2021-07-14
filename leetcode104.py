class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def ListToTree(nodes):
    if len(nodes) == 0:
        return
    Q = []
    head = TreeNode(nodes.pop(0))
    Q.append(head)
    while nodes:
        node = Q.pop(0)
        if not node:
            continue
        if nodes:
            left = nodes.pop(0)
            if left != '*':
                node.left = TreeNode(left)
        if nodes:
            right = nodes.pop(0)
            if right != '*':
                node.right = TreeNode(right)
        Q.append(node.left)
        Q.append(node.right)
    return head

def maxDepth(head):
    if head is None:
        return 0
    else:
        left_height = maxDepth(head.left)
        right_height = maxDepth(head.right)
        return max(left_height, right_height) + 1


print(maxDepth(ListToTree([3,9,20,'*','*',15,7])))