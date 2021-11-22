# Given a string, find the top 3 letter that appear the most
# frequently, and return a list of tuples with the character
# and count.


from collections import deque
from collections import Counter
from collections import namedtuple


def top_three_letters(string):
    '''
    Given a string find the three most
    frequent letters
    This method should return a list
    of tuples, where the tuple contains
    the character and count

    >>> top_three_letters("abbccc")
    [('c', 3), ('b', 2), ('a', 1)]
    >>> top_three_letters("aabbccd")
    [('a', 2), ('b', 2), ('c', 2)]
    '''
    counter = defaultdict(int)
    for c in string:
        counter[c] += 1
    top_three_letters = sorted(
        counter, key=lambda k: counter[k], reverse=True)[:3]
    return [(c, counter[c]) for c in top_three_letters]


# Counter takes in an iterable or a mapping


def top_three_letters_better(string):
    return Counter(string).most_common(3)

# >>> counter = Counter(["hello", "hello", "world"])
# >>> isinstance(counter, dict)
# True
# >>> counter["hello"]
# 2
# >>> counter["hello"] += 1
# >>> counter["hello"]
# 3


class TicketQueue(object):
    def __init__(self):
        self.deque = deque()

    def add_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        """
        self.deque.append(name)
        print(f"{name} has been added to the queue")

    def service_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        >>> queue.service_person("Jack")
        Jack has been serviced
        """
        front_of_line = self.deque.popleft()
        print(f"{front_of_line} has been serviced")

    def bypass_queue(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        >>> queue.bypass_queue("Jill")
        Jill has bypassed the queue
        """
        # self.queue = [name] + self.queue
        # self.queue.insert(0, name)
        self.deque.appendleft(name)
        print(f"{name} has bypassed the queue")
