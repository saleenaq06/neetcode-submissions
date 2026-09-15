class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letters = {}
        t_letters = {}

        for char in s:
            if char in s_letters:
                s_letters[char] += 1
            else:
                s_letters[char] = 1
        
        for char in t:
            if char in t_letters:
                t_letters[char] += 1
            else:
                t_letters[char] = 1

        for key in s_letters:
            if key not in t_letters:
                return False
            if t_letters[key] != s_letters[key]:
                return False
            
        return True
        