import turtle 
import datetime

def draw_hour_arrow(hour):
	p = turtle.Pen()
	p.setheading(90)
	angle = 360 / 12 * hour
	p.right(angle)
	p.pensize(13)
	p.color(45, 45, 45)
	p.backward(76)
	p.forward(332)


def draw_minute_arrow(minute):
	p = turtle.Pen()
	p.setheading(90)
	angle = 360 / 60 * minute
	print(angle)
	p.right(angle)
	p.pensize(12)
	p.color(45, 45, 45)
	p.backward(76)
	p.forward(447)


def main():
	turtle.Screen().bgpic("clock.gif")
	turtle.Screen().colormode(255)
	now = datetime.datetime.now()
	hour = now.hour + now.minute / 60
	minute = now.minute + now.second / 60
	print(minute)
	draw_hour_arrow(hour)
	draw_minute_arrow(minute)
	turtle.exitonclick()


main()