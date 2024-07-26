class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        import itertools

        key_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        digits_to_letters = list()

        for digit in digits:
            digits_to_letters.append(key_dict.get(digit, ""))

        if len(digits_to_letters) == 1:
            return [i for i in digits_to_letters[0]]

        elif digits_to_letters == []:
            return digits_to_letters

        else:
            split_list = [[i for i in i] for i in digits_to_letters]

            args = (i for i in split_list)

            return ["".join(i) for i in list(itertools.product(*args))]
