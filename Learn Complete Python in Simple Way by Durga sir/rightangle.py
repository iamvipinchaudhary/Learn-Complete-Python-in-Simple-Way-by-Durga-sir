# to print * right angle triangle
n = int(input("Enter Number of rows:"))
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

# o/p
# C: \Users\vipin chaudhary\python\ python rightangle.py
# Enter Number of rows: 5
# *
# * *
# * * *
# * * * *
# * * * * *
