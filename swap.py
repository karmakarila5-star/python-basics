a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

print("Original values:")
print("a =", a)
print("b =", b)
print("c =", c)

a = a ^ b ^ c
b = a ^ b ^ c
c = a ^ b ^ c
a = a ^ b ^ c

print("Swapped values:")
print("a =", a)
print("b =", b)
print("c =", c)
