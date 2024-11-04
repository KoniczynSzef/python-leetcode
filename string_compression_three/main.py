class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return "1" + word

        compressed = ""

        current_letter = word[0]
        current_letter_length = 0

        for char in word:
            if current_letter == char:
                if current_letter_length == 9:
                    compressed += "9" + current_letter
                    current_letter_length = 1
                else:
                    current_letter_length += 1

            else:
                compressed += str(current_letter_length) + current_letter
                current_letter_length = 1
                current_letter = char

        if len(compressed) == 0:
            return str(current_letter_length) + current_letter

        # First if -> abcde => add 1e
        # Second if -> cccccccccc => add 1c
        if compressed[len(compressed) - 1] != current_letter or (compressed[len(compressed) - 1] == current_letter and compressed[len(compressed) - 1]):
            return compressed + str(current_letter_length) + current_letter

        return compressed

solution = Solution()

print(solution.compressedString("abcde"))
print(solution.compressedString("aaaaaaaaaaaaaabb"))
print(solution.compressedString("cccccccccc"))
