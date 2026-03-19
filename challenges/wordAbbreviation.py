"""
Sometimes, certain words like optimization or kubernetes are so lengthy that writing them repeatedly in a single text becomes quite tedious.

Let’s define a word as too long if its length is strictly greater than 7 characters. All such words should be replaced with a special abbreviation.

The abbreviation is created as follows:
Write the first and last letter of the word, and between them, insert the number of letters that appear between the first and last letters. This number is written in decimal format and should not contain any leading zeros.

Your task is to automate the process of abbreviating words. Replace all too long words with their abbreviations, while leaving shorter words unchanged.

Example 1
Input:
optimization
Output:
o10n
Example 2
Input:
kubernetes
Output:
k8s
Example 3
Input:
word
Output:
w
"""


class Solution(object):
    def solve(self, s: str) -> str:
        print(f"s: {s}")
        if len(s) > 7:
            return f"{s[0]}{len(s[1:-1])}{s[-1]}"
        return s
