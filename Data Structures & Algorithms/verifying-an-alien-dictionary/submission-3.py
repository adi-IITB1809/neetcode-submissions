class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        position = {}
        
        for i in range(len(order)):
            position[order[i]] = i
        
        
        # Compare every consecutive pair of words
        for i in range(len(words) - 1):
            
            word1 = words[i]
            word2 = words[i + 1]
        
            for j in range(min(len(word1), len(word2))):
                
                # If characters are different
                if word1[j] != word2[j]:
                    if position[word1[j]] > position[word2[j]]:
                        return False
                    
                    else:
                        break
            

            else:
                if len(word1) > len(word2):
                    return False
        
        return True