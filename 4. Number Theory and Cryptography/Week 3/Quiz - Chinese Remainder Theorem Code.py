def ChineseRemainderTheorem(n1, r1, n2, r2):
    # Compute the gcd of n1 and n2
    (x, y) = ExtendedEuclid(n1, n2)
    if x*n1 + y*n2 != 1:
        # n1 and n2 are not coprime, so the problem has no solution
        return None
    # Compute the solution modulo n1*n2
    return (r1*n2*y + r2*n1*x) % (n1*n2)
