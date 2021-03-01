import inspect


def copy_function_args(func, locals_dict: dict):
    signature = inspect.signature(func)
    keys = signature.parameters.keys()
    return {k: locals_dict.get(k) for k in keys}
