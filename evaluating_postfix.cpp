def evaluation_postfix(word):
    n=len(word)
    l=[]
    for i in range(0,len(word)):
        if(word[i]>='0' and word[i]<='9'):
            l.append(int(word[i]))
        else:
            r1=l[len(l)-1]
            l.pop()
            r2=l[len(l)-1]
            l.pop()
            if(word[i]=='+'):
                res=r1+r2
            elif(word[i]=='-'):
                res=r1-r2
            elif(word[i]=='*'):
                res=r1*r2
            elif(word[i]=='/'):
                res=r1/r2
            l.append(res)
    return l[len(l)-1]
m="231*+9-"
print(evaluation_postfix(m))

            
                
            
            
        
