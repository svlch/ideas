from turtle import*

t = Turtle()
bgcolor('white')
t.pencolor('blue')
t.speed(0)

for i in range(320):
  t.circle(190-i, 90)
  t.left(90)
  t.circle(190-i, 90)
  t.left(18)
  if i > 190:
    t.pensize(3)
