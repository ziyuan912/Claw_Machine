from __future__ import division, print_function
from visual import *
from random import *
scene.width = scene.height = 800
yes = 2
I = 20
cycle = 1000
left = box(pos=(-45,-15,0), height=40, width = 10, color = color.yellow)
bottom = box(pos=(-12,-34,0), height=2, length = 65,width = 10, color = color.yellow)
 
def clickFunc():
    if scene.mouse.clicked:
        m = scene.mouse.getclick()
        loc = m.pos
        metal = box(pos=(loc.x, loc.y, 0), mass = 5,length = 3,height = 3,width = 3, color=(random(), random(), random()),
                    f = vector(0,0,0) ,Xm = randint(600,200000), p =  vector(0,0,0),flag = 1)
        metals.append(metal)
 
b=box(pos=vector(0,31,0),length=90, height=5, width=25,color=color.yellow)
a=box(pos=vector(40,-30,0),length=40, height=5, width=25,color=color.yellow)
rod2 = cylinder(pos=(40,-30,0),axis=(0,60,0), radius=5,color=color.yellow)
rod3 = cylinder(pos=(0,5,0),axis=(0,52,0), radius=1)
magnet = cylinder(pos=(0,-5,0),axis=(0,10,0), radius=5)
spring = helix(pos=(0,-5,0),axis=(0,10,0),radius=5.2,length=10,coils=15,color=color.red,thickness=5.2/10)
vmagnet=vector(-1,0,0)
vgoingdown = vector(0,-1,0)
dt=0.01
metals = []
N = 5
t = 0
Fb = vector(0,0,0)
ball = sphere(pos=vector(0,-5,-5), radius=1, color=color.cyan)
vbally=vector(0,1,0)
flag = 1
 
can1 = ring(pos = (24.5, -16, 0), radius = 10, axis = (0,1,0), thickness = 3,color=color.red)
can2 = ring(pos = (24.5, -16-3, 0), radius = 10, axis = (0,1,0), thickness = 3,color=color.orange)
can3 = ring(pos = (24.5, -16-6, 0), radius = 10, axis = (0,1,0), thickness = 3,color=color.green)
can1 = ring(pos = (24.5, -16-9, 0), radius = 10, axis = (0,1,0), thickness = 3,color=color.cyan)
can1 = ring(pos = (24.5, -16-12, -2), radius = 10, axis = (0,1,0), thickness = 3,color=color.blue)
 
 
for i in range(N):
    position = vector(randint(-25,10),-30,0)
    metal = box(pos = position, mass = 5,length = 3,height = 3,width = 3, color=(random(), random(), random()),
                f = vector(0,0,0) ,Xm = randint(600,200000), p =  vector(0,0,0),flag = 1)
    metals.append(metal)
 
 
while True:
    rate(1000)
    clickFunc()
    t += dt
    magnet.pos+=dt*vmagnet
    rod3.pos+=dt*vmagnet
    spring.pos+=dt*vmagnet
    ball.pos+=(0.06*cos(t),0,0.06*sin(t))
    ball.pos+=dt*vmagnet
    ball.pos+=0.1*dt*vbally
    if abs(ball.pos.y-magnet.pos.y)>=10:
        ball.pos.y=magnet.pos.y
    for metal in metals:  #here
        Fb = norm(magnet.pos-(0,1,0)-metal.pos)*6e-7*metal.Xm*I*cycle*pi*5.2*5.2/(mag2(magnet.pos-(0,1,0)-metal.pos)*mag2(magnet.pos-(0,1,0)-metal.pos))*metal.flag
        while Fb.y-9.8*metal.mass < 0 and metal.pos.y <= -30:
            Fb.y = 9.8*metal.mass
        if mag(metal.pos - (magnet.pos-(0,1,0))) >= 3:
            metal.f = Fb+vector(0,-9.8*metal.mass,0)
            metal.p = metal.p + metal.f*dt
            metal.pos = metal.pos+(metal.p)*dt/metal.mass
        if mag(metal.pos - (magnet.pos-(0,1,0))) < 3:
            metal.f = (0,0,0)
            metal.pos += dt*vmagnet
        if (metal.pos.x) > 11.5 and metal.pos.y <= -30 and metal.flag != 0:
            metal.p.x = -1*metal.p.x
            metal.pos.x = 11.5
        elif (metal.pos.x) < -43 and metal.pos.y <= -30:
            metal.p.x = -1*metal.p.x
            metal.pos.x = -43
        if metal.pos.y <= -30:
            metal.pos.y = -30
            metal.p.y = 0
    t1=t
    if scene.kb.keys:
        s = scene.kb.getkey()
        if s == "down":
            while spring.pos.y >= -27:
                rate(1000)
                t1+=dt
                magnet.pos+=dt*vgoingdown
                rod3.pos+=dt*vgoingdown
                spring.pos+=dt*vgoingdown
                ball.pos+=(0.06*cos(t1),0,0.06*sin(t1))
                ball.pos+=dt*vgoingdown
                ball.pos+=0.1*dt*vbally
                if abs(ball.pos.y-magnet.pos.y)>=10:
                    ball.pos.y=magnet.pos.y
                for metal in metals:  #here
                    Fb = norm(magnet.pos-(0,1,0)-metal.pos)*6e-7*metal.Xm*I*cycle*pi*5.2*5.2/(mag2(magnet.pos-(0,1,0)-metal.pos)*mag2(magnet.pos-(0,1,0)-metal.pos))*metal.flag
                    while Fb.y-9.8*metal.mass < 0 and metal.pos.y <= -30:
                        Fb.y = 9.8*metal.mass
                    if mag(metal.pos - (magnet.pos-(0,1,0))) >= yes:
                        metal.f = Fb+vector(0,-9.8*metal.mass,0)
                        metal.p = metal.p + metal.f*dt
                        metal.pos = metal.pos+(metal.p)*dt/metal.mass
                    if mag(metal.pos - (magnet.pos-(0,1,0))) < yes:
                        metal.f = (0,0,0)
                        metal.pos += dt*vgoingdown
                    if (metal.pos.x) > 11.5 and metal.pos.y <= -30 and metal.flag != 0:
                        metal.p.x = -1*metal.p.x
                        metal.pos.x = 11.5
                    elif (metal.pos.x) < -43 and metal.pos.y <= -30:
                        metal.p.x = -1*metal.p.x
                        metal.pos.x = -43
                    if metal.pos.y <= -30:
                        metal.pos.y = -30
                        metal.p.y = 0
            vgoingdown =- vgoingdown
            while spring.pos.y <= -5:
                rate(1000)
                t1+=dt
                magnet.pos+=dt*vgoingdown
                rod3.pos+=dt*vgoingdown
                spring.pos+=dt*vgoingdown
                ball.pos+=(0.06*cos(t1),0,0.06*sin(t1))
                ball.pos+=dt*vgoingdown
                ball.pos+=0.1*dt*vbally
                if abs(ball.pos.y-magnet.pos.y)>=10:
                    ball.pos.y=magnet.pos.y
                for metal in metals:  #here
                    Fb = norm(magnet.pos-(0,1,0)-metal.pos)*6e-7*metal.Xm*I*cycle*pi*5.2*5.2/(mag2(magnet.pos-(0,1,0)-metal.pos)*mag2(magnet.pos-(0,1,0)-metal.pos))*metal.flag
                    while Fb.y-9.8*metal.mass < 0 and metal.pos.y <= -30:
                        Fb.y = 9.8*metal.mass
                    if mag(metal.pos - (magnet.pos-(0,1,0))) >= yes:
                        metal.f = Fb+vector(0,-9.8*metal.mass,0)
                        metal.p = metal.p + metal.f*dt
                        metal.pos = metal.pos+(metal.p)*dt/metal.mass
                    if mag(metal.pos - (magnet.pos-(0,1,0))) < yes:
                        metal.f = (0,0,0)
                        metal.pos += dt*vgoingdown
                    if (metal.pos.x) > 11.5 and metal.pos.y <= -30 and metal.flag != 0:
                        metal.p.x = -1*metal.p.x
                        metal.pos.x = 11.5
                    elif (metal.pos.x) < -43 and metal.pos.y <= -30:
                        metal.p.x = -1*metal.p.x
                        metal.pos.x = -43
                    if metal.pos.y <= -30:
                        metal.pos.y = -30
                        metal.p.y = 0
            vgoingdown =- vgoingdown
        elif s == "up":
            I = 0
            status = 1
            for metal in metals:
                if metal.pos.y > -20:
                    metal.p = vector(0,0,0)
               # print (metal.p)
            while status == 1:
                rate(1000)
                t += dt
                for metal in metals:
                    if metal.pos.y <= -30 and metal.p.y != 0:
                        metal.flag = 0
                        metal.p.y = 0
                    metal.p += 9.8*metal.mass*vector(0,-1,0)*dt*metal.flag
                    metal.pos += metal.p*dt/metal.mass
                    if (metal.pos.x) > 11.5 and metal.pos.y <= -30 and metal.p.x != 0:
                        metal.p.x = -1*metal.p.x
                        metal.pos.x = 11.5
                    elif (metal.pos.x) < -43 and metal.pos.y <= -30:
                        metal.p.x = -1*metal.p.x
                        metal.pos.x = -43
                    #print (metal.p)
                    if scene.kb.keys:
                        s = scene.kb.getkey()
                        if s == "up":
                            status = 0
                            I = 20
                            for metal in metals:
                                if metal.pos.x < 11.5:
                                    metal.flag = 1
                        else:
                            continue
            t=t1
        else:
            continue
    if magnet.pos.x>=25:
        vmagnet=-vmagnet
    elif magnet.pos.x<=-40:
        vmagnet=-vmagnet
 
 
 
