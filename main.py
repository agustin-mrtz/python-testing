from typing import Callable

from pyre_extensions import ParameterSpecification

def to_seconds(milliseconds: List[float]) -> List[int]:
    return [int(x/1000.0) for x in milliseconds]

my_list: List[int] = [1]
my_list = to_seconds(my_list) # Pyre errors here!


def zeroes(number_of_elements: int) -> List[float]:
    a = [0] * number_of_elements
    return a # Pyre errors here!

P = ParameterSpecification("P")

# OK
def good(f: Callable[P, int], *args: P.args, **kwargs: P.kwargs) -> int:
    return f(*args, **kwargs)

# Error because `**kwargs: P.kwargs` is missing.
def bad1(f: Callable[P, int], *args: P.args) -> int:
    return f(*args)

# Error because `*args: P.args` is missing.
def bad2(f: Callable[P, int], **kwargs: P.kwargs) -> int:
    return f(**kwargs)
