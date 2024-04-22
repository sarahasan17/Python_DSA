import math
class node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
def insert(root,a):
    root=node(int(a[0]))
    n=len(a)
    i=1
    q=[root]
    while q:
        b=q.pop(0)
        if i<n and a[i]!=None:
            b.left=node(int(a[0]))
            q.append(b.left)
        i+=1
        if i<n and a[i]!=None:
            b.right=node(int(a[0]))
            q.append(b.right)
        i+=1
    return root
def height(root,l,lev):
    if(root!=None):
        if(lev==len(l)):
            l.append(root)
        height(root.left,l,lev+1)
        height(root.right,l,lev+1)
a=input()
a=a.split(' ')
root=None
root=insert(root,a)
l=[]
height(root,l,0)
print(len(l))
        
        
        
