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

def max_sum_of_path(root,targetsum):
    def dfs(root,targetsum):
        if not root:
            return 0
        countie=1 if root.val==targetsum else 0
        count_left=dfs(root.left,targetsum-root.val)
        count_right=dfs(root.right,targetsum-root.val)
        return countie+count_left+count_right
    if not root:
        return 0
    totalpath=dfs(root,targetsum)
    totalpath+=max_sum_of_path(root.left,targetsum)
    totalpath+=max_sum_of_path(root.right,targetsum)
    return totalpath
    
r1=input()
root=insert_val(r1)
print(max_sum_of_path(root,3))
            
            
            
            
