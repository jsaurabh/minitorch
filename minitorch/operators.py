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
    Addition.

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
    return 1. if x < y else 0.


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

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): process one value

    Returns:
        function : a function that takes a list and applies `fn` to each element
    """
    def _apply(items):
        return [fn(item) for item in items]
    return _apply


def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    return map(neg)(ls)


def zipWith(fn):
    """
    Higher-order zipwith (or map2).

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) one each pair of elements.
    """
    def _apply(items1, items2):
        return [fn(item1, item2) for item1, item2 in zip(items1, items2)]

    return _apply


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    return zipWith(add)(ls1, ls2)


def reduce(fn, start):
    """
    Higher-order reduce.

    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        and computes the reduction

    """
    def _apply(items):
        s = start
        for item in items:
            s = fn(s, item)
        return s

    return _apply


def sum(ls):
    """
    Sum up a list using `reduce` and `add`
    """
    return reduce(add, 0)(ls)


def prod(ls):
    """
    Product of a list using :func:`reduce` and :func:`mul`.
    """
    return reduce(mul, 1)(ls)
