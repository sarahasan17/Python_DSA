class Solution(object):
    def asteroidCollision(self, asteroids):
        def signmatch(a,b):
            if(a>0 and b>0):
                return True
            elif a<0 and b<0:
                return True
            return False
        l=[]
        for i in range(0,len(asteroids)):
            m=asteroids[i]
            if(len(l)==0 or (l[-1]<0 and m>0) or (signmatch(m,l[-1]))):
                l.append(m)
            else:
                while(len(l)>0 and l[-1]>0 and l[-1]<abs(m)):
                    l.pop()
                if(len(l)==0 or l[-1]<0):
                    l.append(m)
                elif(l[-1]==abs(m)):
                    l.pop()
        return l
              
