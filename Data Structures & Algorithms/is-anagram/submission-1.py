class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_contains = {}
        t_contains = {}
        
        for i in range(len(s)):
            if s[i] not in s_contains:
                s_contains[s[i]] = 1
            elif s[i] in s_contains:
                s_contains[s[i]] += 1

            if t[i] not in t_contains:
                t_contains[t[i]] = 1
            elif t[i] in t_contains:
                t_contains[t[i]] += 1

        return s_contains == t_contains


            