def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 1, 2, 3, 4])
    []
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([1])
    [0]
    '''
    # find majority element
    # if there is no majority element, return []
    # find the indexes of the majority element,
    # put them in a lst
    from collections import Counter
    if lst == []:
        return []
    count = Counter(lst)
    top_elems = sorted(
        count.keys(),
        key=lambda x: -count[x]
    )
    maj_elem = top_elems[0]
    # Top elem doesn't have majority count
    if count[maj_elem[0]] <= len(lst) // 2:
        return []
    return [
        i for i, elem in enumerate(lst)
        if elem == maj_elem
    ]


def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 1, 2, 3, 4])
    []
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([1])
    [0]
    '''
    # find majority element
    # if there is no majority element, return []
    # find the indexes of the majority element,
    # put them in a lst
    from collections import Counter
    if lst == []:
        return []
    count = Counter(lst)
    max_count = max(count.values())
    maj_elems = [
        elem for elem, count
        in count.items() if count == max_count
    ]
    # Top two elems have same count
    # or top elem doesn't have majority count
    if (
        len(maj_elems) > 1
        or count[maj_elems[0]] <= len(lst) // 2
    ):
        return []
    return [
        i for i, elem in enumerate(lst)
        if elem == maj_elems[0]
    ]
