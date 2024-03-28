class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def insert_ele(str):
    str=str.split(' ')
    root=node(int(str[0]))
    l=[root]
    i=1
    while(l):
        m=l.pop(0)
        if(i<len(str) and str[i]!='null'):
            m.left=node(int(str[i]))
            l.append(m.left)
        i+=1 
        if(i<len(str) and str[i]!='null'):
            m.right=node(int(str[i]))
            l.append(m.right)
        i+=1 
    return root

def max_level_sum(root,lev,l):
    if root==None:
        return
    if(lev==len(l)):
        l.append(root.data)
    else:
        l[lev]+=root.data
    max_level_sum(root.left,lev+1,l)
    max_level_sum(root.right,lev+1,l)
    
n=input()
root=insert_ele(n)
l=[]
leng=0
max_level_sum(root,leng,l)
n=max(l)
print(l.index(n)+1)
            
