number = int(input('Number of lucky numbers: '))

a = [i for i in range(1,100000)]

for i in range(number):
    if i == 0:
        del a[1::2]
    else:
        del a[a[i]-1::a[i]]
    print(a[i])
