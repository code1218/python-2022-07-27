# lambda(람다)함수

"""
    javascript
    (a, b) => {
        return a + b;
    }

    java (a, b) -> {
        return a + b;
    }
"""

def test(a, b):
    return f"a({a}) + b({b}) = {a + b}"

test2 = lambda a, b: f"a({a}) + b({b}) = {a + b}"

if __name__ == "__main__":
    result = test(10, 20)
    print(result)
    print(test2(20, 30))









