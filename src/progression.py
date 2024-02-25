class grade:

    grade_requirements = {
        6:[],
        7:[],
        8:[],
        9:[],
        10:[],
        11:[],
        12:[]
    }
    def __init__(self):
        self.grade = 6

    def graduate(self, schedule: list[str]):
        for reqs in set(self.grade_requirements[self.grade]):
            if schedule.count(reqs) < self.requirements.count(reqs):
                return False
        if self.grade < 12:
            self.grade += 1