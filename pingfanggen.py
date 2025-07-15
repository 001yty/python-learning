class Solution:
    def mySqrt(self, x: int) -> int:
        a=0
        for i in range(0,x+1):
            if a**2<x:
                a=a+1
            if a**2==x:
                return a
            if a**2>x:
                return a-1

def main():
    solution = Solution()
    print(solution.mySqrt(8))

if __name__ == "__main__":
    main()