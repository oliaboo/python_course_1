def letter_number_count(user_line):
	res = {}
	res['digit'] = 0
	res['alfa'] = 0
	for l in user_line:
		if l.isalpha():
			res['alfa'] += 1
		elif l.isdigit():
			res['digit'] += 1
	return res

user_line = input('Input:\n')
res = letter_number_count(user_line)
print('Output:')
print("LETTERS ", res['alfa'])
print("DIGITS ", res['digit'])
