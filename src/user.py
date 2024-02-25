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

        self.name = ""
        self.age = 11
        self.grade = progression.grade()
        # self.gender = ''
        self.schedule = []
        self.action_history = {}
        self.skills = [academics, athletics, creativity]

    def set_schedule(self, sched):
        self.schedule = sched
        

    def update_skills(self):
        self.action_history[self.age] = self.schedule
        update = [0] * 3
        DOCS = ["nerd", "jock", "dork"]

        for skill in self.schedule:
            res = co.rerank(query=skill, documents=DOCS, model="rerank-english-v2.0", top_n = 3)
            print(res)
            update[res[0].index] += 1
        
        for i in range(len(update)):
            self.skills[i].increment_skill(update[i])

    def get_skills(self):
        return {skill.get_name(): skill.get_level() for skill in self.skills}




if __name__ == "__main__":
    user = User("test")
    user.set_schedule(["math", "math", "basketball","history","music", "basketball"])
    user.update_skills()
    print(user.get_skills())
