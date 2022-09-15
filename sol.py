from string import ascii_lowercase

def solution(x):
	res = ""
	hash = ""

	i = -1
	while (len(ascii_lowercase) >= abs(i)):
		hash += ascii_lowercase[i]

		i -= 1
	
	for n in x:
		index = hash.find(n)
		if (index >= 0):
			res += ascii_lowercase[index]
		else:
			res += n

	print(res)
	return res


if __name__ == '__main__':
	solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")