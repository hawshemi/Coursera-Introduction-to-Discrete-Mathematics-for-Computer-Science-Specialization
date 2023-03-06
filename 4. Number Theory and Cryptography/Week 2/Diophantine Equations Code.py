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
        return (1, 0, a)
    else:
        x, y, d = extended_gcd(b, a % b)
        return (y, x - (a // b) * y, d)

def diophantine(a, b, c):
    assert c % gcd(a, b) == 0
    s, t, d = extended_gcd(a // gcd(a, b), b // gcd(a, b))
    x = s * (c // gcd(a, b))
    y = t * (c // gcd(a, b))
    return (x, y)
