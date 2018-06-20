d = {'a': 1, 'b': 2, 'c': 3}

def check(x):
    if x in d :
        print('the key is in the dictionary ')
    else:
        print('the key is not in the dictionary')

check(1)
check('a')