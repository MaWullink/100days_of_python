from turtle import Turtle

starting_positions = [0, -20, -40]
moving_pace = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.all_snakes= []
        self.create_snake()
        self.head = self.all_snakes[0]
    def create_snake(self):
      for i in range(3):
          snake = Turtle()
          snake.penup()
          snake.color("white")
          snake.shape("square")
          snake.goto(y=0, x=starting_positions[i])
          self.all_snakes.append(snake)
    def snake_move(self):
        start = len(self.all_snakes) - 1
        for snake in range(start, 0, -1):
            new_x = self.all_snakes[snake - 1].xcor()
            new_y = self.all_snakes[snake - 1].ycor()
            self.all_snakes[snake].goto(new_x, new_y)
        self.all_snakes[0].forward(moving_pace)
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)





