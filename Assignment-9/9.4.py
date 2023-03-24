'''This is problem to convert all the negative coordinates to a positive coordinates;
The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
We can add or delete any number from the coordinates ; however graph should not be changed;'''

def convert_coordinates(coordinates):
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)
    updated_coords = [(coord[0] + abs(min_x), coord[1] + abs(min_y)) for coord in coordinates]
    return updated_coords
'''lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
ele = (input())

lst.append(ele) # adding the element

tupl=tuple(lst) #converting list into tuple
print(tupl)'''
In=[(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
print(convert_coordinates(In))