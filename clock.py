import turtle 
import datetime

class Clock(object):
	def __init__(self):
		self.hour_pen = turtle.Pen()
		self.minute_pen = turtle.Pen()
		self.second_pen = turtle.Pen()


	def draw_clock(self):
		turtle.Screen().tracer(False)
		turtle.Screen().bgpic("clock.gif")
		now = datetime.datetime.now()
		hour = now.hour + now.minute / 60
		minute = now.minute + now.second / 60
		second = now.second
		self.draw_hour_arrow(hour)
		self.draw_minute_arrow(minute)
		self.draw_second_arrow(second)
		turtle.Screen().tracer(True)
		turtle.Screen().ontimer(self.draw_clock, 1000)

	def draw_arrow(self, p, angle, pen_size, color, tail_length, length):
		p.reset()
		p.setheading(90)
		p.right(angle)
		p.pensize(pen_size)
		p.color(color)
		p.backward(tail_length)
		p.forward(length)

	def draw_hour_arrow(self, hour):
		self.draw_arrow(
			self.hour_pen,
			angle=360 / 12 * hour,
			pen_size=13, 
			color=(45, 45, 45),
			tail_length=76,
			length=332)

	def draw_minute_arrow(self, minute):
		self.draw_arrow(
			self.minute_pen,
			angle=360 / 60 * minute,
			pen_size=12, 
			color=(45, 45, 45),
			tail_length=76,
			length=447)

	def draw_second_arrow(self, second):
		self.draw_arrow(
			self.second_pen,
			angle=360 / 60 * second,
			pen_size=5, 
			color=(180, 33, 33),
			tail_length=44,
			length=440)


def main():
	turtle.Screen().colormode(255)
	clock = Clock()
	clock.draw_clock()
	turtle.exitonclick()


main()