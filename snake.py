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
        self.head = self.snakes[0]
        

    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def move_snake(self):
        for seg_num in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[seg_num-1].xcor()
            new_y = self.snakes[seg_num-1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.head.forward(15)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move_snake()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move_snake()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move_snake()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
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

    def reset_snake(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
