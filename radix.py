def radix_sort(data):
    max_val = max(data)
    exp = 1
    while max_val // exp > 0:
        counting_sort(data, exp)
        exp *= 10

def counting_sort(data, exp):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = data[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = data[i] // exp
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1

    for i in range(n):
        data[i] = output[i]
