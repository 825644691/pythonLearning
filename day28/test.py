import threading


class Foo(threading.Thread):




threads = []
for i in range(5):
    threads.append(Foo())

for thread in threads:
    thread.start()