from turtle import Turtle

class Roadways(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.first_line_y = -290
        self.print_roadways()

    def print_roadways(self):
        for pos in range(15):
            self.goto(-300, self.first_line_y)
            for line in range(15):
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(20)
            self.first_line_y += 60