class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def XOR (a, b):
            if a != b:
                return 1
            else:
                return 0
            
        def AND (a, b):
            if a == 1 and b == 1:
                return True
            else:
                return False
            
        def OR(a, b):
            if a == 1 or b ==1:
                return True
            else:
                return False
            
        if(len(a) < len(b)):
            a,b = b,a
        b = b.zfill(len(a))
        res = ""
        carry = 0
        for i in range(len(a) -1 , -1, -1):
            temp = XOR(int(a[i]), int(b[i]))
            res = str(XOR(temp , carry))+ res
            # =============================
            temp2 = AND(temp,carry)
            temp3 = AND(int(a[i]), int(b[i]))
            carry = OR(temp2,temp3)
            
            
            
            
        
        if carry:
            res = '1' + res
        return res
        
        
sol = Solution()
result = sol.addBinary("1", "0")
print(result)