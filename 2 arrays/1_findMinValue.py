#Find The Lowest Value in an Array

my_array = [7, 12, 9, 4, 11,3]
fElement=my_array[0]

for i in my_array:
    if i<fElement:
        fElement=i

print("min value is: ",fElement)