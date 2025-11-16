# # 1. What is a Function?

# # A function is a self-contained block of code designed to carry out a specific task in programming language

# # 2. problem solved due to function?

# #  repeating the same code in multiple places made programs long, messy, and hard to manage. A function lets you write code once and reuse it whenever needed, which improves organization and reduces errors.


# #3. way of creating function?

# #  When you define a function, you give it a name, specify input parameters, write the task it should perform, and then call it anywhere in your program.
# #In Python, functions are created using the def keyword, followed by the function name and parentheses. This makes programming more efficient. Fit takes input, processes it, and produces an output.


# # 4. Types of Functions in Python

# # Python supports several types of functions, each serving different purposes. The  categories are:-

# # a. pre-defined functions, which are already available in Python and can be used without writing any code for them; examples include print(), len(), type(), and sum(). These help perform common operations quickly.

# # b. user-defined functions, which are created by the programmer using the def keyword. These allow you to customize behavior and solve your specific problem. 



# # 5. Example of predifine function :-

# text = "Hello Python"
# print(len(text))    # len() is a built-in function that returns length
# print(type(text))   # type() prints the data type of the value


# # 6. Example of userdifine function :-

# def greet(name):
#     print("Hello,", name)

# greet("Ayush")



# # 7. Catagories of function on the basis of paramter and return type ?

# # a. Functions Without Parameters and without Return type
# # Explanation:

# # These functions do not take any input and do not return anything.
# # They only perform a task such as printing a message.

# # Example Code:-
# def greet():
#     print("Hello! Welcome to Python functions.")

# greet()



# # b. Functions With Parameters and without Return type
# # Explanation:

# # These functions take inputs (parameters) but do not return any value.
# # They usually process the input and display the result directly.

# # Example Code:
# def show_square(num):
#     print("Square of", num, "is", num * num)

# show_square(6)



# # c. Functions Without Parameters but With Return type
# # Explanation:

# # These functions do not take any input, but they return a value when executed.
# # They are useful when the function itself generates or calculates something.

# # Example Code:
# def give_number():
#     return 10  # returns a fixed value

# value = give_number()
# print("Returned value:", value)



# # d. Functions With Parameters and with Return type
# # Explanation:

# # These are the most useful and common functions.
# # They take one or more inputs, perform a calculation, and return a result.

# # Example Code:
# def add(a, b):
#     return a + b

# result = add(5, 7)
# print("Sum =", result)

#------------------------------------------------THANK-YOU------------------------------------------------------------------------------- 