class zero_sum:

    def __init__(self, input_list):
        seq = input_list
        result = []
        for combination in itertools.combinations(seq, 3):
            if sum(combination) == 0 and list(combination) not in result:
                result.append(list(combination))
        print(result)

a = zero_sum([-25, -9, -7, -3, 2, 1, 8, 10])
