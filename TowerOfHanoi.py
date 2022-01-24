import turtle

BasePL=10
TowerP=5
TowerW=100
TowerH=300
TowerSpace=300
HORIZON=-100
PMS=2

Isjump=True

POLES={
    "1": [],
    "2": [],
    "3": [],
}

SCR=turtle.Screen()

def init_plate(pi=5):
    _pi=pi+2
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.begin_poly()
    t.left(90)
    t.forward(BasePL*_pi)
    t.circle(BasePL, 180)
    t.forward(BasePL * 2 * _pi)
    t.circle(BasePL, 180)
    t.forward(BasePL * _pi)
    t.end_poly()
    p = t.get_poly()
    pname='plate_%s'%pi
    SCR.register_shape(pname, p)

def init_tower():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.begin_poly()
    t.left(90)
    t.forward(TowerW)
    t.circle(-TowerP, 180)
    t.forward(TowerW)
    t.forward(TowerW)
    t.circle(-TowerP, 180)
    t.forward(TowerW-TowerP/2)
    t.left(90)
    t.forward(TowerH)
    t.circle(-TowerP, 180)
    t.forward(TowerH)
    t.end_poly()
    p = t.get_poly()
    SCR.register_shape('tower', p)

def moveTower(Plates,fromP,toP,midP):
    
    if len(Plates)>1:
       
        moveTower(Plates[1:], fromP, midP, toP)
        
        moveDisk(Plates[0],fromP, toP)
        
        moveTower(Plates[1:], midP, toP, fromP)
    else:
        moveDisk(Plates, fromP, toP)

def moveDisk(Plates, fromP, toP):
    if not (isinstance(Plates,list) or isinstance(Plates,tuple)):
        Plates=[Plates]

    for p in Plates:
        p.penup()

        mx = (toP - 2) * TowerSpace
        my = HORIZON + len(POLES[str(toP)]) * BasePL * 2

        if fromP!=None:
            POLES[str(fromP)].remove(p)
            if Isjump:
                px,py=p.pos()
                p.goto(px,TowerH+py)
                p.goto(mx,TowerH+py)

        p.goto(mx, my)
        POLES[str(toP)].append(p)

def get_plates(pn):
    plates=[]
    for i in range(pn):
        init_plate(i)
        _plate='plate_%s'%i
        _p=turtle.Turtle(_plate)
        _p.color("green","cyan")
        _p.speed(PMS)
        plates.append(_p)

    return plates[::-1]

def show_towers():
    init_tower()
    for tx in [-TowerSpace,0,TowerSpace]:
        t3 = turtle.Turtle('tower')
        t3.penup()
        t3.goto(tx,HORIZON)
        print (t3.pos())

if __name__ == '__main__':
    show_towers()
    plates = get_plates(5)
    moveDisk(plates,None,1)
    moveTower(plates, 1, 3, 2)
    turtle.done()
