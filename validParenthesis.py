class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "]": "[", "}":"{"}
        stack = []
        for element in s:
            if element in closeToOpen:
                if len(stack) == 0:
                    return False
                openingValue = stack.pop()
                return True if openingValue == closeToOpen[element] else False
            else:
                stack.append(element)
        return False if len(stack) > 0 else True

# time complexity = O(n)
# space complexity = O(n)