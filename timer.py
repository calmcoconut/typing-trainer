import time

class Clock:
    def elapsed_time(started, ended):
        started = time.time()
        ended = time.time()
        
        return ended - started

if __name__ == '__main__':
    myclock = Clock()
