class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    # Compare elements at the front of all
    # linked lists
    # Add the minimum element and then
    # move all the pointers of the links
    # that contained the minimum element
    # from collections import defaultdict
    # result = Link(0)
    # pointer = result
    # val_to_links = defaultdict(list)
    # # O(k)
    # for link in linked_lists:
    #     val_to_links[link.val].append(link)

    # # final runtime = O(k*n*k)
    # # how many times is this while loop going to run?
    # # O(k*n)
    # while len(val_to_links) != 0:
    #     min_val = min(val_to_links)  # O(k)
    #     min_link = val_to_links[min_val].pop()  # O(1)
    #     pointer.next = Link(min_link.val)  # O(1)
    #     pointer = pointer.next  # O(1)
    #     # Check if should remove minimum value
    #     if len(val_to_links[min_val]) == 0:  # O(1)
    #         del val_to_links[min_val]  # O(1)
    #     if min_link.next:  # O(1)
    #         val_to_links[min_link.next.val].append(min_link.next)  # O(1)
    # return result.next

    # k - length of linked_lists
    # n - max length of any linked list
    # k*n - upper bound of number of values in all linked lists
    from collections import defaultdict
    from queue import PriorityQueue
    # keep a mapping of the value to the linked list
    # number -> list of linked list
    val_to_links = defaultdict(list)
    pq = PriorityQueue()
    # O(k)
    for link in linked_lists:
        val_to_links[link.val].append(link)
        pq.put(link.val)

    result = Link(0)
    pointer = result

    # how many times does the while loop run?
    # k*n
    while len(val_to_links) != 0:  # O(1)
        min_val = pq.get()  # O(log(k))
        link = val_to_links[min_val].pop()  # O(1)
        pointer.next = Link(link.val)
        pointer = pointer.next

        if len(val_to_links[min_val]) == 0:
            del val_to_links[min_val]  # O(1)
        if link.next:
            val_to_links[link.next.val].append(link.next)  # O(1)
            pq.put(link.next.val)

    # brute force: Final runtime: O(k*n*log(k*n))
    # find min val solution: Final runtime: O(k*n*k)
    # val to link solution: Final runtime: O(k*n*k)
    # priority queue solution: Final runtime: O(k*n*log(k))
    return result.next
