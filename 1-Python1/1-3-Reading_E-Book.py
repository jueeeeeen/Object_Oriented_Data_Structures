print("*** Reading E-Book ***")

Text, Highlight = input("Text , Highlight : ").split(",")
output = ""
for letter in Text:
    if letter != Highlight:
        output += letter
    else:
        output = output + "["+ letter + "]"

print(output)