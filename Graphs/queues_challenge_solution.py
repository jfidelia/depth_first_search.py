import random

class PrintQueue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


class Job:

    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False



class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:  # Queue is empty
            return "No more jobs to print." 

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "printing complete"
        else:
            return "An error occurred."

job1 = Job()
print_q = PrintQueue()
printer = Printer()
print_q.enqueue(job1)
print(print_q.items)
printer.get_job(print_q)
print(print_q.items)

print(printer.print_job(printer.current_job))
