import random
class Hat:

    houses = ["griff", "huff", "raven", "slyth"]
    @classmethod
    def sort(cls, name):
        print(name+ " is in "+ random.choice(cls.houses))


Hat.sort("Harry")
