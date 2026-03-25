def qidong(game):
    def inner(*args,**kwargs):
        print("QIDONG")
        ret=game(*args,**kwargs)
        print("guanbi")
        return ret
    return inner
@qidong
def dnf(username, password):
    print("DNF", username, password)
    return "DNF"

@qidong
def lol(username,password,hero):
    print("LOL", username, password, hero)

# lol(username="z",password="123",hero="z")
s=dnf("z","123")
print(s)
