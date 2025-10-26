def curry(f, n):
    def inner(*args):
        lis = []
        for value in args:
            lis.append(value)
        if len(lis) == n:
            return f(*args)
        else:
            return lambda *more_args: inner(*args, *more_args)
    return inner

def uncurry(curry, n):
    def inner(*args):
        if len(args) != n:
            raise ValueError
        res = curry

        for arg in args:
            res = res(arg)
        return res
    return inner


def f(x, y, z):
    return x + y + z

f_curry = curry(f, 3)
print(f_curry(1)(2)(3))

f_uncurry = uncurry(f_curry, 3)
print(f(1, 2, 3))



