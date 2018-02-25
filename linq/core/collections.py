class Deducer:
    def __init__(self, first, rest=None):
        self.first = first
        self.rest = rest or (lambda: Deducer(None, None))

    @classmethod
    def determine(cls, *values):
        if not values:
            return cls(None, None)

        return cls(values[0], lambda: cls.determine(*values[1:]))

    @classmethod
    def deduce(cls, f, *initializer):
        return cls(initializer[0], lambda: cls.deduce(f, *(initializer[1:] + (f(*initializer),))))

    @classmethod
    def scan(cls, rule, seq, start_elem):
        try:
            iterator = iter(seq)
            last = start_elem
            now = rule(last, next(iterator))
            return cls(now, lambda: cls.scan(rule, iterator, now))
        except StopIteration:
            return cls(None, None)

    def __radd__(self, left):
        return Deducer(left, lambda: self.determine(self.first, *self.rest()))

    def __iter__(self):
        try:
            if self.first is None:
                raise StopIteration
            yield self.first
            yield from self.rest()
        except StopIteration:
            pass

    def __next__(self):
        if self.first is None:
            raise StopIteration
        now, nex = self.first, self.rest()
        self.first, self.rest = nex.first, nex.rest
        return now
