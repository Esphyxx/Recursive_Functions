# Recursive Function Of Factorial
def Factorial(N):
    if N==1:
        return N
    else:
        return (N*Factorial(N-1))

Num=int(input("Input a number"))
Fact=Factorial(Num)
print("The Factorial of this number is:",Fact)

