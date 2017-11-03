import turtle
from myFunctions import*
from random import*
bob = turtle.Turtle()
turtle.bgcolor("black")
turtle.colormode(255)
bob.speed(11)
bob.width(1)
c = (255,0,0)



jump(bob,randint(-500,-300),randint(-500,-300))
gweb(bob)
jump(bob,0,0)
gweb(bob)
jump(bob,randint(300,500),randint(-500,-300))
gweb(bob)
jump(bob,randint(-300,0),randint(-500,-300))
gweb(bob)

jump(bob,randint(-600,-400),randint(-600,-400))
pweb(bob)
jump(bob,300,300)
pweb(bob)
jump(bob,randint(400,600),randint(-600,-400))
pweb(bob)
jump(bob,0,randint(-600,-400))
pweb(bob)

for times in range(75):
     c=(100,100,100)
     y=randint(2,8)
     bob.begin_fill()
     for times in range(8):
          bob.color(c)
          bob.circle(y)
     jump(bob,randint(-900,900),randint(-500,500))
     bob.end_fill()

for times in range(75):
     c=(160,160,0)
     y=randint(2,8)
     bob.begin_fill()
     for times in range(8):
          bob.color(c)
          bob.circle(y)
     jump(bob,randint(-900,900),randint(-500,500))
     bob.end_fill()


jump(bob,100,-100)
for times in range(100):
    polygonFill(bob,3,100,(0,times,times))
    bob.forward(times)
    bob.right(120)
jump(bob,-100,-100)
for times in range(100):
    polygonFill(bob,3,100,(times,times,0))
    bob.forward(times)
    bob.right(120)
jump(bob,0,0)
for times in range(100):
    polygonFill(bob,3,100,(times,0,0))
    bob.forward(times)
    bob.right(120)
jump(bob,100,100)
for times in range(100):
    polygonFill(bob,3,100,(0,times,0))
    bob.forward(times)
    bob.right(120)
jump(bob,-100,100)
for times in range(100):
    polygonFill(bob,3,100,(0,0,times))
    bob.forward(times)
    bob.right(120)




