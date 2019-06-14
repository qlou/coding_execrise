
# str_1 = "instagram"

# str_2 = "margatsni"

str_1 = "instagram"
str_2 = "margrtsni"

class Solution:

	# Implement the first solution, sort two strings
	def check_permutation_1(self, str_1, str_2):
		if len(str_1) != len(str_2):
			return False
		else:
			str_1 = sorted(str_1)
			str_2 = sorted(str_2)
			for i in range(0, len(str_1)):
				if str_1[i] == str_2[i]:
					continue
				else:
					return False
		return True

	def check_permutation_2(self, str_1, str_2):
		if len(str_1) != len(str_2):
			return False
		else:
			dic_1 = {}
			dic_2 = {}
			for i in range(0, len(str_1)):
				if str_1[i] in dic_1.keys():
					dic_1[str_1[i]] += 1
				else:
					dic_1[str_1[i]] = 1

			for i in range(0, len(str_2)):
				if str_2[i] in dic_2.keys():
					dic_2[str_2[i]] += 1
				else:
					dic_2[str_2[i]] = 1

			if dic_2 == dic_1:
				return True
			else:
				return False


s = Solution()
print(s.check_permutation_2(str_1, str_2))