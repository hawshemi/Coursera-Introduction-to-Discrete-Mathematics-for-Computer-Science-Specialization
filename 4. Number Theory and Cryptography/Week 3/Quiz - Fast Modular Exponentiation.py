# First Question
def FastModularExponentiation(b, k, m):
    # Initialize result to b mod m
    result = b % m
    # Compute b^2 mod m, b^4 mod m, b^8 mod m, ..., b^(2^k) mod m
    for i in range(k):
        # Square the result modulo m
        result = (result * result) % m
    return result


# Second Question
def FastModularExponentiation(b, e, m):
    # Initialize result to 1 mod m
    result = 1
    # Compute b^1 mod m, b^2 mod m, b^4 mod m, ..., b^(2^k) mod m
    while e > 0:
        # If the current bit of e is 1, multiply the result by b modulo m
        if e % 2 == 1:
            result = (result * b) % m
        # Square the base modulo m
        b = (b * b) % m
        # Divide the exponent by 2
        e //= 2
    return result
