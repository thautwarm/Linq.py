from ..core.flow import *

src = globals()
__all__ = [src]


@extension_class(set)
def Intersects(self: Flow, *others) -> {'others': 'Seq<Seq> | Seq<Flow<Seq>>'}:
    return Flow(set.intersection(self.stream, *[unbox_if_flow(other) for other in others]))
    # List comprehension goes faster, so we do not use lazy map here.

@extension_class(set)
def Union(self: Flow, *others) -> {'others': 'Seq<Seq> | Seq<Flow<Seq>>'}:
    return Flow(set.union(self.stream, *[unbox_if_flow(other) for other in others]))


@extension_class(set)
def Difference(self: Flow, *others) -> {'others': 'Seq<Seq> | Seq<Flow<Seq>>'}:
    return Flow(set.difference(self.stream, *[unbox_if_flow(other) for other in others]))

@extension_class(set)
def Symmetric_difference(self: Flow, *other) -> {'others': 'Seq<Seq> | Seq<Flow<Seq>>'}:
    return Flow(set.symmetric_difference(self.stream, *[unbox_if_flow(other) for other in others]))
