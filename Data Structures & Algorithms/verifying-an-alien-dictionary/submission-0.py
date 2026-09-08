class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # Store each character and its position in the alien dictionary
        position = {}
        
        for i in range(len(order)):
            position[order[i]] = i
        
        
        # Compare every consecutive pair of words
        for i in range(len(words) - 1):
            
            word1 = words[i]
            word2 = words[i + 1]
            
            # Compare characters of both words
            for j in range(min(len(word1), len(word2))):
                
                # If characters are different
                if word1[j] != word2[j]:
                    
                    # Check their order in alien dictionary
                    if position[word1[j]] > position[word2[j]]:
                        return False
                    
                    # Correct order, so stop comparing this pair
                    break
            
            # Special case:
            # "apple" before "app" is invalid
            else:
                if len(word1) > len(word2):
                    return False
        
        return True