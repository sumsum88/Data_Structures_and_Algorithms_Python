import math


def is_prime(n):
    try:
        res = any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))
        return not(res)
    except Exception as e:
        raise


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)


def lcm(a, b):
    """
    最小公倍数
    """
    return a * b / gcd(a,b)


def modinv(a, m):
    m_ = m
    x, lastx, y, lasty = 0, 1, 1, 0
    while m:
        a, (quotient, m) = m, divmod(a, m)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    if a != 1:
        raise ValueError
    return lastx % m_


def combination_mod(m, n, mod):
    """
    mCn % mod
    """
    num, div = 1, 1
    for i in range(min(n, m - n)):
        num *= m - i
        if num > mod:
            num %= mod
        div *= i + 1
        if div > mod:
            div %= mod
    return (num * modinv(div, mod)) % mod