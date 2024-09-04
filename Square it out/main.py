def SquaredValues(beg, end):
    lst = []  # Initialize an empty list to store squared values
    for i in range(beg, end):
        lst.append(i**2)  # Append the square of each number in the range to the list
    
    lst_even = []  # Initialize an empty list to store even squares
    lst_odd = []   # Initialize an empty list to store odd squares

    for i in lst:  # Iterate through the list of squared values
        if i % 2 == 0:
            lst_even.append(i)  # Append to even list if the number is even
        else:
            lst_odd.append(i)  # Append to odd list if the number is odd
    
    # Print the results after the loop completes
    print(f"Here is a list of even squares within the specified range: {lst_even}")
    print(f"Here is a list of odd squares within the specified range: {lst_odd}")

# Example usage:
SquaredValues(1, 10)