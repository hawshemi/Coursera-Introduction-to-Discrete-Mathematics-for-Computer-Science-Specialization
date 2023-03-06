def lcm(a, b):
    assert a > 0 and b > 0
  
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b%a, a)
    return a * b // gcd(a, b)
