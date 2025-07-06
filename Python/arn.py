arn = "arn:aws:iam::123456789012:user/johndoe"
#print(arn.split(":"))
I = (arn.split(":")[2])
user = (arn.split(":")[5])

print(I + " " + user)

print(len(arn))

result = abs(-7)
print("Absolute value" , result)

print(f"The absolute value is {result}")