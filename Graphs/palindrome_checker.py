class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)
    
    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def palchecker(self, aString):
        chardeque = Deque()

        for ch in aString:
            chardeque.add_rear(ch)

        stillEqual = True

        while chardeque.size() > 1 and stillEqual:
            first = chardeque.remove_front()
            last = chardeque.remove_rear()
            if first != last:
                stillEqual = False

        return stillEqual

chardeque = Deque()
print(chardeque.palchecker('racecar'))

