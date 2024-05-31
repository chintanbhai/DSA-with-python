Tuple= (12 , 32 , 'hello', 12.5)
print(Tuple)

# Tuple is immutable, so we can't change the value of tuple
# Tuple[0] = 23
# print(Tuple)
# TypeError: 'tuple' object does not support item assignment

#function of tuple
print("Length of Tuple : ", len(Tuple))
print("Type of Tuple : ", type(Tuple))
print("Tuple[0] : ", Tuple[0])
print("Tuple[-1] : ", Tuple[-1])
print("Tuple[-2] : ", Tuple[-2])
print("Tuple[-3] : ", Tuple[-3])

# Tuple slicing
print("Tuple[1:3] : ", Tuple[1:3])
print("Tuple[1:] : ", Tuple[1:])
print("Tuple[:3] : ", Tuple[:3])
print("Tuple[-3:-1] : ", Tuple[-3:-1])

# Tuple concatenation
Tuple1 = (12, 23, 34)
Tuple2 = ('hello', 'world')
Tuple3 = Tuple1 + Tuple2
print("Tuple3 : ", Tuple3)

# Tuple repetition
Tuple4 = Tuple1 * 3
print("Tuple4 : ", Tuple4)

# Tuple membership
print("12 in Tuple1 : ", 12 in Tuple1)

# Tuple iteration
for i in Tuple1:
    print(i)

# Tuple unpacking
a, b, c = Tuple1
print("a : ", a)
print("b : ", b)
print("c : ", c)

# Tuple deletion
del Tuple1
# print(Tuple1)
# NameError: name 'Tuple1' is not defined

# Tuple count
Tuple5 = (12, 23, 34, 12, 23, 12)
print("Tuple5.count(12) : ", Tuple5.count(12))

# Tuple index
print("Tuple5.index(23) : ", Tuple5.index(23))

# Tuple sorting
Tuple6 = (12, 23, 34, 12, 23, 12)
print("Tuple6 : ", Tuple6)
Tuple7 = sorted(Tuple6)
print("Tuple7 : ", Tuple7)

# Tuple reverse
Tuple8 = (12, 23, 34, 12, 23, 12)
print("Tuple8 : ", Tuple8)
Tuple9 = reversed(Tuple8)
print("Tuple9 : ", Tuple9)

# Tuple min
Tuple10 = (12, 23, 34, 12, 23, 12)
print("Tuple10 : ", Tuple10)
print("min(Tuple10) : ", min(Tuple10))

# Tuple max
Tuple11 = (12, 23, 34, 12, 23, 12)
print("Tuple11 : ", Tuple11)
print("max(Tuple11) : ", max(Tuple11))


# Tuple sum
Tuple12 = (12, 23, 34, 12, 23, 12)
print("Tuple12 : ", Tuple12)
print("sum(Tuple12) : ", sum(Tuple12))

# Tuple all
Tuple13 = (12, 23, 34, 12, 23, 12)
print("Tuple13 : ", Tuple13)
print("all(Tuple13) : ", all(Tuple13))