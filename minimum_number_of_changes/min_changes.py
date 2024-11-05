class Solution:
    def minChanges(self, s: str):
        if len(s) == 2:
            return 0 if s[0] == s[1] else 1

        total_changes = int(len(s) / 2)

        for i in range(0, len(s), 2):
            if s[i] == s[i + 1]:
                total_changes -= 1

        return total_changes

solution = Solution()

print(solution.minChanges("10"))
print(solution.minChanges("1001"))
print(solution.minChanges("0000"))
print(solution.minChanges("11000111"))