class skill:
    def __init__(self) -> None:
        self.level = 0

    def increment_skill(self, count):
        self.level += count

class academics(skill):
    def __init__(self) -> None:
        super().__init__()
        print("academics created!")

class athletics(skill):
    def __init__(self) -> None:
        super().__init__()
        print("athletics created")

class creativity(skill):
    def __init__(self) -> None:
        super().__init__()
        print("creativity created!")