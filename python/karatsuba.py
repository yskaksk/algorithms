import sys
import math

def devide(a, n):
    first = a // (10 ** n)
    second = a % (10 ** n)
    return int(first), int(second)

def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    n = math.ceil(math.log2(max(len(str(x)), len(str(y)))))
    n = 2 ** (n - 1)
    a, b = devide(x, n)
    c, d = devide(y, n)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a + b, c + d) - ac - bd
    r = int(ac) * (10 ** (2 *n)) + int(ab_cd) * (10 ** n) + int(bd)
    print(f"x = {x}, y = {y}")
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")
    print(f"")
    return r

def main():
    args = sys.argv
    r = karatsuba(int(args[1]), int(args[2]))
    print(r)


if __name__ == "__main__":
    main()
