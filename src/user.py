import skills

class User:
    
    def __init__(self, name, gender):

        academics = skills.academics()
        athletics = skills.athletics()
        creativity = skills.creativity()

        self.name = ""
        self.grade = 6
        self.age = 11
        self.gender = ''
        self.schedule = []
        self.skills = [academics, athletics, creativity]

    def addToSchedule():
        pass

    def updateSkills():
        pass

if __name__ == "__main__":
<<<<<<< HEAD
    user = User("test", "F")
=======
    user = User("test", "F")
>>>>>>> f196d39e5bff2528ffafae3961cddaf8e563a341
