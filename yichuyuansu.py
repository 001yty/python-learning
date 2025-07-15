from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack_size = 0
        for x in nums:
            if x != val:
                nums[stack_size] = x  # 把 x 入栈
                stack_size += 1
        return stack_size

def main():
    solution = Solution()
    print(solution.removeElement([0,1,2,2,3,0,4,2],2))

if __name__ == "__main__":
    main()