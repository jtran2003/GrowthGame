class grade:

    def __init__(self, grade=6):
        self.grade = grade
        self.requirements = []

    def graduate(self, schedule: list[str]):
        for reqs in set(self.requirements):
            if schedule.count(reqs) < self.requirements.count(reqs):
                return False
        return True

class grade_six(grade):

    def __init__(self, grade=6):
        super().__init__(grade)
        self.requirements = ["gym", "math", "english", "art"]


class grade_seven(grade):

    def __init__(self, grade=6):
        super().__init__(grade)

class grade_eigh(grade):

    def __init__(self, grade=6):
        super().__init__(grade)

class grade_nine(grade):

    def __init__(self, grade=6):
        super().__init__(grade)

class grade_ten(grade):

    def __init__(self, grade=6):
        super().__init__(grade)

class grade_eleven(grade):

    def __init__(self, grade=6):
        super().__init__(grade)

class grade_twelve(grade):

    def __init__(self, grade=6):
        super().__init__(grade)


        