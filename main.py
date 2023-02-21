def to_seconds(milliseconds: List[float]) -> List[int]:
    return [int(x/1000.0) for x in milliseconds]

my_list: List[int] = [1]
my_list = to_seconds(my_list) # Pyre errors here!
