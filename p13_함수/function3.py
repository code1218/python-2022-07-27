def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    num3 = 2

    print(f"{num1}, {num2} 덧셈: {add(num1, num2)}")
    print(f"{num1}, {num2} 덧셈2: {add(num1, num2, num3)}")
    print(f"{num1}, {num2} 뺄셈: {sub(num1, num2)}")
    print(f"{num1}, {num2} 곱셈: {mul(num1, num2)}")
    print(f"{num1}, {num2} 나눗셈: {div(num1, num2)}")

