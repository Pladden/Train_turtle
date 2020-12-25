from random import random
import math
import turtle

DARK_BLUE = '#000020'
MAX_Y = turtle.Screen().window_height()//2
TOP = MAX_Y
BOTTOM = -MAX_Y
MAX_LINE_LENGTH = 100
MAX_ANGLE = 180
MAX_POWER = 7
MAX_SPEED = 0
NEW_BRANCH_PROBABILITY = 0.1 # 10%
BRANCH_DEATH_PROBABILITY = 0.1

class Branch(object):
	def __init__(self, parent_branch=None):
		self.p = turtle.Pen()
		self.p.hideturtle()
		self.p.speed(MAX_SPEED)
		self.p.color('white')
		self.p.penup()
		if parent_branch:
			self.p.setposition(parent_branch.p.position())
			self.power = math.ceil(parent_branch.power / 3)
		else:
			self.p.sety(TOP)
			self.power = MAX_POWER
		self.p.pensize(self.power)
		self.is_alive = True

	def draw_line(self):
		self.p.setheading(0)
		angle = random() * MAX_ANGLE
		self.p.right(angle)
		self.p.pendown()
		distance = random() * MAX_LINE_LENGTH
		self.p.forward(distance)

	def decide_if_alive(self):
		self.is_alive = random() < 1 - BRANCH_DEATH_PROBABILITY / self.power
		return self.is_alive


def main():
	turtle.Screen().bgcolor(DARK_BLUE)
	branches = [Branch()]
	min_y = 0
	at_least_one_branch_alive = True
	while at_least_one_branch_alive and min_y > BOTTOM:
		at_least_one_branch_alive = False
		for b in branches:
			if not b.is_alive:
				continue
			b.draw_line()
			is_new_branch_needed = random() < NEW_BRANCH_PROBABILITY
			if is_new_branch_needed:
				branches += [Branch(b)]
			if b.p.ycor() < min_y:
				min_y = b.p.ycor()
			if b.decide_if_alive():
				at_least_one_branch_alive = True
			


main()
input()
