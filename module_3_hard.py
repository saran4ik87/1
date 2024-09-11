def calculate_structure_sum(data):
    sum = 0
    if isinstance(data, dict):
        d_data = list(data.items())
    else:
        d_data = data
    for d in d_data:
        if isinstance(d, int):
            sum += d
        elif isinstance(d, str):
            sum += len(d)
        else:
            sum += calculate_structure_sum(d)
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)
