class zero_sum:

    def __init__(self, input_list):
        a = input_list
        result = []
        for i in range(len(a)):
            for j in range(len(a)):
                for k in range(len(a)):
                    if j > i:
                        if k > j:
                            if a[i] + a[j] + a[k] == 0:
                                result.append([a[i], a[j], a[k]])
        print(result)

a = zero_sum([-25, -9, -7, -3, 2, 1, 8, 10])
