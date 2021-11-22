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
    # brute force solution
    # put all the values of all the linked list into a list
    # sort the list and create a final list from those values
    # k - length of linked_lists
    # n - max length of any linked list
    # k*n - upper bound of the number of values in all linked lists
    values = []
    # O(k*n)
    for link in linked_lists:  # O(k)
        # O(n)
        while link:
            values.append(link.val)
            link = link.next

    # O(k*n*log(k*n))
    sorted_vals = sorted(values)

    result = Link(0)
    pointer = result
    # O(k*n)
    for val in sorted_vals:
        pointer.next = Link(val)
        pointer = pointer.next

    # Final runtime: O(k*n*log(k*n))
    return result.next
