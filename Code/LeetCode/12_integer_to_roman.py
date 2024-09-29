class Solution:
    def intToRoman(self, num: int) -> str:
        romanHash = {
            "1": "I",
            "4": "IV",
            "5": "V",
            "9": "IX",
            "10": "X",
            "40": "XL",
            "50": "L",
            "90": "XC",
            "100": "C",
            "400": "CD",
            "500": "D",
            "900": "CM",
            "1000": "M",
        }
        num = str(num)
        roman = ""
        for i in range(len(num)):
            zeros = '0' * (len(num) - i - 1)
            sub_number = num[i] + zeros
            int_sub_number = int(sub_number[0])
            
            if int_sub_number != 0:
                if len(sub_number) == 4:
                    roman += romanHash["1000"] * int_sub_number
                else:
                    if 5 < int_sub_number < 9:
                        roman +=  romanHash["5" + zeros] + romanHash["1" + zeros] * (int_sub_number - 5)
                    elif 1 < int_sub_number < 4: 
                        roman +=  romanHash["1" + zeros] * int_sub_number
                    else:
                        roman += romanHash[sub_number]
        return roman
        


s = Solution()


ans = s.intToRoman(1994)
print(ans)