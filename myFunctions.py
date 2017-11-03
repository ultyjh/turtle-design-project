#function file
#square

def polygon(t,s,d):
    a = 360/s
    for times in range(s):
        t.forward(d)
        t.right(a)

    
def polygonFill(t,s,d,c):
    a=360/s
    t.color(c)
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.right(a)
    t.end_fill()

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def cool(t,d,c1,c2):
    t.color(c1)
    polygon(t,4,d,c1)
    t.color(c2)
    polygon(t,3,d,c2)

def gweb(t):
    for times in range(50):
        t.color(times,times,0)
        t.circle(times*10)
def pweb(t):
    for times in range(50):
        t.color(times,0,times)
        t.circle(times*10)


                
