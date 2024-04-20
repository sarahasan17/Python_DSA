class node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def insert(root,a):
    if(root==None):
        root=node(a)
        return root
    if(root.val>a):
        root.left=insert(root.left,a)
    else:
        root.right=insert(root.right,a)
    return root
def findmin(root):
    while(root.left!=None):
        root=root.left
    return root.val
def deletenode(root,a):
    if(a<root.val):
        root.left=deletenode(root.left,a)
    elif(a>root.val):
        root.right=deletenode(root.right,a)
    else:
        if(root.left==None):
            return root.right
        elif root.right==None:
            return root.left
        else:
            b=findmin(root.right)
            root.val=b
            root.right=deletenode(root.right,b)
    return root
def display(root):
    l=[root]
    print(root.val,end=' ')
    while(l!=[]):
        b=l.pop(0)
        if(b.left): 
            print(b.left.val,end=' ')
            l.append(b.left)
        if(b.right):
            print(b.right.val,end=' ')
            l.append(b.right)
m=input()
m=m.split(' ')
print(m)
root=None
for i in m:
    root=insert(root,int(i))
root=deletenode(root,2)
display(root)
