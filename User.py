
class User:

    def __init__(self, name):
        self.name = name
        self.point = 0


    def __str__(self):
        return f"""
        Name: {self.name}
        Point: {self.point}
        """

    def add_point(self):
        self.point = self.point + 1





