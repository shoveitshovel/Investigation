import math

def rightAngles(xa,xb,xc,xd,ya,yb,yc,yd):
    side1 = ((xb-xa)**2)+((yb-ya))**2
    side2 = ((xc-xb)**2)+((yc-yb))**2
    side3 = ((xd-xc)**2)+((yd-yc))**2
    side4 = ((xa-xd)**2)+((ya-yd))**2
    hypo1 = ((xc-xa)**2)+((yc-ya))**2
    hypo2 = ((xd-xb)**2)+((yd-yb))**2
    hypo3 = ((xa-xc)**2)+((ya-yc))**2
    hypo4 = ((xb-xd)**2)+((yb-yd))**2
    if (side1) + (side2) == (hypo1):
        ABC = "right"
    else:
        ABC = "notright"
    if (side2) + (side3) == (hypo2):
        BCD = "right"
    else:
        BCD = "notright"
    if (side3) + (side4) == (hypo3):
        CDA = "right"
    else:
        CDA = "notright"
    if (side4) + (side1) == (hypo4):
        DAB = "right"
    else:
        DAB = "notright"
    if ABC == "right" and BCD == "right" and CDA == "right" and DAB == "right":
        return "allright"
    else:
        print(ABC,BCD,CDA,)
        return "notallright"
    
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

def areParralel(xa,xb,xc,xd,ya,yb,yc,yd):
    if xb-xa == 0 and xd-xc == 0:
        slope1 = 1
        slope2 = 1
    else:
        slope1 = (yb-ya)/(xb-xa)
        slope2 = (yd-yc)/(xd-xc)
    if xa-xd == 0 and xc-xb == 0:
        slope3 = 1
        slope4 = 1
    else:
        slope3 = (ya-yd)/(xa-xd)
        slope4 = (yc-yb)/(xc-xb)
    if slope1 == slope2 and slope3 == slope4:
        return "both"
    elif slope1 == slope2 or slope3 == slope4:
        return "half"
    else:
        return "none"
    

isLoopDone = False
print("Enter comma separated coordinates in anticlockwise order:")
pointA = input("Vertex A: ")
pointA=pointA.split(",")
while isLoopDone == False:
    try:
        x1 = int(pointA[0])
        y1 = int(pointA[1])
        isLoopDone = True
    except ValueError:
        print("Error: Values entered are not valid coordinates. Please enter again")
        pointA = input("Vertex A: ")
        pointA=pointA.split(",")
        isLoopDone = False
isLoopDone = False
pointB = input("Vertex B: ")
pointB=pointB.split(",")
while isLoopDone == False:
    try:
        x2 = int(pointB[0])
        y2 = int(pointB[1])
        isLoopDone = True
    except ValueError:
        print("Error: Values entered are not valid coordinates. Please enter again")
        pointB = input("Vertex B: ")
        pointB=pointB.split(",")
        isLoopDone = False
isLoopDone = False
pointC = input("Vertex C: ")
pointC=pointC.split(",")
while isLoopDone == False:
    try:
        x3 = int(pointC[0])
        y3 = int(pointC[1])
        isLoopDone = True
    except ValueError:
        print("Error: Values entered are not valid coordinates. Please enter again")
        pointC = input("Vertex C: ")
        pointC=pointC.split(",")
        isLoopDone = False
isLoopDone = False
pointD = input("Vertex D: ")
pointD=pointD.split(",")
while isLoopDone == False:
    try:
        x4 = int(pointD[0])
        y4 = int(pointD[1])
        isLoopDone = True
    except ValueError:
        print("Error: Values entered are not valid coordinates. Please enter again")
        pointD = input("Vertex D: ")
        pointD=pointD.split(",")
        isLoopDone = False

isParralel = areParralel(x1,x2,x3,x4,y1,y2,y3,y4)
isEqual = areSidesEqual(x1,x2,x3,x4,y1,y2,y3,y4)
areAngles = rightAngles(x1,x2,x3,x4,y1,y2,y3,y4)

print(x1,x2,x3,x4,y1,y2,y3,y4)
print(isParralel)
print(areAngles)
print(isEqual)

if isParralel == "both":
    print("Both pairs of sides are parralel")
    if isEqual == "all":
        print("All sides are equal")
        if areAngles == "allright":
            print("All angles are 90 degrees")
            print("All diagonals are perpendicular")
            print("Both diagonals bisect eachother")
            print("Both diagonals bisect the angle they pass through")
            print("Both diagonals are equal in length")
            print("This indicated that this quadrilateral is a square.")
        else:
            print("Not all angles are 90 degrees")
            print("All diagonals are perpendicular")
            print("Both diagonals bisect eachother")
            print("Both diagonals bisect the angle they pass through")
            print("Both diagonals are inequal in length")
            print("This indicated that this quadrilateral is a rhombus.")
    else:
        print("Not all sides are equal")
        if areAngles == "allright":
            print("All angles are 90 degrees")
            print("All diagonals are not perpendicular")
            print("Both diagonals bisect eachother")
            print("Neither diagonals bisect the angle they pass through")
            print("Both diagonals are equal in length")
            print("This indicated that this quadrilateral is a rectangle.")
        else:
            print("Not all angles are 90 degrees")
            print("All diagonals are not perpendicular")
            print("Both diagonals bisect eachother")
            print("Neither diagonals bisect the angle they pass through")
            print("Both diagonals are inequal in length")
            print("This indicated that this quadrilateral is a parralelogram.")
elif isParralel == "half":
    print("There is a pair of parralel sides")
    print("There are no equal sides")
    print("Not all angles are 90 degrees")
    print("All diagonals are not perpendicular")
    print("Niether diagonals bisect eachother")
    print("Neither diagonals bisect the angle they pass through")
    print("Both diagonals are inequal in length")
    print("This indicated that this quadrilateral is a trapezium.")
else:
    print("There are no parralel sides")
    if isEqual == "pair":
        print("There is a pair of adjacent equal sides")
        print("Not all angles are 90 degrees")
        print("All diagonals are perpendicular")
        print("One diagonal bisects the other")
        print("One diagonal bisects the angle they pass through")
        print("Both diagonals are inequal in length")
        print("This indicated that this quadrilateral is a kite.")


