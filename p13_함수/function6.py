def calc(*args):
    result1 = 0
    result2 = 0
    result3 = 0

    for i in args:
        result1 += i

    result2 += 1
    for i in args:
        result2 *= i

    result3 += 1
    for i in args:
        result3 **= i

    return result1, result2, result3

if __name__ == "__main__":
    a, b, c = calc(1, 2, 3, 4)
    print(calc(1, 2, 3, 4))
    print(f"a: {a}, b: {b}, c: {c}")



