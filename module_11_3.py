import inspect
from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else '__main__'

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }

    return info


number_info = introspection_info(42)
pprint(number_info)

string_info = introspection_info('Good evening')
pprint(string_info)

list_info = introspection_info([8, 4.0, 'Night'])
pprint(list_info)

