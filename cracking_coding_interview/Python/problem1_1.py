
# import numpy as np
# Assume the string is 
# input_string = "hello_world"
"""
input_string = "abcdefg"

# Assume there are N elements

class Solution:
	def is_unique(self,input_string):
		N = 256
		if len(input_string>N):
			return False
		flag = [0]*N

		for i in range(0, len(input_string)):
			if flag[ord(input_string[i])] == 1:
				return False
			else:
				flag[ord(input_string[i])] = 1

		return True


s = Solution()
print(s.is_unique(input_string))
"""

# O(N)
import unittest


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()