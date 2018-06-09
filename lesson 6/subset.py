class subset:

    def __init__(self, input_list):

        result = []
        a = input_list    
        b = a
        for n in range(len(a)-1):
            for i in b:
                for j in b:
                    if b.index(j) > b.index(i):
                        if n == 0:
                            result.append(list(set([i,j])))
                        elif list(set(i + j)) not in result and list(set(i + j)) != a:
                            result.append(list(set(i + j)))
            b = result    
            if n == len(a)-2:
                for i in a:
                    result.append([i])
                result.append([])
        print(result)

sub = subset([1, 2, 3, 4, 5])
