def fastbit_radix_sort(data, lb, ub, bit_position):
    if bit_position == 0:
        return
    
    startptr = lb
    endptr = ub
    
    while startptr < endptr:
        if (data[startptr] & bit_position) < (data[endptr] & bit_position):
            startptr += 1
            endptr -= 1
        elif (data[startptr] & bit_position) > (data[endptr] & bit_position):
            data[startptr], data[endptr] = data[endptr], data[startptr]
            startptr += 1
            endptr -= 1
        else:
            if (data[startptr] & bit_position) == 0:
                startptr += 1
            else:
                endptr -= 1

    if (startptr - 1) - lb == 1:
        if data[lb] > data[startptr - 1]:
            data[lb], data[startptr - 1] = data[startptr - 1], data[lb]
    else:
        fastbit_radix_sort(data, lb, startptr - 1, bit_position >> 1)

    if (ub - startptr) == 1:
        if data[startptr] > data[ub]:
            data[startptr], data[ub] = data[ub], data[startptr]
    else:
        fastbit_radix_sort(data, startptr, ub, bit_position >> 1)

# Helper function to scale floats to integers and revert them after sorting
def scale_to_ints(data, scale_factor):
    return [int(x * scale_factor) for x in data]

def revert_to_floats(data, scale_factor):
    return [x / scale_factor for x in data]
