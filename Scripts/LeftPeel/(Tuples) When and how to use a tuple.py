# Usually when you make a whole bunch of tuplers,m you will put them in a list
# or do something with them because you are collecting data with them for a purpose

pt1 = (3, 4)
pt2 = (5, 10)
pt3 = (10, -4)

print(len(pt1)) # You can use the len ability to check the length of lists and tuples

print(5 in pt1) # The in ability also works with lists and tuples
print(5 in pt2)

set_of_pts = [pt1, pt2, pt3]
print(set_of_pts)
print(set_of_pts[0][1]) 
# 4
# You can print of the elemtents of a tuple from a list.
# This will access the first tuple and the 2nd element/or 1st index of it.

print(set_of_pts[2][1])
# -4

x, y = pt1
print(x)
print(y)
# 3
# 4
# This will print out pt1 as individual elements

# Now if there were 3 elements in the tuple it wouldn't work with 2 variables

# pt1 = (3, 4, 10)

# line 23, in <module>  
#     x, y = pt1
# ValueError: too many values to unpack (expected 2)
# unpacked means its trying to unpack all the variables of the tuple

# x, y, z = pt1
# print(x)
# print(y)
# print(z)
# 3
# 4
# 10

# set_of_pts = [pt1, pt2, pt3]

for x, y in set_of_pts:
    print(str(x) + " " + str(y))
3 4
5 10
10 -4           # This works if you include z with 3 elements