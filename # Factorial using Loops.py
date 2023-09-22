# Factorial using Loops

def Factorial(N):
    F=1
    for C in range(N,1,-1):
        F*=C
    return F

Num=int(input("Input a number "))
Fact=Factorial(Num)
print("The Factorial of this number is:",Fact)

