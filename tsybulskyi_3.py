def print_all_even(from_num = 1000, to_num = 3000):
	even_number_list = []
	for i in range(from_num, to_num+1):
		all_even = True
		for d in str(i):
			if int(d)%2 != 0:
				all_even = False
				break
		if all_even:
			even_number_list.append(i)
	return even_number_list

def print_list_format(l):
	for i in l:
		print(i, end = '; ')
	print()

print_list_format(print_all_even())