class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,val):
    if(root==None):
        root=node(val)
        return root
    if(val<root.val):
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root

def heightval(root,l,lev):
    if(root!=None):
        if(len(l)==lev):
            l.append(root.val)
        heightval(root.left,l,lev+1)
        heightval(root.right,l,lev+1)

a=input()
a=a.split(' ')
root=None
for i in a:
    root=insert(root,int(i))
lev=0
l=[]
heightval(root,l,lev)
print(len(l))
