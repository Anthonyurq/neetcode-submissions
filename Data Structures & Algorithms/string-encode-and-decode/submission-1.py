class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            for char in word:
                string += char 
            string += "€"

        return string

    

    def decode(self, s: str) -> List[str]:
        result = []
        curWord = ""
        for letter in s:
            if letter == "€":
                result.append(curWord)
                curWord = ""
            else:
                curWord += letter

        return result
