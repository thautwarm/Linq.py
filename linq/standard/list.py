from ..core.flow import *
from ..core.utils import *

src = globals()
__all__ = [src]


@extension_class(list)
def Extended(self: Flow, *others):
    stream = []
    stream.extend(self.stream)
    for other in map(unbox_if_flow, others):
        stream.extend(other)
    return Flow(stream)


@extension_class(list)
def Extend(self: Flow, *others):
    for other in map(unbox_if_flow, others):
        self.stream.extend(other)
    return self


@extension_class(list)
def Appended(self: Flow, elem):
    stream = self.stream + [elem]
    return Flow(stream)


@extension_class(list)
def Append(self: Flow, elem):
    self.stream.append(elem)
    return self


@extension_class(list)
def Depended(self: Flow, elem):
    stream = [elem] + self.stream
    return Flow(stream)


@extension_class(list)
def Depend(self: Flow, elem):
    self.stream.insert(0, elem)
    return self


@extension_class(list)
def Reversed(self: Flow):
    return Flow(self.stream[::-1])


@extension_class(list)
def Reverse(self: Flow):
    self.stream.reverse()
    return self


@extension_class(list)
def Removed(self: Flow, elem):
    stream = self.stream[:].remove(elem)
    return Flow(stream)


@extension_class(list)
def Remove(self: Flow, elem):
    self.stream.remove(elem)
    return self


@extension_class(list)
def Inserted(self: Flow, idx, elem):
    stream = self.stream[:].insert(idx, elem)
    return Flow(stream)


@extension_class(list)
def Insert(self: Flow, idx, elem):
    self.stream.insert(idx, elem)
    return self


@extension_class(list)
def Sorted(self: Flow, by):
    if is_to_destruct(by):
        by = destruct_func(by)
    stream = self.stream[:]
    stream.sort(key=by)
    return Flow(stream)


@extension_class(list)
def Sort(self: Flow, by):
    if is_to_destruct(by):
        by = destruct_func(by)
    self.stream.sort(key=by)
    return self