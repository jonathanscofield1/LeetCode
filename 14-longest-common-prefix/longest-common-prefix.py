class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:

            return strs[0]

        else:

            first_word = strs[0]

            other_words = strs[1:]

            substrings = [first_word[:x] for x in range(1, len(first_word) + 1)]

            prefixes = list()

            for substring in substrings[::-1]:
                for word in other_words:
                    if substring in word and word.startswith(substring):
                        prefixes.append(substring)

            common_prefixes = [
                prefix
                for prefix in prefixes
                if prefixes.count(prefix) == len(other_words)
            ]

            if len(common_prefixes) == 0:
                return ""
            else:
                return common_prefixes[0]
