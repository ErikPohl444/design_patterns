import copy
"""
Create one prototypical instance, then create new objects using those instances
"""


class Kambucha:
    """
    This is an example class which is the source and can be copied
    """
    def __init__(self):
        print("Mmm. Kambucha is created at a factory.")

    def __deepcopy__(self, memodict={}):
        print("we cloned a kambucha from another kambucha!")


def main():
    mother_prototype = Kambucha()
    kambucha_copy = copy.deepcopy(mother_prototype)
    even_more = copy.deepcopy(mother_prototype)


if __name__ == "__main__":
    main()
