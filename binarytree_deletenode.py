class node:
    def __init__(self,val):
        self.val=val 
        self.left=None
        self.right=None
    
def binary_tree(root,val):
    if root==None:
        root=node(val)
        return root
    if val<root.val:
        root.left=binary_tree(root.left,val)
    else:
        root.right=binary_tree(root.right,val)
    return root
 
  
def search_val(root,data):
    if root==None:
        return
    elif root.val==data:
        return root
    elif root.val>data:
        return search_val(root.left,data)
    return search_val(root.right,data)

def deletenode(root,key):
    if root==None:
        return
    elif key<root.val:
        root.left=deletenode(root.left,key)
    elif key>root.val:
        root.right=deletenode(root.right,key)
    else:
        if(root.left==None):
            return root.right
        if root.right==None:
            return root.left
        else:
            m.val=findmin(root.right)
            root.val=m.vzl
            root.right=deletenode(root.right,m.val)
    return root
def findmin(root):
    while(root.left!=None):
        root=root.left
    return root
def display(root):
    l=[root]
    while l:
        level_q=[]
        next_q=[]
        for i in l:
            level_q.append(i.val)
            if(i.left):
                next_q.append(i.left)
            if(i.right):
                next_q.append(i.right)
        print(level_q)
        l=next_q
            
n=input()
n=n.split(' ')
root=node(int(n[0]))
for i in range(1,len(n)):
    root=binary_tree(root,int(n[i]))
root=deletenode(root,2)
if(root!=None):
    display(root)
else:
    print("Null")

    
    
    
    
        
    
