#flatten the list of list
matrix=[[1,2],[3,4],[5,6]]
flat=[num for row in  matrix for num in row]
print(flat)

#range
pairs=[(x,y)for x in range(1,4) for y in range(1,4)]
print(pairs)