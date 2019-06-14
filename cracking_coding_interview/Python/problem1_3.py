

input_string = "Mr John Smith    "

true_length = 13

# How many additional charactiers are needed

class Solution:
	def new_string(self, input_string, true_length):
		cnt_space = 0
		for i in range(0, true_length):
			if input_string[i] == " ":
				cnt_space += 1

		index = true_length + cnt_space*2

		for i in range(true_length, 0, -1):
			if input_string[true_length] == ' ':
				# print(input_string)
				input_string[index-3:index] = '%20'
				#input_string[index-1] = '2'
				#input_string[index-2] = '%'
				index -= 3

			else:
				input_string[index] = input_string[i]
				index -= 1
		sss = ''.join(input_string)
		return sss


s = Solution()
print(s.new_string(list(input_string), true_length))
"""

# O(N)
import unittest


def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            print(string)
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
"""