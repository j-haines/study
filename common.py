import functools

def print_return(func):
    @functools.wraps(func)
    def wraps(*args):
        ret = func(*args)
        print(ret)
        return ret
    return wraps
