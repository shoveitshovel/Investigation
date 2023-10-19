import math

def distance(a,b,c,d):
    e = b - a  

def areParralel(xa,xb,xc,xd,ya,yb,yc,yd):
    if xb-xa == 0 and xd-xc == 0:
        if yc-ya == 0 and yd-yb == 0:
            return "both"
        else:
            slope3 = (yc-ya)/(xc-xa)
            slope4 = (yd-yb)/(xc-xb)
            if slope3 == slope4:
                return "both"
            else:
                return "half"
    else:
        if yc-ya == 0 and yd-yc == 0:
            slope1 = (yb-ya)/(xb-xa)
            slope2 = (yd-yc)/(xd-xc)
            if slope3 == slope4:
                return "both"
            else:
                return "half"
    slope1 = (yb-ya)/(xb-xa)
    slope2 = (yd-yc)/(xd-xc)
    slope3 = (yc-ya)/(xc-xa)
    slope4 = (yd-yb)/(xd-xb)
    slope1 = abs(slope1)
    slope2 = abs(slope2)
    slope3 = abs(slope3)
    slope4 = abs(slope4)
    if slope1 == slope2 and slope3 == slope4:
        return "both"
    elif slope1 == slope2 or slope3 == slope4:
        return "half"
    else:
        return "none"
    
def areSidesEqual(xa,xb,xc,xd,ya,yb,yc,yd):
    misc1 = ((xb-xa)**2)+((yb-ya))**2
    misc2 = ((xc-xb)**2)+((yc-yb))**2
    misc3 = ((xd-xc)**2)+((yd-yc))**2
    misc4 = ((xa-xd)**2)+((ya-yd))**2
    side1 = math.sqrt(misc1)
    side2 = math.sqrt(misc2)
    side3 = math.sqrt(misc3)
    side4 = math.sqrt(misc4)
    if side1 == side2 and side2 == side3 and side3 == side4:
        return "all"
    elif side1 == side2 and side3 == side4 or side2 == side3 and side4 == side1:
        return "pair"
    else:
        return "none"
    
    



print("Enter comma separated coordinates in anticlockwise order:")
pointA = input("Vertex A: ")
pointB = input("Vertex B: ")
pointC = input("Vertex C: ")
pointD = input("Vertex D: ")
pointA=pointA.split(",")
pointB=pointB.split(",")
pointC=pointC.split(",")
pointD=pointD.split(",")
print(pointA)
print(pointB)
print(pointC)
print(pointD)
for i in range(len(pointA)):
    pointA[i] = int(pointA[i])
for i in range(len(pointB)):
    pointB[i] = int(pointB[i])
for i in range(len(pointC)):
    pointC[i] = int(pointC[i])
for i in range(len(pointD)):
    pointD[i] = int(pointD[i])

x1 = int(pointA[0])
x2 = int(pointB[0])
x3 = int(pointC[0])
x4 = int(pointD[0])
y1 = int(pointA[1])
y2 = int(pointB[1])
y3 = int(pointC[1])
y4 = int(pointD[1])

print(pointA)
print(pointB)
print(pointC)
print(pointD)

isParralel = areParralel(x1,x2,x3,x4,y1,y2,y3,y4)
isEqual = areSidesEqual(x1,x2,x3,x4,y1,y2,y3,y4)

print(isParralel)

print(x1,x2,x3,x4,y1,y2,y3,y4)
print(isEqual)


print(pointA, pointB, pointC, pointD)
