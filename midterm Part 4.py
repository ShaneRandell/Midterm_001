## Midterm Exam Part 4

import csv  # imports the csv library

file = open("book.csv", "a")  # Opening a file called book.csv for appending
title = input("enter a title: ")  # asking the user to enter a title
author = input("Enter author: ")  # asking the user to enter a author
year = input("Enter the year it was released: ")  # askign the user to enter year book was published
newrecord = title + "," + author + "," + year + "\n"  # creating a string to combine all the entered information
file.write(str(newrecord))  # writing to the file all the information the user inputted
file.close()  # closing the file

file = open("Book.csv", "r")  # opening the file for reading
for row in file:  # for loop with the condition to print all the rows in the file
    print(row)  # printing the contents of rows in the file
file.close()  # closing the file
