squares=[]

for x in range(1,6):
    squares.append(x**2)
print(squares)    

square_comp=[x**2 for x in range(1,6)]
print(square_comp)

#even_numbers

even_num=[x for x in range(1,6)if x%2==0]
print(even_num)

#with string
letters=[ch.upper()for ch in "hello"]
print(letters)
