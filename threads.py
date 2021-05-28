import logging
import time
import threading


def ping(name):
    logging.info(f"Thread {name}: ping")
    time.sleep(2)
    logging.info(f"Thread {name}: pong")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main: before creating thread")
    t = threading.Thread(target=ping, args=(1, ))
    logging.info("Main: before starting thread")
    t.start()
    logging.info("Main: waiting on thread")
    # t.join()
    logging.info("Main: all done")
