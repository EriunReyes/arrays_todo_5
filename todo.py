# Implement function sigma(num) that given a number, returns the sum of all positive integers up to number (inclusive).
#  Ex.: sigma(3) = 6 (or 1 + 2 + 3); sigma(5) = 15 (or 1 + 2 + 3 + 4 + 5).

# def sigma(num):
#     if num == 0:
#         return 0
#     else:
#         return sigma(num - 1) + num

# print(sigma(5))




# Just the Facts, ma’am. Factorials, that is. Write a function factorial(num) that, given a number, 
# returns the product (multiplication) of all positive integers from 1 up to number (inclusive). 
#For example, factorial(3) = 6 (or 1 * 2 * 3); factorial(5) = 120 (or 1 * 2 * 3 * 4 * 5).

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return factorial(num - 1) * num


# print(factorial(5))
# def drawLeftStars(num):
#     for num in range(15):
#         print("*****")


# drawLeftStars(15)


# def drawRightStars(num):
#     for num in range(num):
#         print("                                                                                                                              *****")


# drawRightStars(75)



# def drawCenteredStars(num):
#     for num in range(num):
#         print("                                                   *****                                         ")


# drawCenteredStars(75)


# def battle(ship1):
#     for ship1 in range(ship1):
#         print("     (=*=)                       >0<")
#         print(      "      (=*=)        >0<")
#         print(     "           (=*=)             >0<")
#         print("     (=*=)         >0<")
#         print("      (=*=)                    >0<")

# battle(5)



# def drawleftchar(num, char):
#     for i in range(10):
#         print(num, char)

# drawleftchar(5, "halo")


# def drawrightchar(num, char):
#     for i in range(10):
#         print("---------------------------------------------------------------------------------------------------------------------------------",num, char)

# drawrightchar(5, "halo")


def drawcenteredchar(num, char):
    for i in range(10):
        print("---------------------------------",num, char,"---------------------")

drawcenteredchar(5, "halo")




