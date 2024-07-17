def ManageStack(list):
    stack = []
    for item in list:
        if not stack and item[0] !="A":
            print("-1")
        else:
            if item == "P":
                print(f"Pop = {stack.pop()}")
            elif item[0] =="A":
                stack.append(int(item[2:]))
                print(f"Add = {int(item[2:])}")
            elif item[0] == "D":
                temp_stack = []
                for num in stack:
                    if num != int(item[2:]):
                        temp_stack.append(num)
                    else:
                        print(f"Delete = {int(item[2:])}")
                stack = temp_stack
            elif item[:2] =="LD":
                temp_stack = []
                for num in stack[::-1]:
                    if num >= int(item[3:]):
                        temp_stack.append(num)
                    else:
                        print(f"Delete = {num} Because {num} is less than {int(item[3:])}")
                stack = temp_stack[::-1]
            elif item[:2] =="MD":
                temp_stack = []
                for num in stack[::-1]:
                    if num <= int(item[3:]):
                        temp_stack.append(num)
                    else:
                        print(f"Delete = {num} Because {num} is more than {int(item[3:])}")
                stack = temp_stack[::-1]
    return "Value in Stack = " + str(stack)

list = input("Enter Input : ").split(",")
print(ManageStack(list))