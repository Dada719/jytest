def wrapper1(fn):
    def inner(*args,**kw):
        print("wrapper1start")
        re=fn(*args,**kw)
        print("wrapper1end")
        return re
    return inner

def wrapper2(fn):
    def inner(*args,**kw):
        print("wrapper2start")
        re=fn(*args,**kw)
        print("wrapper2end")
        return re
    return inner


@wrapper1
@wrapper2
def target():
    print("target")
# 1 2 t 2 1



target()
