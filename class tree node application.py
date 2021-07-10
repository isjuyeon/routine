class Treenode:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
def treeheight(root):
    if root is None:
        return 0
    hLeft=treeheight(root.left)
    hRight=treeheight(root.right)
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

print(treeheight(root))
