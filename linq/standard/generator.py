from ..core.collections import *
from ..core.flow import *
from ..core.utils import *

src = globals()
__all__ = [src]


@extension_class_name('generator')
def Next(self: Flow):
    return Flow(next(self.stream))


@extension_class_name('generator')
def Depend(self: Flow, elem):
    head = Unitter(elem)
    return Flow(concat_generator(head, self.stream))
