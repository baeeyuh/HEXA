import random
import time
from fastbit import fastbit_radix_sort, scale_to_ints, revert_to_floats
from hex import fastbit_radix_sort_hex
from radix import radix_sort

def compare_sorts():
    # Scale factor to convert float to int (6 decimal places)
    scale_factor = 10**6

    # Generate a random dataset of 10,000 floating-point numbers
    data = [random.uniform(0, 100000) for _ in range(10000)]
    
    # Convert floating-point numbers to integers
    data_for_fastbit = scale_to_ints(data, scale_factor)
    data_for_radix = data_for_fastbit[:]
    data_for_fastbit_hex = data_for_fastbit[:]

    # Original Fastbit Radix Sort
    start_time = time.time()
    max_bit_position = 1 << (max(data_for_fastbit).bit_length() - 1)
    fastbit_radix_sort(data_for_fastbit, 0, len(data_for_fastbit) - 1, max_bit_position)
    fastbit_time = time.time() - start_time
    data_for_fastbit = revert_to_floats(data_for_fastbit, scale_factor)
    
    # Hexadecimal Fastbit Radix Sort
    start_time = time.time()
    max_bit_position = 1 << (max(data_for_fastbit_hex).bit_length() - 1)
    fastbit_radix_sort_hex(data_for_fastbit_hex, 0, len(data_for_fastbit_hex) - 1, max_bit_position)
    fastbit_hex_time = time.time() - start_time
    data_for_fastbit_hex = revert_to_floats(data_for_fastbit_hex, scale_factor)

    # Standard Radix Sort
    start_time = time.time()
    radix_sort(data_for_radix)
    radix_time = time.time() - start_time
    data_for_radix = revert_to_floats(data_for_radix, scale_factor)
    
    # Results
    print(f"Original Fastbit Radix Sort Time: {fastbit_time:.5f} seconds")
    print(f"Hexadecimal Fastbit Radix Sort Time: {fastbit_hex_time:.5f} seconds")
    print(f"Standard Radix Sort Time: {radix_time:.5f} seconds")
    print("Original Fastbit Sort is correct:", data_for_fastbit == sorted(data))
    print("Hexadecimal Fastbit Sort is correct:", data_for_fastbit_hex == sorted(data))
    print("Standard Radix Sort is correct:", data_for_radix == sorted(data))

# Run the comparison
compare_sorts()
