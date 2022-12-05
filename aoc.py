def chunks(iterable, length: int):
    """
    Generator to return chunks of size length
    list(aoc.chunks("abcdefg", 3)) -> ['abc', 'def', 'g']
    """
    for start in range(0, len(iterable), length):
        yield iterable[start:start + length]

