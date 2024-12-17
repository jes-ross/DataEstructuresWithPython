class Queue:
    def __init__(self):
        self.__items = []
    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    def queuing(self, item):
        self.__items.insert(0,item)
    def unQueuing(self):
        return self.__items.pop()
    def readFirstOne(self):
        return self.__items[len(self.__items)-1]
    def readLastOne(self):
        auxiliaryQueue = Queue()
        while not(self.isEmpty()):
            lastElement = self.unQueuing()
            auxiliaryQueue.queuing(lastElement)
        while not(auxiliaryQueue.isEmpty()):
            self.queuing(auxiliaryQueue.unQueuing())
        return lastElement
    def numberOfElements(self):
        auxiliaryQueue = Queue()
        elements = 0
        while not(self.isEmpty()):
            elements += 1
            auxiliaryQueue.queuing(self.unQueuing())
        while not(auxiliaryQueue.isEmpty()):
            self.queuing(auxiliaryQueue.unQueuing())
        return elements
    def showQueue(self):
        print("Queue: ", self.__items, "<-- First Element")

def queueSimulator():
    end = False
    queue = Queue()
    while not(end):
        option = input("Option: ")
        if(option == "1"):
            item = input("Introduce the element to queue: ")
            queue.queuing(item)
            print("Element queued: ", item)
        if(option == "2"):
            if queue.isEmpty():
                print("The queue is empty")
            else:
                item = queue.readFirstOne()
                queue.unQueuing()
                print("Unqueueing element: ", item)
        elif(option == "3"):
            if queue.isEmpty():
                print("Queue is empty...you can't read no one :(")
            else:
                print("The first element is: ", queue.readFirstOne())
        elif(option == "4"):
            if queue.isEmpty():
                print("You can't do this")
            else:
                print("The last element is: ", queue.readLastOne())
        elif(option == "5"):
            if queue.isEmpty():
                print("Yes, It is")
            else:
                print("No, It's not empty")
        elif(option == "6"):
            if queue.isEmpty():
                print("No elements to count")
            else:
                print("The number of elements of the queue is: ", queue.numberOfElements())
        elif(option == "7"):
            if queue.isEmpty():
                print("Nothing to show")
            else:
                queue.showQueue()
        elif(option == "8"):
            end = True

print("""
*****************
Queue Simulator
*****************
    Menu:
    1) Queue
    2) Unqueue
    3) Read first element
    4) Read last element
    5) Is empty
    6) Number of elements
    7) Show elements
    8) Exit
""")
queueSimulator()