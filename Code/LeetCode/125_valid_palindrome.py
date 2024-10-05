import re

class Solution:
    #! MY SOLUTION (BAD ASF but WITH REGULAR EXPRESSION MY BOY) 
    # def isPalindrome(self, s: str) -> bool:
    #     if len(s) == 1:
    #         return True

    #     s_lower_case = s.lower()
    #     pattern = r'[^a-zA-Z0-9]'
    #     s_clean = re.sub(pattern, '', s_lower_case)
    #     s_len = len(s_clean)
        
    #     if s_len == 0:
    #         return True
        
    #     isOdd = s_len % 2 != 0
    #     tail = 0
    #     head = s_len - 1
        
    #     if isOdd:
    #         while head != (s_len // 2):
    #             if s_clean[tail] != s_clean[head]:
    #                 return False
    #             tail += 1
    #             head -= 1
    #     else:
    #         while head - tail >= 1:
    #             if s_clean[tail] != s_clean[head]:
    #                 return False
    #             tail += 1
    #             head -= 1
    #     return True
    
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        L = 0
        R = n - 1
        
        while L < R:
            if not s[L].isalnum():
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue
            
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        
        return True
        
s = Solution()

myInput = "A man, a plan, a canal: Panama"

ans = s.isPalindrome(myInput)

print(ans)