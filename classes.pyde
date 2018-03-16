from MyLib_1 import *

BGC = color(200)
v1 = None
v2 = None

def setup():
    global v1,v2
    size(600,600)
    v1 = Vector(width/2,height/2)
    v2 = Vector(width/2,height/2)
    
def draw():
    global BGC
    background(BGC)
    drawVectors()
    
def drawVectors():
    global v1,v2
    temp1 = Vector(0,1)
    temp2 = Vector(1,0)
    global v1,v2
    v1.addVector(temp1)
    v2.addVector(temp2)
    wrap(v1)
    wrap(v2)
    ellipse(v1.x,v1.y,25,25)
    ellipse(v2.x,v2.y,15,15)
    
def wrap(vec):
    if vec.x > width:
        vec.x =0
    if vec.y > height:
        vec.y = 0