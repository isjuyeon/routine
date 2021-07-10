from collections import deque
class TreeNode:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent=parent
        self.left = left
        self.right = right #가리키는 노드들을 호출함
    def __str__(self):
        return str(self.key)
    def preorder(self):
        if self is not None:
            print(self.key,end='')
            self.preorder(self.left)
            self.preorder(self.right)
    def inorder(self):
        if self is not None:
            self.preorder(self.left)
            print(self.key, end='')
            self.preorder(self.right)
    def postorder(self):
        if self is not None:
            self.preorder(self.left)
            self.preorder(self.right)
            print(self.key, end='')

    def levelorder(self):
        q=deque()
        q.appendleft(self)
        while q is not None:#아무래도 q!=None이랑 뭐가 다른지는 잘 모르겠음
            n = q.pop()
            if n is not None:
                print(n.data, end=' ')
                q.appendleft(n.left)
                q.appendleft(n.right)

    def count_node(self):
        if self is None:
            return 0
        else:
            return 1 + self.count_node(self.left) + self.count_node(self.right)

    def count_leaf(self):
        if self is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        else:
            return self.count_leaf(self.left) + self.count_leaf(self.right)


a=TreeNode()
a.preorder([1,2,3])