import logging
from spydrnet import ir
from types import GeneratorType

logger = logging.getLogger('spydrnet_logs')


def get_names(objects):
    '''
    Returns names of the object (it the object contains name property)

    args:
        object(list[Cable, Port, Definition, Instance]): pass list of objects
    returns:
        (list[str]) : list of
    '''
    names = []
    if not isinstance(objects, (list, tuple, GeneratorType)):
        objects = tuple([objects,])
    for each in objects:
        if isinstance(each, (ir.Cable, ir.Port, ir.Definition, ir.Instance)):
            names.append(each.name)
        else:
            logger.warning("Skipping unsupport object %s", type(each))
    return names
