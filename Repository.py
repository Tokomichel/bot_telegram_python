
class Repository:
    def __init__(self, ame) -> None:
        self.name =  ame
        self.language = []

    def __str__(self) -> str:
        return self.name + "\n" + self.language