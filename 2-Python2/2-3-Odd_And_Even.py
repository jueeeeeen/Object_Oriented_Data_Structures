def odd_even(type, data, mode):
    output = ""
    if type == "L":
        data = list(data.split(" "))
        output = []
    if mode == "Even":
        for i in range(len(data)):
            if i % 2 != 0:
                if type == "L":
                    output.append(data[i])
                else:
                    output = output + data[i]
    else:
        for i in range(len(data)):
            if i % 2 == 0:
                if type == "L":
                    output.append(data[i])
                else:
                    output = output + data[i]
    return output

print("*** Odd Even ***")
typ, data, mode = input("Enter Input : ").split(",")
print(odd_even(typ, data, mode))