from .decorator import coroutine


@coroutine
def printcoroutine():
    while True:
        s=yield
        print(s)


@coroutine
def writer(fname,mode='w'):
    with open(fname,mode) as f:
            while True:
                s=yield
                f.write(s)