def fastbit_radix_sort_hex(data, lb, ub, bit_position):
    if bit_position == 0:
        return
    
    for i in range(16):
        startptr = lb
        endptr = ub
        while startptr <= endptr:
            if (data[startptr] & bit_position) >> (bit_position.bit_length() - 4) < i:
                startptr += 1
            elif (data[endptr] & bit_position) >> (bit_position.bit_length() - 4) > i:
                endptr -= 1
            else:
                data[startptr], data[endptr] = data[endptr], data[startptr]
                startptr += 1
                endptr -= 1

    if (startptr - 1) - lb == 1:
        if data[lb] > data[startptr - 1]:
            data[lb], data[startptr - 1] = data[startptr - 1], data[lb]
    else:
        fastbit_radix_sort_hex(data, lb, startptr - 1, bit_position >> 4)

    if (ub - startptr) == 1:
        if data[startptr] > data[ub]:
            data[startptr], data[ub] = data[ub], data[startptr]
    else:
        fastbit_radix_sort_hex(data, startptr, ub, bit_position >> 4)
