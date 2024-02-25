import cohere
import os
from dotenv import load_dotenv
import re
import random

load_dotenv()
COHERE_KEY = os.getenv("COHERE_KEY")
co = cohere.Client(COHERE_KEY)

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

class work:

    def __init__(self):
        self.occupation = None

    def search_job(self, schedule, grade):
        history = ", ".join(schedule)
        ret = None

        while not ret:
            res = co.chat(message=f"Please provide me a serious comma separated string of part-time jobs for students in grade {grade} who have previously done {history}. Additionally, please do not include any comments, prefacing text, or additional jargon aside from the string.", model="command-light", temperature=0.2).text
            res_list = res.split("\n")

            for i in range(len(res_list)):
                if re.search(".+,.+,.+,.+", res_list[i]):
                    if len(res_list[i].split(", ")) > 5:
                        return [job.strip() for job in res_list[i].split(",")]
        
    def apply_to_job(self, job, history):
        DOC = set(history)
        DOC.add("student job")
        DOC = list(DOC)

        res = co.rerank(query=job, documents=DOC, model="rerank-english-v2.0", top_n=1)[0]
        if res.document['text'] == "student job":
            self.occupation = job
            print("Job changed successfully")
        else: 
            count = history.count(DOC[res.index])
            roll = random.randint(1, 30)
            if roll <= count:
                self.occupation = job
                print("Job changed successfully")
            else:
                print("Job unchanged")
        return res

                    
if __name__ == "__main__":
    jobs = work()
    # print(jobs.search_job(["math"], 6))
    print(jobs.apply_to_job("math teacher", ["math", "math","math","math","math","math","math","math","math","math"]))