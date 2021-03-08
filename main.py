## Midterm test for Advanced Embedded ##

## Part 1 Leibniz Formula


# This is my main function for solving the equation

def pi_estimation(n):
    pi_value = 0  # setting value for pi
    numerator = 4.0  # setting the value of my numerator

    for i in range(n):  # setting the condition of my for loop to run as many times are the user has entered
        denomantor = (2 * i + 1)  # using the value i to calculate me demonator based on which iriteration
        term = numerator / denomantor  # main division of the equation
        if i % 2:  # depending on the i value, it will either add or subtract to the final pi value
            pi_value -= term
        else:
            pi_value += term
    return (pi_value)  # returning pi_value to be printed to the console


# main were my code will be executed
if __name__ == "__main__":
    print("Enter how many times you wold like to run the function!")  # Asking for user input
    n = int(input())  # setting n equal to the user input
    print(pi_estimation(n))  # printing the returned value of pi to my console
