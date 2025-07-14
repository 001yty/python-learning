from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # 处理空列表情况
            return ""

        for j in range(len(strs[0])):  # 以第一个字符串为基准
            char = strs[0][j]
            for i in range(1, len(strs)):  # 检查其他字符串
                if j >= len(strs[i]) or strs[i][j] != char:
                    return strs[0][:j]
        return strs[0]


def main():
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
    print(solution.longestCommonPrefix(["a"]))


if __name__ == "__main__":
    main()