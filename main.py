import math

def difference(a,b,):
    if a < b:
        return b - a
    else:
        return a - b    

#def areParralel(xa,xb,xc,xd,ya,yb,yc,yd):
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
    side1x = difference(xa,xb)
    side2x = difference(xb,xc)
    side3x = difference(xc,xd)
    side4x = difference(xd,xa)
    side1y = difference(ya,yb)
    side2y = difference(yb,yc)
    side3y = difference(yc,yd)
    side4y = difference(yd,ya)
    if side1x == side2y and side1y == side2x:
        side12equal = True
    else:
        side12equal = False
    if side2x == side3y and side2y == side3x:
        side23equal = True
    else:
        side23equal = False
    if side3x == side4y and side3y == side4x:
        side34equal = True
    else:
        side34equal = False
    if side4x == side1y and side4y == side1x:
        side41equal = True
    else:
        side41equal = False
    if side12equal == True and side23equal == True and side34equal == True and side41equal == True:
        return "allsides"
    elif side12equal == True and side34equal == True:
        return "twopairs"
    elif side23equal == True and side41equal == True:
        return "twopairs"
    else:
        return "notequal"
    
    



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

#isParralel = areParralel(x1,x2,x3,x4,y1,y2,y3,y4)
isEqual = areSidesEqual(x1,x2,x3,x4,y1,y2,y3,y4)

#print(isParralel)

print(x1,x2,x3,x4,y1,y2,y3,y4)
print(isEqual)


print(pointA, pointB, pointC, pointD)
