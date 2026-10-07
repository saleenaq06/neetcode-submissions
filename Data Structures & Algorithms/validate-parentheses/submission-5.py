class Solution:
    def isValid(self, s: str) -> bool:
        seen_stack = []
        map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in map:
                if seen_stack == []:
                    return False
                prev_char = seen_stack.pop()
                if map[char] != prev_char:
                    return False
            else:
                seen_stack.append(char)
        
        if seen_stack == []:
            return True
        return False