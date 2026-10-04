"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False

# I used a set because a set will allow me to see if a product ID has already been seen. Each ID is checked 
# once so the runtime should be 0(n)


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if len(self.tasks) == 0:
            return None
        return self.tasks.pop(0)

# I used a list as a queue because tasks needed to stay in the order they were added.
# Adding the append is 0(1), while removing the oldest task with pop(0) is 0(n)


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

# I used another set this time because it automatically stores only unique values
# Adding a value is expected 0(1), and getting the numbers of the unique values with len is 0(1)


print(has_duplicates([10, 20, 30, 20, 40]))
print(has_duplicates([1, 2, 3, 4, 5]))

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(task_queue.remove_oldest_task())

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())