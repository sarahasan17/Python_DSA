from collections import defaultdict

def funword(s,dic,val):
    if s in val: return val[s]
    res=[]
    if dic[s]==1: res=[s]
    for i in range(1,len(s)):
        if(s[:i] in dic): 
            a=funword(s[i:],dic,val)
            for j in a: res.append(s[:i]+" "+j)
    val[s]=res
    return res
def final(s,dic2):
    l=defaultdict(lambda:0)
    for i in dic2: l[i]=1
    return funword(s,l,{})
s=input()
dic3=input()
dic3=dic3.split(' ')
m=final(s,dic3)
