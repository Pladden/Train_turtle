from random import random
import math
import turtle
import json

SKY_COLOR = (0, 0, 20)
MAX_POWER_COLOR = (220, 220, 255)
MAX_Y = turtle.Screen().window_height()//2
TOP = MAX_Y
BOTTOM = -MAX_Y
MAX_LINE_LENGTH = 20
MAX_ANGLE = 180
MAX_POWER = 7
MAX_SPEED = 0
NEW_BRANCH_PROBABILITY = 0.05 # 10%
BRANCH_DEATH_PROBABILITY = 0.07
MAX_GRADIENT_WIDTH = 200

class Branch(object):
	def __init__(self, parent_branch=None):
		self.p = turtle.Pen()
		self.p.hideturtle()
		self.p.speed(MAX_SPEED)
		self.p.color(MAX_POWER_COLOR)
		self.p.penup()
		if parent_branch:
			self.start_position = parent_branch.p.position()
			self.power = math.ceil(parent_branch.power / 3)
		else:
			self.start_position = (0, TOP)
			self.power = MAX_POWER
		self.p.setposition(self.start_position)
		self.is_alive = True
		self.p.pendown()
		self.vectors = []

	def draw_line(self):
		angle = round(random() * MAX_ANGLE)
		self.p.setheading(0)
		self.p.right(angle)
		distance = round(random() * MAX_LINE_LENGTH)
		vector = {'angle': angle, 'distance': distance}
		self.vectors += [vector]
		self.p.forward(distance)
		
	def draw_layer(self, color, pensize):
		pensize = math.ceil(pensize * self.power / MAX_POWER)
		self.p.pensize(pensize)
		self.p.color(color)
		self.p.penup()
		self.p.setposition(self.start_position)
		self.p.pendown()
		for vector in self.vectors:
			angle = vector['angle']
			distance = vector['distance']
			self.p.setheading(0)
			self.p.right(angle)
			self.p.forward(distance)

	def serialize(self):
		result = dict(
			start_position=self.start_position,
			power=self.power,
			vectors=self.vectors)
		return result

	def deserialize(self, b):
		self.start_position = b['start_position']
		self.power = b['power']
		self.vectors = b['vectors']

	def decide_if_alive(self):
		self.is_alive = random() < 1 - BRANCH_DEATH_PROBABILITY / self.power
		return self.is_alive


def build_lightning_branches():
	turtle.Screen().tracer(False)
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
	turtle.Screen().tracer(True)
	return branches


def draw_lightning_branches_by_layers(branches):
	n_layers = MAX_GRADIENT_WIDTH // 2	
	for layer_index in range(n_layers):
		color = [0, 0, 0]
		x = n_layers - 1 - layer_index
		for i in range(3):
			c = round(SKY_COLOR[i] + (x - 100)**6 / 4e9) - (255 - MAX_POWER_COLOR[i])
			color[i] = max(0, min(c, 255))
		pensize = MAX_GRADIENT_WIDTH - layer_index * 2
		turtle.Screen().tracer(False)
		for b in branches:
			b.draw_layer(color, pensize)
		turtle.Screen().tracer(True)


def save_lightning_branches(branches, file_name="lightning.json"):
	serialized_branches = []
	for branch in branches:
		serialized_branches += [branch.serialize()]
	result = json.dumps(serialized_branches)
	with open(file_name, 'w') as f:
		f.write(result)


def initialize_screen():
	turtle.Screen().colormode(255)
	turtle.Screen().bgcolor(*SKY_COLOR)


def main():
	file_name = input('Enter a file name to load from it (empty enter will generate a new one): ')
	initialize_screen()
	if file_name:
		branches = load_lightning_branches(file_name)
	else: 
		branches = build_lightning_branches()
		save_lightning_branches(branches)
	draw_lightning_branches_by_layers(branches)
	

def load_lightning_branches(file_name):
	with open(file_name) as f:
		content = f.read()
	serialized_branches = json.loads(content)
	branches = []
	for b in serialized_branches:
		new_branch = Branch()
		new_branch.deserialize(b)
		branches += [new_branch]
	return branches


main()
input()
