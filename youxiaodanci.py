class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False


        for c in word:
            if c.isalpha():#python自带函数，检查c是否属于字母
                if c.lower() in 'aeiou':
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False
        return has_vowel and has_consonant  # 必须同时有元音和辅音

        return has_vowel and has_consonant
def main():
    solution = Solution()
    print(solution.isValid("234Adas"))

if __name__ == "__main__":
    main()