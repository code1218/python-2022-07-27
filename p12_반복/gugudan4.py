
for dan in range(2, 10):
    print(f"{dan}단", end="\t")
    for num in range(1, 10):
        print(f"{dan} x {num} = {dan * num}", end="\t")
    print()