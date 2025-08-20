from turtle import Turtle
START_POSITIONS  = [(0, 0), (-25, 0), (-50,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def move_snake(self):
        for seg_num in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[seg_num-1].xcor()
            new_y = self.snakes[seg_num-1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.snakes[0].forward(15)

    def head(self):
        return self.snakes[0]

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)
            self.move_snake()

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)
            self.move_snake()

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)
            self.move_snake()

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
            self.move_snake()

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def add_segment(self, pos):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.snakes.append(snake)