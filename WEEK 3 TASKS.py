#WEEK 3 TASK 1A Write a program that allows you to enter 4 numbers and stores them in a file called “Numbers”. Have a go at ‘w’ ‘r’ ‘a’
my_file = open("Numbers.txt","w")
my_1d_list = [3,45,83,21]
print (my_1d_list)
my_file.close()

my_file = open("Numbers.txt", "a")
my_1d2_list = [1, 3, 5, 7]
print (my_1d2_list)
my_file.close()

#task 2 Write a program to ask a student for their percentage mark and convert this to a grade
def mark_grade(inp_result):
    result =  inp_result
    if result  >= 80:
        print ("You got an A*")
    elif result >=70:
        print ("You got a A")
    elif result >=60:
        print ("You got a B")
    elif result >=50:
        print ("You got a C")
    elif result <50:
        print ("You did not pass the exam")
result =int( input ("what is your percentage mark?"))
mark_grade(result)
