class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs,key=len)
        for each_word in strs:
            for word_index in range(len(each_word)):
                if word_index in range(len(word)):
                    if word[word_index]!=each_word[word_index]:
                        word=word[:word_index]
        return word