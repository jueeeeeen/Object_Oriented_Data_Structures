print("*** Fun with Drawing ***")
n = int(input("Enter input : "))

for i in range(1, (n*3-1)):
    if i <= n:
        if i == 1:
            print(f"{'.' * (n-i)}*{'.' * (2*(n-i)-1)}*{'.' * (n-i)}")
        elif i == n:
            print(f"*{'+' * (2*i-3)}*{'+' * (2*i-3)}*")
        else:
            print(f"{'.' * (n-i)}*{'+' * (2*i-3)}*{'.' * (2*(n-i)-1)}*{'+' * (2*i-3)}*{'.' * (n-i)}")
    else:
        if i == n*3-2:
            print(f"{'.' * (2*n-2)}*{'.' * (2*n-2)}")
        else:
            print(f"{'.' * (i-n)}*{'+' * ((6*n)-5-(2*i))}*{'.' * (i-n)}")