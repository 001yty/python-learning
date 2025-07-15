class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack

def main():
    solution = Solution()
    print(solution.isValid("({{)}}"))

if __name__ == "__main__":
    main()