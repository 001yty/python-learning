from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        number=len(nums)
        a=nums[0]
        num=[nums[0]]
        for i in range(1,len(nums)):

            if nums[i]==a:
                number=number-1
            if nums[i]>a:
                a=nums[i]
                num.append(a)
        nums=num
        return number,nums

def main():
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))


if __name__ == "__main__":
    main()