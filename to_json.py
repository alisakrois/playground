import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        data = func(*args, **kwargs)
        return json.dumps(data)
    return wrapped
