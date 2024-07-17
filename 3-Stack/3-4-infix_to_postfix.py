class Stack :

    def __init__(self,list = None) :
        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self) :
        return self.items == []

    def push(self,data) :
        self.items.append(data)

    def pop(self) :
        return self.items.pop()

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]


def infix2postfix(exp) :
    s = Stack()
    postfix = ""
    symbols = {"+":1, "-":1, "*":2, "/":2, "(":3}
    for item in exp:
        if "a" <= item <= "z":
            postfix += item
        elif item in "+-*/(":
            while not s.isEmpty() and ((item == ")") or (s.peek() != "(" and symbols[item] <= symbols[s.peek()])):
                if s.peek() != "(":
                    postfix += s.peek()
                s.pop()
            s.push(item)
    while not s.isEmpty():
        if s.peek() != "(":
            postfix += s.peek()
        s.pop()
    return postfix


print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))