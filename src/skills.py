class skill:
    def __init__(self) -> None:
        self.level = 0
        self.name = ""

    def increment_skill(self, count):
        self.level += count
    
    def get_level(self):
        return self.level
    
    def get_name(self):
        return self.name



class academics(skill):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "academics"



class athletics(skill):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "athletics"



class creativity(skill):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "creativity"