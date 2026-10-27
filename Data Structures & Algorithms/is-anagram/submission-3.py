class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        a=dict()
        b=dict()
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        for i in t:
            if i not in b:
                b[i]=1
            else:
                b[i]+=1
        for i in a.keys():
            if i not in b.keys():
                return False
            if a[i]!=b[i]:
                return False
        return True
        
