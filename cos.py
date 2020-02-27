import math

__author__="NullString"

m=-1

print("Cosine calculator - calculate angle or side\n\n")

while m != 0 and m != 1:
    m=int(input("Calculate Side (0) or Angle (1): "))

if m == 0:
    while True:
        A=int(input("A: "))
        b=float(input("b: "))
        c=float(input("c: "))
        print("a^2 = {0}^2 + {1}^2 - 2*{0}*{1}*cos({2})".format(b, c, A))
        bc=round(b**2+c**2, 2)
        bcos=round(2*b*c*math.cos(math.radians(A)), 2)
        print("a^2 = {0} - {1}".format(bc, bcos))
        asqr=round(bc - bcos, 1)
        print("a^2 = {0}".format(asqr))
        a=round(math.sqrt(asqr), 2)
        print("a = {0}".format(a))
        print("area = {0}".format(round(a*b*c/2, 2)))
        print("---------------------------------------------")
elif m == 1:
    while True:
        a=float(input("a: "))
        b=float(input("b: "))
        c=float(input("c: "))
        calc1="{0}^2+{1}^2-{2}^2".format(b, c, a)
        calc2="2*{0}*{1}".format(b, c)
        bca=round(b**2 + c**2 - a**2, 2)
        bc=round(2*b*c, 2)
        print(" "*7 + calc1)
        print("cosA = " + ("-"*len(calc1)))
        print(" "*((len(calc1)-len(calc2))//2+7)+calc2)
        #
        print("\n")
        calc1="{0}".format(bca)
        print(" "*7 + calc1)
        print("cosA = " + ("-"*len(calc1)))
        calc2="{0}".format(bc)
        print(" "*((len(calc1)-len(calc2))//2+7)+calc2)
        #
        print("\n")
        cosA=round(bca/bc, 2)
        print("cosA = {0}".format(cosA))
        #
        print("\n")
        angle=round(math.acos(math.radians(cosA)), 2)
        print("A = {0}°".format(angle))
        print("---------------------------------------------")
  
