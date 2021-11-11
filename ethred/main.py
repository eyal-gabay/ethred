from threading import Thread
from time import sleep

import multiprocessing


class Ethred:
    """
    # example code

    def command(argv_1, number):
        os.system(f"sleep 2")
        print(argv_1, number)

    Ethred(
        5,
        timeout=3
    )(
        open("e.txt").readlines(),
        command
    )
    """
    def __init__(self, number_of_threads, timeout=None) -> None:
        self.stop_at = number_of_threads
        self.c = 0
        self.e = 0
        self.r = lambda *args: 0
        self.timeout_sleep = timeout

    def timeout(self, f, *args):
        p = multiprocessing.Process(target=f, args=args)
        p.start()
        p.join(self.timeout_sleep)
        if p.is_alive():
            p.kill()
            p.join()

    def _do(self, a, b) -> None:
        self.timeout(self.r, a, b)
        self.c -= 1

    def __call__(self, v: list, f) -> None:
        self.r.__code__ = f.__code__
        for i in v:
            i = i.strip()
            try:
                while 1:
                    if self.c < self.stop_at:
                        Thread(target=self._do, args=[i, self.e]).start()
                        self.c += 1
                        self.e += 1
                        break
                    else:
                        sleep(0.1)
            except KeyboardInterrupt:
                exit("bye bye")

