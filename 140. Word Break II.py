class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)  # Convert list to set for O(1) lookups
        memo = {}  # Dictionary for memoization

        def backtrack(index):
            if index in memo:
                return memo[index]

            if index == len(s):
                return [""]  # Base case: Return empty string to build sentences

            sentences = []
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in word_set:
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        sentences.append(word + (" " + sentence if sentence else ""))

            memo[index] = sentences
            return sentences

        return backtrack(0)
