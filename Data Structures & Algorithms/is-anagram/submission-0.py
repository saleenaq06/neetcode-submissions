class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = []
        t_letters = []

        for char in s:
            s_letters.append(char)
        
        for char in t:
            t_letters.append(char)

        s_letters.sort()
        t_letters.sort()
        if s_letters == t_letters:
            return True
        return False