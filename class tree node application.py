class Treenode:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
    def treeheight(self):
        if self is None:
            return 0
        hLeft=self.treeheight(self.left)
        hRight=self.treeheight(self.right)
        if (hLeft>hRight):
            return hLeft+1
        else:
            return hRight+1
d = Treenode('D', None, None)
e = Treenode('E', None, None)
b = Treenode('B', d, e)
f = Treenode('F', None, None)
c = Treenode('C', f, None)
root = Treenode('A', b, c)

print(Treenode.treeheight(root))
#에러난거 꼭 고치고, 디버깅까지해서 재귀 이해 again