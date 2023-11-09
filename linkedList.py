import tkinter as tk

class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value: int):
        newNode = node(value)
        if self.head is None:
            self.head = newNode
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = newNode
    
    def print(self) -> None:
        linkedListValueString = ""
        pointer = self.head
        while pointer:
            linkedListValueString += str(f"{pointer.data}")
            if pointer.next:
                linkedListValueString += str(" --> ")
            pointer = pointer.next
        print(linkedListValueString)
    
    #can be used in testing
    def getString(self) -> str:
        linkedListValueString = ""
        pointer = self.head
        while pointer:
            linkedListValueString += str(f"{pointer.data}")
            if pointer.next:
                linkedListValueString += str(" --> ")
            pointer = pointer.next
        return linkedListValueString

class VisualizeLinkedList:
    def __init__(self) -> None:
        self = tk.Tk()
        self.title("Linked List visualizer")
        self.geometry_x = 500
        self.geometry_y = 500
        self.geometry(f"{self.geometry_x},{self.geometry_y}")
        label = tk.Label(self, text= myLinkedList.getString())
        label.pack()

    def getLengthOfLinkList(inputLinkedList: linkedList) -> int:
        current = inputLinkedList.head
        if inputLinkedList.head == None:
            return 0
        lengthCount = 1 
        while inputLinkedList.head.next:
            current = current.next
            lengthCount +=1
        return lengthCount
    
    def run(self):
        #mainloop
        self.mainloop()
        
        

myLinkedList = linkedList
myLinkedList.append(3)
myLinkedList.append(9)
myLinkedList.append(27)

myLinkedList.print()

#myList = VisualizeLinkedList
#myList.run()


        

