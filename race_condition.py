import threading

x = 0

def inc():
    global x
    for _ in range(10_000_000):
        x += 1


def dec():
    global x
    for _ in range(10_000_000):
        x -= 1


def run():
    print(f"x = {x}")
    t1 = threading.Thread(target=inc)
    t2 = threading.Thread(target=dec)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"x = {x}")
