class Wizard:
    def __init__(this, name):
        if not name:
            raise ValueError("No name")
        this.name = name


class Student(Wizard):
    def __init__(this, name, house):
        super().__init__(name)
        this.house = house


class Professor(Wizard):
    def __init__(this, name, subject):
        super().__init__(name)
        this.subject = subject
