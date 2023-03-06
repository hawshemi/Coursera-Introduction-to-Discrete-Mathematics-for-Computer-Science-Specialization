def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)

    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (gcd, x, y)


def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1

    _, a_inv, _ = extended_gcd(a, n)
    x = (b * a_inv) % n
    return x
