class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        import string
        alphas = string.ascii_lowercase
        wordbook = {}
        letterbook = []
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        i = 0
        
        # wordbook[alphas[i]] = "gehad"
        for word in words:
            if word not in wordbook.values():
                wordbook[alphas[i]] = word,words.index(word)
                
                i+=1
                
        for letter in pattern:
            
        # for key in wordbook.keys():
        #     print(key)
        #     print(wordbook[key])
        
        
        
        


   
    
sol  = Solution()
sol.wordPattern(pattern = "abba", s = "dog cat cat dog")