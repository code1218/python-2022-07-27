dan = 0

while dan < 8:
    dan = dan + 2
    num = 0
    print(f"{dan}단")
    while num < 9:
        num = num + 1
        print(f"{dan} x {num} = {dan * num}")

    print()
    dan = dan - 1