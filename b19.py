def to_base19(n):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHI"
    base19 = ""
    while n > 0:
        base19 = digits[n % 19] + base19
        n //= 19
    return base19

print(to_base19(100)) 