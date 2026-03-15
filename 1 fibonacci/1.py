#METHOD 1: Using a FOR LOOP
#0,1
#1,2,3,5,8,13,21,34...

num1=0
num2=1

for i in range(8):
    nextFibo=num1+num2
    print(nextFibo)
    num1=num2
    num2=nextFibo
