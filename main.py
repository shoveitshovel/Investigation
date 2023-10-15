def areAngles90(A, B, C, D):
    if float(A[0]) == float(B[0]) and float(A[2]) == float(D[2]):
        DAB = True
    if float(B[0]) == float(C[0]) and float(B[2]) == float(A[2]):
        ABC = True
    if float(C[0]) == float(D[0]) and float(C[2]) == float(B[2]):
        BCD = True
    if float(C[0]) == float(A[0]) and float(D[2]) == float(C[2]):
        CDA = True
    if DAB == True and ABC == True and BCD == True and CDA == True:
        return True
    else:
        return False


print("Enter comma-separated coordinates in anticlockwise order:")
pointA = input("Vertex A: ")
pointB = input("Vertex B: ")
pointC = input("Vertex C: ")
pointD = input("Vertex D: ")

print(pointA, pointB, pointC, pointD)