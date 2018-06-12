def func(arg_pos, **kwargs):
    sum = 0
    sum = sum + arg_pos
    for i in kwargs:
        sum = sum + kwargs[i]
    print(sum)

func(1, a = 5, b = 6)
    
