class Stack:
    def __init__(self):
        self.__items = []
    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        else: 
            return False
    def stacking(self, item):
        self.__items.append(item)
    def withDrawing(self):
        return self.__items.pop()
    def readTop(self):
        return self.__items[len(self.__items)-1]
    def showStack(self):
        print("Stack: ", self.__items, "<--TOP")

def stackSimulator():
    end = False
    stack = Stack()
    while not(end):
        option = input("Option: ")
        if(option == "1"):
            item = input("Introduce the element to stack: ")
            stack.stacking(item)
            print("Stacked element: ", item)
        elif(option == "2"):
            if stack.isEmpty():
                print("The stack is empty...you can't do this.")
            else:
                item = stack.readTop()
                stack.withDrawing()
                print("Withdrawing element: ", item)
        elif(option == "3"):
            if stack.isEmpty():
                print("The stack is empty, you can't read the top")
            else:
                print("The top is: ", stack.readTop())
        elif(option == "4"):
            if stack.isEmpty():
                print("The stack is empty")
            else:
                print("The stack is not empty")
        elif(option == "5"):
            stack.showStack()
        elif(option == "6"):
            end = True
print("""
*******************
Stack simulator.
*******************
Menu:
    1) Stack
    2) Wtihdarw
    3) Read top
    4) Is empty?
    5) Show stack
    6) Exit
""")

stackSimulator()