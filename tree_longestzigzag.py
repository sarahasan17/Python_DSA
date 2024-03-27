class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insert_val(str):
    str=str.split(' ')
    root=node(int(str[0]))
    l=[root]
    i=1
    while l:
        node1=l.pop(0)
        if(i<len(str) and str[i]!="null"):
            node1.left=node(int(str[i]))
            l.append(node1.left)
        i+=1 
        if(i<len(str) and str[i]!="null"):
            node1.right=node(int(str[i]))
            l.append(node1.right)
        i+=1 
    return root

def zigzag(root):
    if not root:
        return 0
    max_val=[0]
    def traverse(root,dir,len):
        max_val[0]=max(max_val[0],len)
        if(dir=='left' and root.right):
            traverse(root.right,'right',len+1)
        elif(dir=='right' and root.left):
            traverse(root.left,'left',len+1)
    traverse(root,'left',0)
    traverse(root,'right',0)
    return max_val[0]
    
r1=input()
root=insert_val(r1)
print(zigzag(root))
            
            
            
            
