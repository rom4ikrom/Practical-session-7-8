a  = int(input("Enter a number: "))

def fact(n):
    num = 1
    while n >= 1:
        num = num * n
        n -= 1
    return num

print(fact(a))
