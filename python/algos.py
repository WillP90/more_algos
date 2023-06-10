# 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255
def getnumsto225():
    # for loop to get all the numbers in 255
    for n in range(256):
        # prints the numbers as long as the loop runs
        print(n)
# calls function
# getnumsto225()

# 2. Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise
def getevens():
    # for loop to check all number to 1000
    for n in range(1001):
        # if statement to check if its even using modulus operator
        if n % 2 == 0:
            # prints only even numbers as long as loop runs
            print(n)
# calls function
# getevens()

# 3. Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999)
def returnoddsum():
    # creating empty variable to hold sum of numbers
    sum1=0
    # for loop itterating through 5000
    for n in range(5000):
        # if statement finding odd number using modulus
        if n % 2 == 1:
            # adding all the numbers together by adding single number and replacng variable
            sum1 += n
    # printing the sum1 variable after running through the number
    print(sum1)
# returnoddsum()

# 4. Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14)
def iteratarray(arg):
    # creating empty variable
    sum1=0
    # for loop to iterate through the array
    for i in arg:
        # index of the array being added to the others
        sum1+=i
    # printing the sum of the items in array
    print(sum1)
# function call
# iteratarray([2,3,4,5])

# 5. Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
def findmax(list1):
    # creating a variable to store the max number
    maxnum = 0
    # for loop to iterate the list
    for n in list1:
        # checking to see if the number in the list is higher then previous numbers
        if n > maxnum:
            # if its larger then it will replace the number in the variable
            maxnum = n
    # prints a string with the max number
    print(f"The greatest number is {maxnum}")
# function calls with the lists
# findmax([-3,3,5,7])
# findmax([10,7,-4,8,3])

# 6. Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
# defining the definition with a list argument
def findAverage(list1):
    # setting up variables to store the sum of all the numbers, and the average
    sumnum = 0
    avenum = 0
    # for loop to iterate through the numbers on the list
    for n in list1:
        # adding all the numbers to get the sum
        sumnum += n
    # taking the sum and dividing it by the length of the list
    avenum = sumnum / len(list1)
    # printing the average of the list
    print(avenum)
# function call
# findAverage([1,3,5,7,20])

# 7. Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method
# function decleration taking one argument
def oddarray(list1):
    # setting up empty list to append to
    newlist = []
    # for loop to iterate through the list
    for n in list1:
        # if statement to check if number is odd using the remainder of modulus
        if n % 2 == 1:
            # if odd, appends the number to the new list
            newlist.append(n)
    # prints the result of the new appended list
    print(newlist)
# the function calls
# oddarray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

# 8. Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7)
# creating definition instance taking in a list and single integer to check it against
def greatertheny(list1, y):
    # creating the new list to append greater numbers to
    newlist1 = []
    # for loop to iterate through the list given
    for n in list1:
        # if statement to check if the list item is greater then the pre chosen y number
        if n > y:
            # if its larger, appends to the new list
            newlist1.append(n)
    # print statement to print valid numbers
    print(newlist1)
# function call for the list
# greatertheny([1,2,3,5,7,9], 3)

# 9. Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
# function definition bringing in a list
def squareitself(list1):
    # creating a new list to append to
    newlist1 = []
    # for loop to iterate through the list
    for n in list1:
        # taking the item in list and appending to new list after multiplying by itself
        newlist1.append(n*n)
    # prints the new list
    print(newlist1)
# function call with list of numbers
# squareitself([1,5,10,-2])

# 10. Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
def swapnegatives(list1):
    newlist1 =[]