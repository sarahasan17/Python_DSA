class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insert_val_to_node(str1):
    str1=str1.split(' ')
    root=node(int(str1[0]))
    l=[root]
    i=1 
    while(l):
        node1=l.pop(0)
        if(i<len(str1) and str1[i]!="null"):
            node1.left=node(int(str1[i]))
            l.append(node1.left)
        i+=1 
        if(i<len(str1) and str1[i]!="null"):
            node1.right=node(int(str1[i]))
            l.append(node1.right)
        i+=1 
    return root
def make_comp(root1,root2):
    def leaf_nodes(root,l1):
        if not root:
            return
        elif not root.left and not root.right:
            l1.append(root.val)
        leaf_nodes(root.left,l1)
        leaf_nodes(root.right,l1)
    l1=[]
    l2=[]
    leaf_nodes(root1,l1)
    leaf_nodes(root2,l2)
    return l1==l2
r1=input()
r2=input()
root1=insert_val_to_node(r1)
root2=insert_val_to_node(r2)
print(make_comp(root1,root2))

        
            
        
        
            
            
