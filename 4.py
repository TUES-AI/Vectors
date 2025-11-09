vector = [1,2,3]
vector2 = [2,3,4]

for i in range(3):
    print(vector[i], end=' ')
print()
for i in range(3):
    print(vector2[i], end=' ')

print("\nSum of the vectrors")
for i in range(3):
    print(vector[i]+vector2[i])

print("\nScalar multiplication of the vector1")
for i in range(3):
    print(vector[i]*10)
