'''------------------------------dog problem------------------------------------'''
'''Max has a dog, which is an integer N years old. Now he wants the age of his dog in 
human years. The internet says that 1 dog year equals to 7 human years. Your task is 
to find and return an integer value representing the age of Max's dog in human years.'''
'''def max_age(n):
    dog_h=n*7
    return dog_h

num=4
print(max_age(num))'''

''' --------------------------------space problem-------------------------------------------'''
''' you have been given the task of making the content on a social media platform more 
user-friendly. Your task is to find and return an integer value representing the count 
of the number of spaces in a given string S.

Input:
A string S
Output :
Return an integer value representing the count of the number of spaces in a given 
string S.
Example:
Input:
Hello World Hey
Output:
2'''

'''tup=("hello welcome")
print(tup.count(" "))
'''

'''str=input()
print(str.count(" "))'''

'''---------------------------------jar problem---------------------------------------------------'''
'''You are given an integer array of size N, representing jars of chocolates. Three 
students A, B, and C respectively, will pick chocolates one by one from each chocolate 
jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task 
is to fine and return an integer value representing the total number of chocolates that 
student A will have, after all the chocolates have been picked from all the jars.
Note: Once a jar is done A will start taking the chocolates from the new jar.
Input Format :
input1: An integer array representing the quantity of chocolates in each jar.
input2: An integer value N representing the number of jars.
Output Format:
Return an integer value representing the total number of chocolates that student A 
will have, after all the chocolates are picked.'''           
#map func is uesd in place of 'for' loop to take input in the list ,it is a ittration func
#list func is used to store the input in list
#split func is used to seaprate the integer values with commas
chocolate=list(map(int,input("enter the number of chocolates in the jars").split()))
N=len(chocolate)
count=0
for i in chocolate:
        if i==0:
            continue
        if i<=3:
            count=count+1
        else:
            if i%3==0:
                count=count+(i//3)
            else:
                count=count+(i//3)+1
print(count)
               

