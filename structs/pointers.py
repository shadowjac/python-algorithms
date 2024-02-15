
num1 = 11

num2 = 11


print("Before num2 value is updated:")
print("num1=", num1)
print("num2=", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

dict1 = { 'value': 11}
dict2 = dict1

print("\ndict1 to:", id(dict1))
print("dict2 to:", id(dict2))

dict2['value'] =22

print("\ndict1 to:", id(dict1))
print("dict2 to:", id(dict2))