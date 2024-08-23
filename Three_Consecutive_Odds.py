class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        # [1,2,34,3,4,5,7,23,12]
        for i in range(0, len(arr)):
            if arr[i] % 2 !=0:
                try:
                    if arr[i+1] %2 !=0 and arr[i+2] %2 !=0:
                        return True
                except IndexError:
                    return False
        return False
    
    
    print(threeConsecutiveOdds(0,[2,6,4,1]))