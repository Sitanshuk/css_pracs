n = int(input("Enter a prime Number"))

g = int(input("Enter a prime Number"))

x = int(input("Enter a Random Number for User 1: "))

y = int(input("Enter a Random Number for User 2: "))

a = (g**x)%n

b = (g**y)%n

k1 = (b**x)%n

k2 = (a**y)%n

print("A:",a)

print("B:",b)

print("K1:",k1)

print("K2:",k2)