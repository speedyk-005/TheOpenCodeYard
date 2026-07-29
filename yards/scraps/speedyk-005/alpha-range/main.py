"""Alpha range generator — yield letters like range() does numbers."""


def alpha_range(a, z, step=1):
    for i in range(ord(a), ord(z), step):
        yield chr(i)


if __name__ == "__main__":
    for i in alpha_range("a", "z", 2):
        print(i)