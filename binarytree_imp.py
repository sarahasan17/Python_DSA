class binarytree:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
    def insert(self,val):
        if(self.val):
            if val<self.val:
                if self.left is None:
                    self.left=binarytree(val)
                else:
                    self.left.insert(val)
            elif val>self.val:
                if self.right is None:
                    self.right=binarytree(val)
                else:
                    self.right.insert(val)
        else:
            self.val=val
    def printval(self):
        if(self.left):
            self.left.printval()
        print(self.val,end=' ')
        if(self.right):
            self.right.printval()
    def prefix(self):
        print(self.val,end=' ')
        if(self.left):
            self.left.printval()
        if(self.right):
            self.right.printval()
    def postfix(self):
        if(self.left):
            self.left.printval()
        if(self.right):
            self.right.printval()
        print(self.val,end=' ')
        
root = binarytree(12)
root.insert(6)
root.insert(14)
root.insert(3)
print("Infix")
root.printval()
print()
print("Prefix")
root.prefix()
print()
print("Postfix:")
root.postfix()
        
                    
