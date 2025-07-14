class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if len(s)==1:
            return True
        if len(s)==2:
            if s[0]==s[1]:
                return True
            else:
                return False
        if len(s)!=1 and len(s)!=2:
            for i in range(len(s)):
                if s[i]==s[len(s)-i-1]:
                    i=i+1
                if s[i]!=s[len(s)-i-1]:
                    return False
                    break
                if(i>len(s)/2):
                    return True

def main():
    solution = Solution()
    print(solution.isPalindrome(11));

if __name__ == "__main__":
    main()


