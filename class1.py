class Hello:
    def __init__(self, str):
        self.str = str
class NewClass(Hello):
    def __init__(self):
        super().__init__()

    def apply_function(self):
        self.tptint()