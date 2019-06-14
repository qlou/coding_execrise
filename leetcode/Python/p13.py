class Solution:
    def romanToInt(self, s: str) -> int:
        # write a dictionary for the symbol and value
        d = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        m = len(s)
        number = 0
        for i in range(0, m-1):
            if (d[i] == 1 and d[i+1] == 5):
                number = number + d[i+1] - 1
                i=i+1
            elif d[i] == 1 and d[i+1] == 10:
                number = number + d[i+1] - 1
                i=i+1
            elif d[i] == 10 and d[i+1] == 50:
                number = number + d[i+1] - 10
                i=i+1
            elif d[i] == 10 and d[i+1] == 50:
                number = number + d[i+1] - 10
                i=i+1
            elif d[i] == 100 and d[i+1] == 500:
                number = number + d[i+1] - 10
                i=i+1
            elif d[i] == 100 and d[i+1] == 500:
                number = number + d[i+1] - 10
                i=i+1
            else:
                number = number + d[i]

s = Solution()
print(s.romanToInt('IV'))