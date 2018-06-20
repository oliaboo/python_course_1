L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print(L)
u_values = []
for i in L:
    u_values += (i.values())
u_values = set(u_values)
print(u_values)
