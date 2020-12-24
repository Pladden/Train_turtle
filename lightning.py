from random import random
import turtle

DARK_BLUE = '#000020'
MAX_Y = turtle.Screen().window_height()//2
TOP = MAX_Y
BOTTOM = -MAX_Y
MAX_LINE_LENGTH = 100
MAX_ANGLE = 180
MAX_POWER = 10
MAX_SPEED = 0
NEW_BRANCH_PROBABILITY = 0.1 # 10%

class Branch(object):
	def __init__(self, parent_branch=None):
		self.p = turtle.Pen()
		self.p.speed(MAX_SPEED)
		self.p.pensize(MAX_POWER)
		self.p.color('white')
		self.p.up()
		if parent_branch:
			self.p.setposition(parent_branch.p.position())
		else:
			self.p.sety(TOP)

	def draw_line(self):
		self.p.setheading(0)
		angle = random() * MAX_ANGLE
		self.p.right(angle)
		self.p.down()
		distance = random() * MAX_LINE_LENGTH
		self.p.forward(distance)


def main():
	turtle.Screen().bgcolor(DARK_BLUE)
	branches = [Branch()]
	while branches[0].p.ycor() > BOTTOM:
		for b in branches: 
			b.draw_line()
			is_new_branch_needed = random() > 1 - NEW_BRANCH_PROBABILITY
			if is_new_branch_needed:
				branches += [Branch(b)]





main()
input()
