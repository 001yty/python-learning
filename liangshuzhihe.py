
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, num in enumerate(nums):
            chazhi = target - num
            if chazhi in dic:
                return [dic[chazhi], index]
            dic[num] = index

def main():
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9));

if __name__ == "__main__":
    main()