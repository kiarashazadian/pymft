def star(fn):
    def inner(*args):
        out = fn(*args)
        out ="*"+ out + "*"
        return out

    return inner


@star
def echo(s):
    return s


print(echo("khodahafez"))

