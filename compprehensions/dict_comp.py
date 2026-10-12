#square numbers as pairs

square_numbers={x:x**2 for x in range(6)}
print(square_numbers)

#with condition

even_square_dict={x:x**2 for x in range(10)if x%2==0}
print(even_square_dict)