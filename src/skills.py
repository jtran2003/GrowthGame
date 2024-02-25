import cohere
import os
from dotenv import load_dotenv
import re

load_dotenv()
COHERE_KEY = os.getenv("COHERE_KEY")
co = cohere.Client(COHERE_KEY)

class skill:
    def __init__(self) -> None:
        self.level = 0
        self.name = ""
        self.search_key = ""

    def increment_skill(self, count=0, weight=0):
        self.level += count + weight
    
    def get_level(self):
        return self.level
    
    def get_name(self):
        return self.name
    
    def search_activities(self, schedule):
        history = ", ".join(schedule)
        ret = None

        while not ret:
            res = co.chat(message=f"Please provide me a serious comma separated string of {self.search_key} for students who have previously done {history} and do not include the activities that I have mentioned. Additionally, please do not include any comments, prefacing text, or additional jargon aside from the string.", model="command-light", temperature=0.2).text
            res_list = res.split("\n")

            for i in range(len(res_list)):
                if re.search(".+,.+,.+,.+", res_list[i]):
                    if len(res_list[i].split(", ")) > 5:
                        return [[activity.strip(), self.name] for activity in res_list[i].split(",")]


class academics(skill):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "academics"
        self.search_key = "classes"
    
    def search(grade, schedule):
        if grade < 9:
            return [["math", "academics"], ["science","academics"], ["english","academics"], ["french","academics"], ["history","academics"], ["PE","academics"], ["music","academics"]]
        if grade < 11:
            return [["math","academics"], ["science","academics"], ["english","academics"], ["french","academics"], ["history","academics"], ["PE","academics"], ["music","academics"], ["business","academics"], ["tech","academics"]]
        else:
            return super().search_activities(schedule)
        

class athletics(skill):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "athletics"
        self.search_key = "sports"



class creativity(skill):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "creativity"
        self.search_key = "hobbies"

if __name__ == "__main__":
    test = creativity()
    print(test.search_activities(["math", "math", "basketball","history","music", "basketball"]))