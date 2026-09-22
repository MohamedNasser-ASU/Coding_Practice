class Student:
    def __init__(this, name, house):
        this.name  = name
        this.house = house

    def __str__(this):
        return f"{this.name} from {this.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


    # @property
    # def name(this):
    #     return this._name
    # @name.setter
    # def name(this, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     this._name = name

    # @property
    # def house(this):
    #     return this._house
    # @house.setter
    # def house(this, house):
    #     if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
    #         raise ValueError("Invalid house")
    #     this._house = house


def main():

    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
