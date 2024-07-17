print("*** Fun with Drawing ***")
x = int(input("Enter input : "))

for i in range(x*4-3):
    for j in range(x*4-3):
        for k in range(x*4-3):
            if i == k or j == k or i == x*4-4-k or j == x*4-4-k:
                if k % 2 == 0:
                    print("#", end="")
                elif k % 2 == 1:
                    print(".", end="")
                break
    print("")