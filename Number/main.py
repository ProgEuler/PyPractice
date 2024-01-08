n = int(input("Enter a number: "))

# Using list comprehension to create a list of strings
numbers = [str(i) for i in range(1, n+1)]

# Join the list of strings without any separator and print the result
print(''.join(numbers))
