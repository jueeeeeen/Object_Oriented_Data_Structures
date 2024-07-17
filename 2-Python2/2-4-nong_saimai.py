def hbd(age):
    return f"saimai is just {20 + (age%2)}, in base {int(age/2)}!"

year = input("Enter year : ")

print(hbd(int(year)))