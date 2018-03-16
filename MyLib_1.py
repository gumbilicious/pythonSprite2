############################################################
# import statements
############################################################
import math
import time
############################################################
# modification of a series of classes developed for
# use with p5.js
############################################################
############################################################
############################################################
############################################################
############################################################
############################################################
# series of utility functions
############################################################
def distance(x1, y1, x2, y2):
    modX = (max(x1, x2) - min(x1, x2)) ** 2
    modY = (max(y1, y2) - min(y1, y2)) ** 2
    return (modX + modY) ** .5

def angle(x1, y1, x2, y2):
    return atan2(y2 - y1, x2 - x1)

def myRange(start, end, step=None):
    if step == None:
        step = 1
    while start <= end:
        yield start
        start += step
############################################################
############################################################
############################################################
############################################################
############################################################
# Vector Class
#
############################################################
class Vector(object):
############################################################
# constructor
############################################################
    def __init__(self, x, y):
        self.x = x
        self.y = y
############################################################
# sets the vector to x,y scalar values
############################################################
    def set(self, x, y):
        self.x = x
        self.y = y
############################################################
# copies values from another vector
############################################################
    def setVector(self, vec):
        self.x = vec.x
        self.y = vec.y
############################################################
# adds itself to another passed vector
############################################################
    def addVector(self, vec):
        self.x += vec.x
        self.y += vec.y
############################################################
# subtracts another vector from itself
############################################################
    def subtractVector(self, vec):
        self.x -= vec.x
        self.y -= vec.y
############################################################
# multiplies a vector to itself
############################################################
    def multiplyVector(self, vec):
        self.x *= vec.x
        self.y *= vec.y
############################################################
# multiplies a scalar value to both vector component values
############################################################
    def multiplyScalar(self, scalar):
        self.x *= scalar
        self.y *= scalar
############################################################
# returns the dot product of itself and another passed vector
############################################################
    def dotProduct(self, vec):
        return ((self.x * vec.x) + (self.y * vec.y))
############################################################
# returns the distance of itself and another passed vector
############################################################
    def dist(self, vec):
        return distance(self.x, self.y, vec.x, vec.y)
############################################################
# returns the scalar magnitude value of a vector
############################################################
    def magnitude(self):
        return distance(0, 0, self.x, self.y)
############################################################
# returns the angle of the scalar magnitude of the vector
############################################################
    def getAngle(self):
        return angle(0, 0, self.x, self.y)
############################################################
# sets the vector in proportion of the passed angle at
# a total vector magnitude of 1, or of the passed magnitude
############################################################
    def setAngle(self, angle,magnitude = None):
        self.x = cos(angle)
        self.y = sin(angle)
        if magnitude != None:
            self.multiplyScalar(magnitude)
############################################################
# returns a formatted string of the vector components
############################################################
    def toString(self):
        return str(self.x) + " : " + str(self.y)
############################################################
############################################################
############################################################
############################################################
############################################################
############################################################
# a series of boolean variables monitoring whether particular
# keyboard keys are pressed
############################################################
class Controls(object):
############################################################
# 
############################################################
    def __init__(self):
        self.left = False
        self.up = False
        self.right = False
        self.down = False
        self.space = False
        self.ctrl = False
        self.shift = False
############################################################
# 
############################################################
    def activate(self):
        if(keyCode == 37):
            self.left = True
        if(keyCode == 38):
            self.up = True
        if(keyCode == 39):
            self.right = True
        if(keyCode == 40):
            self.down = True
        if(keyCode == 32):
            self.space = True
        if(keyCode == 16):
            self.shift = True
        if(keyCode == 17):
            self.ctrl = True
############################################################
# 
############################################################
    def deactivate(self):
        if(keyCode == 37):
            self.left = False
        if(keyCode == 38):
            self.up = False
        if(keyCode == 39):
            self.right = False
        if(keyCode == 40):
            self.down = False
        if(keyCode == 32):
            self.space = False
        if(keyCode == 16):
            self.shift = False
        if(keyCode == 17):
            self.ctrl = False
############################################################
# 
############################################################
    def toString(self):
        L = "L:" + str(self.left)
        U = " U:" + str(self.up)
        R = " R:" + str(self.right)
        D = " D:" + str(self.down)
        SP = " Space:" + str(self.space)
        SH = " Shift:" + str(self.shift)
        C = " C:" + str(self.ctrl)
        temp = L + U + R + D + SP + SH + C
        return temp
############################################################
############################################################
############################################################
############################################################
############################################################
############################################################
# CS(Coordinate System), allows for a larger mapping scheme
# outside of the canvas's boundaries
############################################################
class CS(object):
############################################################
# 
############################################################
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.originX = 0
        self.originY = 0
############################################################
# 
############################################################
    def setOrigin(self, x, y):
        self.originX = x
        self.originY = y
############################################################
# 
############################################################
    def moveOrigin(self, x, y):
        self.originX += x
        self.originY += y
############################################################
# 
############################################################
    def toString(self):
        W = "W:" + str(self.width)
        H = " H:" + str(self.height)
        X = " X:" + str(self.originX)
        Y = " Y:" + str(self.originY)
        return W + H + X + Y
############################################################
############################################################
############################################################
############################################################
############################################################
############################################################
# makes an array of Ball objects that behaves as a dynamic
# star field
############################################################
class Starfield(object):
############################################################
# 
############################################################
    def __init__(self, starCount, minStarSize, maxStarSize, cs=None):
        self.starCount = starCount  # initial number of stars in array
        self.stars = []  # star array
        self.minStarSize = minStarSize  # minimum size of stars
        self.maxStarSize = maxStarSize  # maximum size of stars
        if cs == None:
            self.CS = CS(width, height)
        else:
            self.CS = CS
        # how stars react to the boundary
        # can be set to "wrap" or "rebound", any other value will
        # make stars not react to the boundary
        self.boundaryHandling = "wrap"

        for i in range(0, self.starCount):
            x = random(0, self.CS.width)
            y = random(0, self.CS.height)
            size = random(self.minStarSize, self.maxStarSize)
            self.stars.append(Ball(x, y, size))
############################################################
# 
############################################################
    def draw(self):
        for i in range(0, len(self.stars)):
            pushStyle()
            noStroke()
            self.stars[i].move()
            self.stars[i].drawZone()
            if self.boundaryHandling == "wrap":
                self.stars[i].wrap()
            elif self.boundaryHandling == "rebound":
                self.stars[i].rebound()
            else:
                self.stars[i].wrap()
            popStyle()
############################################################
# 
############################################################
    def push(self):
        for i in range(0, len(self.stars)):
            self.stars[i].push()
############################################################
# 
############################################################
    def setAngle(self, angle):
        for i in range(0, len(self.stars)):
            self.stars[i].angle = angle
############################################################
# 
############################################################
    def setForce(self, force):
        for i in range(0, len(self.stars)):
            self.stars[i].force = force
############################################################
# 
############################################################
    def setSpeedLimit(self, max):
        for i in range(0, len(self.stars)):
            self.stars[i].maxSpeed = max
############################################################
# 
############################################################
    def setFriction(self, friction):
        for i in range(0, len(self.stars)):
            self.stars[i].friction = friction
############################################################
# 
############################################################
    def setColor(self, R, G=None, B=None):
        if G == None and B == None:
            for i in range(0, len(self.stars)):
                self.stars[i].setColor(R)
        else:
            for i in range(0, len(self.stars)):
                self.stars[i].setColor(R, G, B)

############################################################
############################################################
############################################################
############################################################
############################################################
############################################################
# makes a Ball sprite, r is radius
############################################################
class Ball(object):
############################################################
# 
############################################################
    def __init__(self, x, y, diameter):
        self.color = color(255)
        self.CS = CS(width, height)
        self.p = Vector(x, y)  # position vector
        self.v = Vector(0, 0)  # velocity vector
        self.a = Vector(0, 0)  # acceleration vector
        self.g = Vector(0, 0)  # gravity vector
        self.f = Vector(0, 0)  # force vector
        self.r = diameter / 2  # radius
        self.maxSpeed = 100  # used for speed limit
        self.angle = 0  # used for rotation and direction
        self.isTurned = False  # used for rotation state
        self.isPushed = False  # if force is acting on sprite
        self.force = 1  # magnitude of foce applied to sprite
        self.mass = 1  # mass of sprite
        self.img = "img/default.jpg"  # will be used for an image for sprite
        self.friction = 0  # friction coefficient
        self.spinFriction = 0  # friction applied to spin
        self.inelastic = 1  # inelastic collision coefficient
        self.spin = 0  # angular momentum
############################################################
#
############################################################

    def setCS(self, CS):
        self.CS = CS
############################################################
#
############################################################

    def setPos(self, x, y):
        self.p.x = x
        self.p.y = y
############################################################
#
############################################################

    def setVel(self, x, y):
        self.v.x = x
        self.v.y = y
############################################################
#
############################################################

    def setColor(self, R, G=None, B=None):
        if G == None and B == None:
            self.color = color(R)
        else:
            self.color = color(R, G, B)
############################################################
#
############################################################

    def setImg(self, filePath=None):
        if filePath != None:
            self.img = loadImage(filePath)
        else:
            self.img = loadImage(self.img)
############################################################
#
############################################################

    def getCSX(self):
        return self.p.x + self.CS.originX
############################################################
#
############################################################

    def getCSY(self):
        return self.p.y + self.CS.originY
############################################################
#
############################################################

    def drawZone(self):
        pushStyle()
        if self.color != None:
            fill(self.color)
        x = self.p.x + self.CS.originX
        y = self.p.y + self.CS.originY
        ellipse(x, y, self.r * 2, self.r * 2)
        popStyle()
############################################################
#
############################################################

    def drawImg(self):
        pushStyle()
        translate(self.p.x + self.CS.originX, self.p.y + self.CS.originY)
        rotate(self.angle)
        imageMode(CENTER)
        image(self.img, 0, 0, self.r * 2, self.r * 2)
        ellipse(0, 0, 25, 25)
        popStyle()
############################################################
#
############################################################

    def drawCSGrid(self, xStep=None, yStep=None):
        if xStep == None:
            xStep = 75
        if yStep == None:
            yStep = 75
        for i in myRange(0, self.CS.height, yStep):
            p1x = self.CS.originX
            p1y = self.CS.originY + i
            p2x = self.CS.width + self.CS.originX
            p2y = self.CS.originY + i
            line(p1x, p1y, p2x, p2y)
        for i in myRange(0, self.CS.width, xStep):
            p1x = self.CS.originX + i
            p1y = self.CS.originY
            p2x = self.CS.originX + i
            p2y = self.CS.height + self.CS.originY
            line(p1x, p1y, p2x, p2y)
############################################################
#
############################################################

    def drawCSBoundary(self):
        # top
        p1x = self.CS.originX
        p1y = self.CS.originY
        p2x = self.CS.width + self.CS.originX
        p2y = self.CS.originY
        line(p1x, p1y, p2x, p2y)
        # bottom
        p1x = self.CS.originX
        p1y = self.CS.originY + self.CS.height
        p2x = self.CS.width + self.CS.originX
        p2y = self.CS.originY + self.CS.height
        line(p1x, p1y, p2x, p2y)
        # left
        p1x = self.CS.originX
        p1y = self.CS.originY
        p2x = self.CS.originX
        p2y = self.CS.height + self.CS.originY
        line(p1x, p1y, p2x, p2y)
        # right
        p1x = self.CS.originX + self.CS.width
        p1y = self.CS.originY
        p2x = self.CS.originX + self.CS.width
        p2y = self.CS.height + self.CS.originY
        line(p1x, p1y, p2x, p2y)
############################################################
#
############################################################

    def setCenter(self):
        self.CS.setOrigin((width / 2) - self.p.x, (height / 2) - self.p.y)
############################################################
#
############################################################

    def edgeLockCS(self):
        if width < self.CS.width and height < self.CS.height:
            if (width - self.CS.originX) > self.CS.width:
                self.CS.originX = -(self.CS.width - width)
            if self.CS.originX > 0:
                self.CS.originX = 0
            if (height - self.CS.originY) > self.CS.height:
                self.CS.originY = -(self.CS.height - height)
            if self.CS.originY > 0:
                self.CS.originY = 0
############################################################
#
############################################################

    def circInt(self, ball):
        master = False
        if distance(self.p.x, self.p.y, ball.p.x, ball.p.y) < (self.r + ball.r):
            master = True
        return master
############################################################
#
############################################################

    def pointInt(self, x, y):
        master = False
        if distance(self.getCSX(), self.getCSY(), x, y) < self.r:
            master = True
        return master
############################################################
# based on collision2, and unideal elastic collision
# still needs to be tested
############################################################

    def collision(self, ball):
        a1 = angle(self.p.x, self.p.y, ball.p.x, ball.p.y)
        a2 = angle(ball.p.x, ball.p.y, self.p.x, self.p.y)
        mTot = (self.mass * self.v.magnitude()) + \
            (ball.mass * ball.v.magnitude())
        m1 = (mTot / 2) / self.mass
        m2 = (mTot / 2) / ball.mass

        self.v.setAngle(a2)
        ball.v.setAngle(a1)
        self.v.multiplyScalar(m1 * self.inelastic)
        ball.v.multiplyScalar(m2 * self.inelastic)
############################################################
#
############################################################

    def move(self):
        self.f.set(0, 0)  # intializes force vector
        if self.isPushed:
            self.f.setAngle(self.angle)  # assigns angle/direction of force
            self.f.multiplyScalar(self.force)  # applies magnitude of force
        if self.spin != 0:
            tempAngle = self.v.getAngle()
            tempSpeed = self.v.magnitude()
            self.v.setAngle(tempAngle + self.spin)
            self.v.multiplyScalar(tempSpeed)
        self.a.setVector(self.f)  # copies f to a
        # corrects force by applying mass to a = F/m
        self.a.multiplyScalar(1 / self.mass)
        self.a.addVector(self.g)  # applies gravity
        self.v.addVector(self.a)  # adds acceleration to velocity
        self.v.multiplyScalar(1 - self.friction)  # applies friction
        self.spin = self.spin * (1 - self.spinFriction)
        self.speedLimit()
        self.p.addVector(self.v)  # makes new position
############################################################
#
############################################################

    def push(self):
        self.isPushed = True
        self.move()
        self.isPushed = False
############################################################
#
############################################################

    def speedLimit(self):
        if self.maxSpeed != None:
            if self.v.magnitude() > self.maxSpeed:
                self.v.setAngle(self.v.getAngle())
                self.v.multiplyScalar(self.maxSpeed)
############################################################
#
############################################################

    def wrap(self):
        if (self.p.x - self.r) > self.CS.width:
            self.p.x = -self.r
        elif(self.p.x + self.r) < 0:
            self.p.x = self.CS.width + self.r
        if (self.p.y - self.r) > self.CS.height:
            self.p.y = -self.r
        elif(self.p.y + self.r) < 0:
            self.p.y = self.CS.height + self.r

############################################################
#
############################################################
    def rebound(self):
        if (self.p.x + self.r) > self.CS.width:
            self.v.x = -self.v.x
        elif(self.p.x - self.r) < 0:
            self.v.x = -self.v.x
        if (self.p.y + self.r) > self.CS.height:
            self.v.y = -self.v.y
        elif(self.p.y - self.r) < 0:
            self.v.y = -self.v.y

############################################################
############################################################
############################################################
############################################################
############################################################
############################################################
# makes a Mini Map object, the Mini Map contains canvas and
# coordinate system (CS) information as well as an array of objects to
# draw on the map.
# The Mini Map will show the entire coordinate system, the target
# locations in that coordinate system and the current canvas view
# of the coordinate system.
############################################################

class MiniMap(object):
############################################################
# 
############################################################
    def __init__(self, cs):
        self.scaleDownFactor = 10  # divides CS dimension by this number
        self.CS = cs  # coordinate system
        self.width = self.CS.width / self.scaleDownFactor  # width of map
        self.height = self.CS.height / self.scaleDownFactor  # height of map
        self.p = Vector(0, 0)  # position vector of miniMap
        self.targets = []  # array of sprite objects
        # size of targets drawn on map, targets are not automatically scaled
        self.targetSize = 3
        # map background color, default translucent green
        self.mapColor = color(0, 128, 0, 128)
        # map target color, default white no stroke
        self.targetColor = color(255)
        self.frameColor = color(0)  # map view frame color, default black
        self.posValue = 1
        self.setPosition(1)

############################################################
# sets the position vector based either on fixed x and y coordinates
# on the canvas or by selecting a preset position with a single number
#  1 - top left
#  2 - top right
#  3 - bottom right
#  4 - bottom left
#  1--2
#  |  |
#  4--3
############################################################
############################################################
# 
############################################################
    def setPosition(self, x, y=None):
        if y == None:
            self.posValue = x
            if x == 1:
                self.p.x = 0
                self.p.y = 0
            if x == 2:
                self.p.x = width - self.width
                self.p.y = 0
            if x == 3:
                self.p.x = width - self.width
                self.p.y = height - self.height
            if x == 4:
                self.p.x = 0
                self.p.y = height - self.height
        else:
            self.p.x = x
            self.p.y = y
############################################################
# 
############################################################
    def setScale(self, x):
        self.scaleDownFactor = x
        self.width = self.CS.width / self.scaleDownFactor
        self.height = self.CS.height / self.scaleDownFactor
        if self.posValue != 0:
            self.setPosition(self.posValue)
############################################################
# 
############################################################
    def draw(self):
        self.drawFrame()
        self.drawTargets()
        self.drawViewWindow()
############################################################
# 
############################################################
    def drawFrame(self):
        self.width = self.CS.width / self.scaleDownFactor
        self.height = self.CS.height / self.scaleDownFactor
        pushStyle()
        fill(self.mapColor)
        rect(self.p.x, self.p.y, self.width, self.height)
        popStyle()
############################################################
# 
############################################################
    def drawTargets(self):
        size = self.targetSize
        for i in range(0, len(self.targets)):
            x = float(
                self.p.x) + (float(self.targets[i].p.x) * (float(self.width) / float(self.CS.width)))
            y = float(
                self.p.y) + (float(self.targets[i].p.y) * (float(self.height) / float(self.CS.height)))
            if x > self.p.x and x < (self.p.x + self.width):
                if y > self.p.y and y < (self.p.y + self.height):
                    pushStyle()
                    fill(self.targetColor)
                    noStroke()
                    ellipse(x, y, size, size)
                    popStyle()
############################################################
# 
############################################################
    def drawViewWindow(self):
        x = float(self.p.x) - (float(self.CS.originX)
                               * (float(self.width) / float(self.CS.width)))
        y = float(self.p.y) - (float(self.CS.originY)
                               * (float(self.height) / float(self.CS.height)))
        sizeX = float(width) * (float(self.width) / float(self.CS.width))
        sizeY = float(height) * (float(self.height) / float(self.CS.height))
        pushStyle()
        noFill()
        strokeWeight(30 / self.scaleDownFactor)
        stroke(self.frameColor)

        # draws each side of the view rectangle
        line(x, y, x + sizeX, y)  # top
        line(x, y, x, y + sizeY)  # left
        line(x + sizeX, y, x + sizeX, y + sizeY)  # right
        line(x, y + sizeY, x + sizeX, y + sizeY)  # bottom
        popStyle()
############################################################
############################################################
############################################################
############################################################
############################################################
############################################################
# a clock has a time(millisecond,centisecond,decisecond,
# second, minute, and hour), a way to retrieve incremental time
# and a way to print out formatted time.
# this object is made to be used with the timer object.
############################################################
class Clock(object):
############################################################
# constructor
############################################################
    def __init__(self):
        self.startTime = time.time() #referenced start time
        self.endTime = time.time() # current time
        self.elapsedTime = 0 #endTime - startTime
        self.active = True #controls if clock is active
        self.ms = 0 #millisecond
        self.cs = 0 #centisecond
        self.ds = 0 #decisecond
        self.s = 0 #second
        self.m = 0 #minute
        self.h = 0 #hour
        self.startS = 0 #offset seconds
        self.startM = 0 #offset minute
        self.startH = 0 #offset hour
        self.schedule = []
############################################################
# updates endTime and assigns ms,cs,ds,s,m,h variables
############################################################
    def updateTime(self):
        self.endTime = time.time()
        if self.active:
            self.elapsedTime = self.endTime - self.startTime
        self.ms = int((self.elapsedTime * 1000) % 10)
        self.cs = int((self.elapsedTime * 100) % 10)
        self.ds = int((self.elapsedTime * 10) % 10)
        self.s = int(((self.elapsedTime * 1) + self.startS) % 60)
        self.m = int(
            (((self.elapsedTime + self.startS) / 60) + self.startM) % 60)
        self.h = int(
            (((self.elapsedTime + (self.startM * 60) + self.startS) / 3600) + self.startH) % 24)
############################################################
# resets timer to 00:00:00
############################################################
    def reset(self):
        self.startTime = time.time()
        self.active = True
############################################################
# stops the Timer from updating time
############################################################
    def stop(self):
        self.active = False
############################################################
# starts Timer from the nearest second
############################################################
    def start(self):
        self.startS = self.s
        self.startM = self.m
        self.startH = self.h
        self.startTime = time.time()
        self.active = True
############################################################
# sets the initial/start time of the Timer
############################################################
    def setTime(self, h, m=None, s=None):
        self.startH = h % 24
        if m != None:
            self.startM = m % 60
        if s != None:
            self.startS = s % 60
############################################################
# returns total elapsed hours
############################################################
    def elapsedH(self):
        self.updateTime()
        h = int(self.getH())
        return h
############################################################
# returns total elapsed minutes
############################################################
    def elapsedM(self):
        self.updateTime()
        return ((self.m) + (self.h * 60))
############################################################
# returns total elapsed seconds
############################################################
    def elapsedS(self):
        self.updateTime()
        return (self.s + (self.m * 60) + (self.h * 360))
############################################################
# returns total elapsed deciseconds
############################################################
    def elapsedDS(self):
        self.updateTime()
        return (self.elapsedS() * 10 + self.ds)
############################################################
# returns total elapsed centiseconds
############################################################
    def elapsedCS(self):
        self.updateTime()
        return (self.elapsedDS() * 10 + self.cs)
############################################################
# returns total elapsed milliseconds
############################################################
    def elapsedMS(self):
        self.updateTime()
        return (self.elapsedCS() * 10 + self.ms)
############################################################
# prints formatted time up to the nearest second
############################################################
    def printTime(self):
        self.updateTime()
        # hour formatting
        if self.h < 10:
            h = "0%1.0f:" % floor(self.h)
        else:
            h = "%1.0f:" % floor(self.h)
        # minute formatting
        if self.m < 10:
            m = "0%1.0f:" % floor(self.m)
        else:
            m = "%1.0f:" % floor(self.m)
        # second formatting
        if self.s < 10:
            s = "0%1.0f" % floor(self.s)
        else:
            s = "%1.0f" % floor(self.s)
        return h + m + s
############################################################
# prints formatted time up to the millisecond
############################################################
    def printMSTime(self):
        self.updateTime()
        ds = str(".%1.0f" % floor(self.ds))
        cs = str("%1.0f" % floor(self.cs))
        ms = str("%1.0f" % floor(self.ms))
        return self.printTime() + ds + cs + ms
############################################################
# 
############################################################
    def onInterval(self,func,timeInterval):
        self.updateTime()
        self.schedule.append(Event(func,timeInterval,self.endTime))
        
    def runSchedule(self):
        self.updateTime()
        for i in range(0,len(self.schedule)):
            if self.schedule[i].actionTime < self.endTime:
                self.schedule[i].runEvent()
                self.schedule[i].setNewActionTime()
                
        
class Event(object):
    def __init__(self,callback,timeInterval,startTime):
        self.timeInterval = timeInterval
        self.startTime = startTime
        self.actionTime = startTime + timeInterval
        self.event = callback
        
    def runEvent(self):
        self.event()
        
    def setNewActionTime(self):
        self.actionTime += self.timeInterval
        
    def toString(self):
        return str(self.timeInterval) + " " + str(self.startTime) + " " + str(self.actionTime)
        