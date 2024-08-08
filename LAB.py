
#Lab exp 1 : Write python program to print list of numbers using range and for loop.
# L=[]
# for i in range (0, 20, 2):
#   L.append(i)
# print(L)


#Lab exp 2 : Write python program to print first n prime numbers.

# def is_prime(num):
#     """Check if a number is a prime number."""
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def print_first_n_primes(n):
#     """Print the first n prime numbers."""
#     count = 0
#     num = 2
#     while count < n:
#         if is_prime(num):
#             print(num, end=' ')
#             count += 1
#         num += 1
#
# # Number of prime numbers to print
# n =int (input("Enter the number for prime numbers to print: "))
# print_first_n_primes(n)


#Lab exp 3 : Write python program to multiply matrices.

# def matrix_multiply(A, B):
#     """Multiply two matrices A and B."""
#     # Get the number of rows and columns for each matrix
#     rows_A, cols_A = len(A), len(A[0])
#     rows_B, cols_B = len(B), len(B[0])
#
#     # Check if the matrices can be multiplied
#     if cols_A != rows_B:
#         raise ValueError("Number of columns in A must be equal to number of rows in B.")
#
#     # Initialize the result matrix with zeros
#     result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
#
#     # Perform matrix multiplication
#     for i in range(rows_A):
#         for j in range(cols_B):
#             for k in range(cols_A):
#                 result[i][j] += A[i][k] * B[k][j]
#
#     return result
#
# # Example matrices
# A = [
#     [1, 2, 3],
#     [4, 0, 6],
#     [1, 8, 4]
# ]
#
# B = [
#     [0, 8, 4],
#     [1, 10, 4],
#     [3, 2, 1]
# ]
#
# # Multiply matrices A and B
# result = matrix_multiply(A, B)
#
# # Print the result
# for row in result:
#     print(row)


#Lab exp 5 : Write python program in which a function is defined and calling that function prints‘Hello World’.

# def print_hello_world():
#   print("Hello World.")
#
# print_hello_world()

#Lab exp 6 : Write python program to let user enter some data in string and then verify data and print "welcome to user" .

# def verify_data(data):
#     """Verify the data entered by the user."""
#     # For this example, let's say the verification is just checking if the data is not empty
#     if data.strip() == "":
#         return False
#     return True
#
# # Prompt the user to enter some data
# user_data = input("Please enter your data: ")
#
# # Verify the entered data
# if verify_data(user_data):
#     print("Welcome, user!")
# else:
#     print("Invalid data entered. Please try again.")

# Lab exp 7 : Write python program to store strings in list and then print them.

# # Initialize an empty list to store strings
# string_list = []
#
# # Get the number of strings from the user
# num_strings = int(input("Enter the number of strings: "))
#
# # Get the strings from the user and add them to the list
# for i in range(num_strings):
#   string = input(f"Enter string {i+1}: ")
#   string_list.append(string)
#
# # Print the strings in the list
# print("The strings you entered are:")
# for string in string_list:
#   print(string)

# Lab exp 9 : Write python program in which a class is defined, then create object of that class and call simple ‘print function’ defined in class.

# class MyName:
#   def print_message(self):
#     print("My name is Rudraksh.")
#
# # Create an object of the class
# my_object = MyName()
#
# # Call the print function
# my_object.print_message()

# Lab exp 10 : Write python program in which an function (with single string parameter ) is defined and calling that function prints the string parameters given to function.

# def print_string(s1):
#   """Prints the string passed as a parameter."""
#   print(s1)
#
# # Call the function with a string
# print_string("Hello, I'm Lakshay and this is my Lab record .")