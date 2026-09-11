class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes:list[int] = [hash(tuple(sorted(word))) for word in strs]
        groups:dict[int, list[str]] = {} # TODO(bader): turn into an ordered dict (fifo)
                
        for i in range(len(hashes)):
            if hashes[i] in groups:
                groups[hashes[i]].append(strs[i])
            else:
                groups[hashes[i]] = [strs[i],]

        return list(groups.values())



    def anagrams(self, s:str, t:str) -> bool:
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
