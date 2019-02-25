import sys, time


def bar(i, N):
    sys.stdout.write("*" * i + "="*(N-i) + '\r')
    sys.stdout.flush()
    time.sleep(0.1)
    print()


if __name__ == "__main__":
    pass
