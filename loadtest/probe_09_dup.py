import os


def run(cmd):
    # load-test probe 09-dup: deliberate command injection
    return os.system("sh -c " + cmd)


if __name__ == "__main__":
    run(input())
