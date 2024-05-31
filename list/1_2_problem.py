
a=2
b=2
c=2
n=2
coordinates = [[x, y, z] for x in range(a + 1) for y in range(b + 1) for z in range(c + 1) if x + y + z != n]
print(coordinates)


