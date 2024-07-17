s = input("Enter Input : ")
parenthesis = {'(': ')', '[': ']'}
stack = []
for c in s:
    if c in '([':
        stack.append(c)
    elif c in ')]':
        if stack and parenthesis[stack[-1]] == c:
            stack.pop()
        elif stack == [] or parenthesis[stack[-1]] != c:
            print("Parentheses : Unmatched ! ! !")
            exit()
if stack:
    print("Parentheses : Unmatched ! ! !")
else:
    print("Parentheses : Matched ! ! !")