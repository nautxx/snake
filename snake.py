from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000) # sends dead snakes to some graveyard over in 1000, 1000
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    # moves snake forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0 , -1): # range(start, stop, step)
            new_x = self.segments[seg_num - 1].xcor() # gets 2nd to last segment x coord
            new_y = self.segments[seg_num - 1].ycor() # gets 2nd to last segment y coord
            self.segments[seg_num].goto(new_x, new_y) # tells last segment to go to position of 2nd to last segment
        self.head.forward(MOVE_DISTANCE) # moves first segment forward so the others can follow

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)