import math

## Task 0.1
## Mathematical operators


def mul(x, y):
    """
    Multiplication.

    Args:
        x (float): A float number
        y (float): A float number

    Returns:
        Multiplication of two numbers
    """
    return x * y
    # ":math:`f(x, y) = x * y`"
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def id(x):
    """
    Identity.

    Args:
        x (float): A float number

    Returns:
        x
    """
    return x


def add(x, y):
    """
    Multiplication.

    Args:
        x (float): A float number
        y (float): A float number

    Returns:
        Addition of two numbers
    """
    return x + y


def neg(x):
    """
    Negation.

    Args:
        x (float): A float number

    Returns:
        Negation of x
    """
    return -x


def lt(x, y):
    """
    Find whether x is a smaller number than y.

    Args:
        x (float): A float number
        y (float): A float number

    Returns:
        Boolean indicating x is lower than y
    """
    return x < y


def eq(x, y):
    """
    Find whether x is equals to y.

    Args:
        x (float): A float number
        y (float): A float number

    Returns:
        Boolean indicating x equals y
    """
    return x == y


def max(x, y):
    """
    Find max of given two numbers x and y.

    Args:
        x (float): A float number
        y (float): A float number

    Returns:
        Maximum number of the two inputs
    """
    return x if x > y else y


def sigmoid(x):
    """
    Find sigmoid of given number.

    Args:
        x (float): A float number

    Returns:
        Sigmoidal of the input
    """
    return (1. / (1. + math.exp(-x))) if x >= 0 else (1. / (1. + math.exp(x)))


def relu(x):
    """
    Find ReLU activation of given number.

    Args:
        x (float): A float number

    Returns:
        ReLu value of the input
    """
    return x if x > 0 else 0


def relu_back(x, y):
    """
    Find back ReLU activation of given number.

    Args:
        x (float): A float number
        y (float): A float number

    Returns:
        Back ReLu value of the input
    """
    return y if x > 0 else 0


EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(a, b):
    return b / (a + EPS)


def inv(x):
    ":math:`f(x) = 1/x`"
    return 1.0 / x


def inv_back(a, b):
    return -(1.0 / a ** 2) * b


## Task 0.3
## Higher-order functions.


def map(fn):
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): process one value

    Returns:
        function : a function that takes a list and applies `fn` to each element
    """
    # TODO: Implement for Task 0.3.
    raise NotImplementedError('Need to implement for Task 0.3')


def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    return map(neg)(ls)


def zipWith(fn):
    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) one each pair of elements.

    """
    # TODO: Implement for Task 0.3.
    raise NotImplementedError('Need to implement for Task 0.3')


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    return zipWith(add)(ls1, ls2)


def reduce(fn, start):
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
        fn(x_1, x_0)))`

    """
    # TODO: Implement for Task 0.3.
    raise NotImplementedError('Need to implement for Task 0.3')


def sum(ls):
    """
    Sum up a list using :func:`reduce` and :func:`add`.
    """
    # TODO: Implement for Task 0.3.
    raise NotImplementedError('Need to implement for Task 0.3')


def prod(ls):
    """
    Product of a list using :func:`reduce` and :func:`mul`.
    """
    # TODO: Implement for Task 0.3.
    raise NotImplementedError('Need to implement for Task 0.3')
