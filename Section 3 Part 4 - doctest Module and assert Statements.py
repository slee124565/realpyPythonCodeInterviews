class A():
    def __init__(self):
        pass

    def f(self):
        '''
        Function description and anything else goes here...
        >>> a = A()
        >>> a.f()
        Hello world
        'Hello world'
        '''
        print('Hello world')
        return 'Hello world'

    @property
    def error(self):
        '''
        >>> A().error
        Traceback (most recent call last):
        ...
        Exception: I am an error
        '''
        raise Exception("I am an error")


def f(x):
    '''
    >>> f(10)
    Args: 10
    'Valid input'
    >>> f(-1)
    Traceback (most recent call last):
    ...
    ValueError: Invalid input
    '''
    if x <= -1:
        raise ValueError("Invalid input")
    print(f"Args: {x}")
    return 'Valid input'


def g(x):
    # assert <condition>, [<error>]
    # assert x >= 0, "Invalid input"
    pass


def lst_one_more(lst1, lst2):
    assert len(lst1) == len(lst2), "Length of lists are not the same"
    for i in range(len(lst1)):
        lst1[i] = lst2[i] + 1


lst1 = [1, 1, 1]
lst2 = [1, 2, 3]
lst_one_more(lst1, lst2)
for i, x in enumerate(lst1):
    # assert x == lst2[i] + 1
    print(x, lst2[i])
