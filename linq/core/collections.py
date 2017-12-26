from ..core.utils import concat_generator


class Generator:
    def __init__(self, rule, start_elem):
        self.rule = rule
        self.start_elem = start_elem

    def __iter__(self):
        now = self.start_elem
        while True:
            try:
                yield now
                now = self.rule(now)
            except StopIteration:
                break


class Unitter(Generator):
    def __init__(self, unit):
        def stop(_):
            raise StopIteration()

        super().__init__(stop, unit)


class Scanner:
    def __init__(self, rule, seq, start_elem):
        self.rule = rule
        self.seq = seq
        self.start_elem = start_elem

    def __iter__(self):
        last = self.start_elem
        for now in self.seq:
            acc = self.rule(last, now)
            yield acc
            last = acc


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
        return cls(initializer[0], lambda: cls.deduce(f, *initializer[1:],
                   f(*initializer)))

    def __radd__(self, left):
        return Deducer(left, lambda: self.determine(self.first, *self.rest()))

    def __iter__(self):
        try:
            if self.first is None:
                raise StopIteration()
            yield self.first
            yield from self.rest()
        except StopIteration:
            pass
