// 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255
function getnumsto225(){
    //  for loop to get all the numbers in 255
    for(let n =0; n < 256; n++){
        // prints the numbers as long as the loop runs
        console.log(n);
    }
}
// # calls function
// getnumsto225()

// 2. Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise
function getevens(){
    // for loop to check all number to 1000
    for (n=0; n<1001; n++){
        // if statement to check if its even using modulus operator
        if (n % 2 == 0){
            // prints only even numbers as long as loop runs
            console.log(n);
        }
    }
}
// calls function
// getevens()

// 3. Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999)
function returnoddsum(){
    // creating empty variable
    sum1=0
    // for loop for iterating through 5000
    for(let n = 0; n < 5000; n++){
        // if to see if its odd number
        if(n % 2 == 1){
            // adds all odd numbers together in the empty variable
            sum1 += n
        }
    }
    print(sum1)
}
// returnoddsum()

// # 4. Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14)
function iteratearray(arg){
    // creating empty variable
    sum1=0
    // for loop to iterate through the array
    for(let i = 0; i < arg.length; i++){
        // index of the array being added to the others
        sum1+= arg[i]
    }
    // printing the sum of the items in array
    console.log(sum1);
}
// function call
// iteratearray([2,3,4,5])

// # 5. Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
function findmax(list1){
    // creating a variable to store the max number
    maxnum = 0
    // for loop to iterate the list
    for(let n = 0; n < list1.length; n++){
        // checking to see if the number in the list is higher then previous numbers
        if(list1.i > maxnum){
            // if its larger then it will replace the number in the variable
            maxnum = list1[i]
        }
    }
    // prints a string with the max number
    console.log("The max number is " + maxnum);
}
// function call with the lists
findmax([-3,3,5,7])
// findmax([10,7,-4,8,3])