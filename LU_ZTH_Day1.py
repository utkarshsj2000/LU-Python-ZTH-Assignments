# Assignment: Take multiple numbers through input and print the sum of the numbers.

x = input("Enter all Values:")  # 10 20 30 40 50 60 70 90 50
y = x.split()
add = 0

print(y)
for i in y:
    add += int(i)
print('Sum of all input No. is:', add)
