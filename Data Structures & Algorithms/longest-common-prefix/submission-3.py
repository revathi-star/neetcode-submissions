class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_word = min(strs,key=len)
        for _ in range(len(min_len_word)):
            for word in strs:
                if not word.startswith(min_len_word):
                    min_len_word=min_len_word[:-1]
        return min_len_word