def count_unique(s):
    '''
    Count number of unique characters in s
    >>> count_unique("aabb")
    2
    >>> count_unique("abcdef")
    6
    '''
    # seen_c = [] # O(1)
    # # 0 + 1 + 2 + 3 + 4 + ... + n - 1 ~= n^2
    # for c in s: # O(n)
    #     if c not in seen_c: # O(n)
    #         seen_c.append(c) # O(1)
    # return len(seen_c) # O(n^2)

    # seen_c = set() # O(1)
    # for c in s: # O(n)
    #     if c not in seen_c: # O(1)
    #         seen_c.add(c) # O(1)
    # return len(seen_c) # O(n)

    # return len({c for c in s}) # O(n)

    return len(set(s))  # O(n)
