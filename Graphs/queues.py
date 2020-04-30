class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Takes in an item and inserts that item into the 0th index of the list
        that is representing the Queue.
        
        The runtime is O(n), or linear time, because inserting into the 0th
        index of a list forces all the other items in the list to move one index
        to the right
        """
        self.items.insert(0, item)
    
    def dequeue(self):
        """Returns and the front most item of the Queue, which is
        represented by the last item in the list.

        The runtime is O(1), or constant time, because indexing to the end of a 
        list happens in constant time.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Return the last item in the list. which represents the front-most
        item in the Queue.
            
        The runtime is constant because we're just indexing to the last item of 
        the list and returning the value found there.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the size of the Queue, which is represented by the length of 
        the list.
        
        The runtime is 0(1), or constant time, because we're only returning the length.
        """
        return len(self.items)

    def is_empty(self):
        """Returns a Boolean value expressing whether of not the lsit
        representing the Queue is empty
        
        Runs in constant time, because it's only checking for equality.
        """
        return self.items == []

my_q = Queue()
my_q.enqueue('apple')
print(my_q.items)
my_q.enqueue('banana')
print(my_q.items)
my_q.dequeue()
print(my_q.items)
print(my_q.dequeue())
print(my_q.items)
print(my_q.dequeue())
print(my_q.peek())
my_q.enqueue('apple')
print(my_q.peek())
print(my_q.size())
print(my_q.is_empty())