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
    
def display(root):
    if root==None:
        return
    print(root.val,end=' ')
    display(root.left)
    display(root.right)
n=input()
n=n.split(' ')
root=node(int(n[0]))
for i in range(1,len(n)):
    root=binary_tree(root,int(n[i]))
data=search_val(root,2)
if(data!=None):
    display(data)
else:
    print("Null")

    
    
    
    
        
    
