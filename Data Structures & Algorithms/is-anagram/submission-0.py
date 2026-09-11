class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1_letter_frequency: dict[str, int] = {}
        word2_letter_frequency: dict[str, int] = {}

        for letter in s:
            if letter in word1_letter_frequency:
                word1_letter_frequency[letter] += 1
            else:
                word1_letter_frequency[letter] = 1

            
        for letter in t:
            if letter in word2_letter_frequency:
                word2_letter_frequency[letter] += 1
            else:
                word2_letter_frequency[letter] = 1
        
        for letter in word1_letter_frequency:
            if not letter in word2_letter_frequency or not word1_letter_frequency[letter] == word2_letter_frequency[letter]:
                return False 
        
        return len(word1_letter_frequency.keys()) == len(word2_letter_frequency.keys())
