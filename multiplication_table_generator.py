num =  int(input("enter the table you want: "))
how = int(input(f"{num} upto: "))

for i in range (1,how+1):
    print(f"{i} X {num} = {i*num}")