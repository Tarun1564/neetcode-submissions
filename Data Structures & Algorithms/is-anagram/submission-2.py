class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)==len(t)):
            a=list(s)
            b=list(t)
            if sorted(a)==sorted(b):
                return True
        return False