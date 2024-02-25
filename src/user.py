import skills
import cohere
import progression
import os
from dotenv import load_dotenv

load_dotenv()
COHERE_KEY = os.getenv("COHERE_KEY")
co = cohere.Client(COHERE_KEY)

class User:
    
    def __init__(self, name):

        academics = skills.academics()
        athletics = skills.athletics()
        creativity = skills.creativity()

        self.name = name
        self.age = 11
        self.grade = progression.grade()
        self.work = progression.work()
        # self.gender = ''
        self.schedule = []
        self.action_history = {}
        self.skills = [academics, athletics, creativity]

    def set_schedule(self, sched):
        self.schedule = sched
        

    def update_skills(self):
        self.action_history[self.age] = self.schedule

        for skill in set(self.schedule):
            if skill[1] == "academics":
                self.skills[0].increment_skill(self.schedule.count(skill))
            elif skill[1] == "athletics":
                self.skills[1].increment_skill(self.schedule.count(skill))
            else:
                self.skills[3].increment_skill(self.schedule.count(skill))

    def get_skills(self):
        return {skill.get_name(): skill.get_level() for skill in self.skills}




if __name__ == "__main__":
    user = User("test")
    user.set_schedule(["math", "math", "basketball","history","music", "basketball"])
    user.update_skills()
    print(user.get_skills())
