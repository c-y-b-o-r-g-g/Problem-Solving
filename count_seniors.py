class Solution:
    def countSeniors(self, details: list[str]) -> int:
        
        counter=0
        for person in details:
            if(int(person[11])) > 6:
                counter+=1
            elif(int(person[11]))==6:
                if(int(person[12]))>0:
                    counter+=1
        return counter
    
    
sol = Solution()
res = sol.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"])
print(res)