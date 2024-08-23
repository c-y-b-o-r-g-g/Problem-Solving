class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000

        }
        if "IV" in s:
            sum += 4
            s = s.replace("IV", '')
            # s= s.removesuffix("IV")
        if "IX" in s:
            sum += 9
            # s= s.removesuffix("IX")
            s = s.replace("IX", '')
        if "XL" in s:
            sum += 40
            # s= s.removesuffix("XL")
            s = s.replace("XL", '')
        if "XC" in s:
            sum += 90
            # s = s.removesuffix("XC")
            s = s.replace("XC", '')
        if "CD" in s:
            sum += 400
            # s= s.removesuffix("CD")
            s = s.replace("CD", '')
        if "CM" in s:
            sum += 900
            # s= s.removesuffix("CM")
            s = s.replace("CM", '')

        # print(s)
        for letter in s:
            if letter != ' ':
                # print(letter)
                # print(romans.get(letter)) 
                sum += romans.get(letter)
        return sum

    print(romanToInt(0, "MCMXCIV"))
