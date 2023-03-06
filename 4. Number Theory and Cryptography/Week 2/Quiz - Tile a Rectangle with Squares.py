# fix this code

def gcd(a, b):
    if a == 0 :
        return b
    return gcd(b%a, a)

def squares(n, m):
    return (n * m) // (gcd(n, m)**2)