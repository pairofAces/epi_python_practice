# Create a program to count the number of bits tha are set to 1 in a nonnegative integer

def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

# Time complexity:
    # Since the program is performing O(1) computation per bit, the time complexity
    # is O(n), where (n) is the number of bits required to represent an integer
