import greenlet

def test1():
    print(12)
    gr2.switch()
    print(36)
    gr2.switch()


def test2():
    print(24)
    gr1.switch()
    print(48)





gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
gr1.switch()
print(78)