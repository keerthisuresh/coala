from coalib.misc.Decorators import generate_eq, generate_repr


@generate_repr("begin", "inside", "end")
@generate_eq("begin", "inside", "end")
class InBetweenMatch:
    """
    Holds information about a match performed with the `search_in_between`
    functions.
    """

    def __init__(self, begin, inside, end):
        """
        Instantiates a new InBetweenMatch.

        :param begin:  The `Match` of the start pattern.
        :param inside: The `Match` between start and end.
        :param end:    The `Match` of the end pattern.
        """
        self._begin = begin
        self._inside = inside
        self._end = end

    @property
    def begin(self):
        return self._begin

    @property
    def inside(self):
        return self._inside

    @property
    def end(self):
        return self._end
