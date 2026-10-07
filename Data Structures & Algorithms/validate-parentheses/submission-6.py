class Solution:
    def isValid(self, s: str) -> bool:
        seen_stack = []
        map = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in map:
                seen_stack.append(char)
            if char in map.values():
                if seen_stack == []:
                    return False
                prev_char = seen_stack.pop()
                if prev_char == '(' and char == ')':
                    continue
                elif prev_char == '{' and char == '}':
                    continue
                elif prev_char == '[' and char == ']':
                    continue
                else:
                    return False
        if seen_stack == []:
            return True
        return False    


        