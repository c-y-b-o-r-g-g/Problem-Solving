class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = []
        for letter in magazine:
            mag.append(letter)
        mag.sort()

        for letter in ransomNote:
            if letter not in mag:
                return False
            mag.remove(letter)
        return True


    print(canConstruct(0,"a","b"))